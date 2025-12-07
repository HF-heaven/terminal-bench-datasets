import json
from pathlib import Path

PIXIU_ID = "cd115"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """In:B-CAUSE
an:I-CAUSE
effort:I-CAUSE
to:I-CAUSE
prevent:I-CAUSE
the:I-CAUSE
federal:I-CAUSE
fund:I-CAUSE
rate:I-CAUSE
rising:I-CAUSE
further:I-CAUSE
the:I-CAUSE
central:I-CAUSE
bank:I-CAUSE
added:I-CAUSE
more:I-CAUSE
money:I-CAUSE
into:I-CAUSE
the:I-CAUSE
system:I-CAUSE
on:I-CAUSE
Thursday.:I-CAUSE
So:I-EFFECT
far:I-EFFECT
this:I-EFFECT
week:I-EFFECT
$:I-EFFECT
203:I-EFFECT
billion:I-EFFECT
has:I-EFFECT
been:I-EFFECT
injected:I-EFFECT
into:I-EFFECT
the:I-EFFECT
markets.:I-EFFECT"""
NUM_TOKENS = 35

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
