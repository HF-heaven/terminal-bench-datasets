import json
from pathlib import Path

PIXIU_ID = "cd114"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """In:B-CAUSE
the:I-CAUSE
twelve:I-CAUSE
years:I-CAUSE
of:I-CAUSE
operation:I-CAUSE
there:I-CAUSE
have:I-CAUSE
been:I-CAUSE
several:I-CAUSE
hundred:I-CAUSE
individuals:I-CAUSE
involved:I-CAUSE
with:I-CAUSE
the:I-CAUSE
twelve:I-CAUSE
ownership:I-CAUSE
groups:I-CAUSE
,:I-CAUSE
with:I-CAUSE
group:I-CAUSE
number:I-CAUSE
thirteen:I-CAUSE
currently:I-CAUSE
forming.:I-CAUSE
As:I-EFFECT
Howard:I-EFFECT
points:I-EFFECT
out:I-EFFECT
,:I-EFFECT
LandMark:I-EFFECT
groups:I-EFFECT
never:I-EFFECT
own:I-EFFECT
100:I-EFFECT
percent:I-EFFECT
of:I-EFFECT
a:I-EFFECT
horse.:I-EFFECT"""
NUM_TOKENS = 39

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
