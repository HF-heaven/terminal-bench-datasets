import json
from pathlib import Path

PIXIU_ID = "finerord619"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """(:O
Submitted:O
rendering:O
::O
BKV:B-ORG
Group:I-ORG
):O
Johnson:B-ORG
brothers:I-ORG
rethink:O
plan:O
for:O
St.:B-LOC
Paul:I-LOC
waterfront:I-LOC
By:O
::O
Adam:B-PER
Voge:I-PER
July:O
7:O
,:O
2015:O
4:06:O
pm:O
0:O
Shepard:B-LOC
Road:I-LOC
Development:O
is:O
actively:O
searching:O
for:O
other:O
ideas:O
after:O
the:O
city:O
of:O
St.:B-LOC
Paul:I-LOC
rejected:O
a:O
six:O
-:O
story:O
apartment:O
plan:O
on:O
19:O
acres:O
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
