import json
from pathlib import Path

PIXIU_ID = "cd76"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """-:B-CAUSE
The:I-CAUSE
Penn:I-CAUSE
State:I-CAUSE
Board:I-CAUSE
of:I-CAUSE
Trustees:I-CAUSE
Committee:I-CAUSE
on:I-CAUSE
Finance:I-CAUSE
,:I-CAUSE
Business:I-CAUSE
and:I-CAUSE
Capital:I-CAUSE
Planning:I-CAUSE
today:I-CAUSE
(:I-CAUSE
Sept.:I-CAUSE
12:I-CAUSE
):I-CAUSE
recommended:I-CAUSE
a:I-CAUSE
state:I-CAUSE
appropriation:I-CAUSE
request:I-CAUSE
totaling:I-CAUSE
$:I-CAUSE
359.8:I-CAUSE
million:I-CAUSE
for:I-CAUSE
fiscal:I-CAUSE
year:I-CAUSE
2020-21:I-CAUSE
,:O
representing:O
an:B-EFFECT
increase:I-EFFECT
of:I-EFFECT
$:I-EFFECT
22.6:I-EFFECT
million:I-EFFECT
over:I-EFFECT
2019-20.:I-EFFECT"""
NUM_TOKENS = 43

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
