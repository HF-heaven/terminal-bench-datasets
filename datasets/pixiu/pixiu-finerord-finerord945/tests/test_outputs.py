import json
from pathlib import Path

PIXIU_ID = "finerord945"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """German:O
luxury:O
car:O
makers:O
Audi:B-ORG
,:O
a:O
unit:O
of:O
Volkswagen:B-ORG
AG:I-ORG
VLKAY:B-ORG
0.06:O
%:O
,:O
Mercedes:B-ORG
-:I-ORG
Benz:I-ORG
parent:O
Daimler:B-ORG
AG:I-ORG
DDAIY:B-ORG
0.85:O
%:O
,:O
and:O
BMW:B-ORG
AG:I-ORG
BMW:B-ORG
-:O
0.49:O
%:O
have:O
agreed:O
in:O
principle:O
to:O
purchase:O
the:O
telecommunications:O
group:O
’s:O
digital:O
mapping:O
service:O
Nokia:B-ORG
Here:O
,:O
according:O
to:O
a:O
person:O
familiar:O
with:O
the:O
situation:O
.:O"""
NUM_TOKENS = 57

ANSWER_FILE = Path("/app/answer.txt")
ITEM_FILE = Path("/tests/data/item.json")


def test_item_file_exists():
    assert ITEM_FILE.exists(), f"Missing data file for PIXIU sample {PIXIU_ID}"
    data = json.loads(ITEM_FILE.read_text())
    assert data.get("id") == PIXIU_ID
    assert data.get("label_type") == LABEL_TYPE


def _read_answer():
    assert ANSWER_FILE.exists(), "answer.txt was not created"
    return ANSWER_FILE.read_text().strip()


def test_answer_format():
    """Check that answer has the correct format (token:label per line)."""
    answer = _read_answer()
    lines = answer.strip().split('\n')
    
    # Should have one line per token
    assert len(lines) == NUM_TOKENS, \
        f"Expected {NUM_TOKENS} lines (one per token), got {len(lines)}"
    
    # Each line should be token:label
    for i, line in enumerate(lines):
        assert ':' in line, \
            f"Line {i+1} doesn't have token:label format: {line!r}"
        parts = line.split(':', 1)
        assert len(parts) == 2, \
            f"Line {i+1} should have exactly one colon: {line!r}"


def test_answer_matches_reference():
    """Check that answer matches the expected output."""
    answer = _read_answer()
    expected = EXPECTED_ANSWER.strip()

    # Normalize whitespace for comparison
    answer_normalized = '\n'.join(line.strip() for line in answer.split('\n') if line.strip())
    expected_normalized = '\n'.join(line.strip() for line in expected.split('\n') if line.strip())

    assert answer_normalized == expected_normalized, \
        f"Answer doesn't match expected output.\nExpected:\n{expected_normalized}\n\nGot:\n{answer_normalized}"
