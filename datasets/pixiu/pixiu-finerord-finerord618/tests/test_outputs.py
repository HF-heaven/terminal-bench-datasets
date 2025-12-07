import json
from pathlib import Path

PIXIU_ID = "finerord618"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """Home:O
/:O
News:O
/:O
Construction:O
&:O
Development:O
/:O
Johnson:B-ORG
brothers:I-ORG
rethink:O
plan:O
for:O
St.:B-LOC
Paul:I-LOC
waterfront:I-LOC
Shepard:I-LOC
Road:I-LOC
Development:O
had:O
proposed:O
a:O
six:O
-:O
story:O
,:O
211:O
-:O
unit:O
apartment:O
building:O
at:O
2751:B-LOC
Shepard:I-LOC
Road:I-LOC
in:I-LOC
St.:I-LOC
Paul:I-LOC
,:O
near:O
the:O
Mississippi:O
River:O
,:O
but:O
that:O
plan:O
appears:O
unlikely:O
to:O
proceed:O
.:O"""
NUM_TOKENS = 52

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
