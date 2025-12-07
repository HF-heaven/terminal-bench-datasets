import json
from pathlib import Path

PIXIU_ID = "finerord615"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """The:O
report:O
also:O
shows:O
the:O
Bush:B-PER
camp:O
’s:O
taste:O
for:O
the:O
luxe:O
and:O
exclusive:O
,:O
with:O
payments:O
to:O
the:O
likes:O
of:O
the:O
Four:B-ORG
Seasons:I-ORG
Palo:I-ORG
Alto:I-ORG
,:O
the:O
St.:B-LOC
Regis:I-LOC
in:I-LOC
Atlanta:I-LOC
and:O
Houston:B-LOC
,:O
the:O
Hotel:B-ORG
Bel:I-ORG
Air:I-ORG
in:O
Los:B-LOC
Angeles:I-LOC
,:O
the:O
Mandarin:B-ORG
Oriental:I-ORG
in:O
San:B-LOC
Francisco:I-LOC
and:O
the:O
Union:B-ORG
League:I-ORG
of:O
Philadelphia:B-LOC
.:O"""
NUM_TOKENS = 56

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
