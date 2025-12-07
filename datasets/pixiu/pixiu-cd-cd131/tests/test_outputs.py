import json
from pathlib import Path

PIXIU_ID = "cd131"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """Weakened:B-EFFECT
by:I-EFFECT
decades:I-EFFECT
of:I-EFFECT
mismanagement:I-EFFECT
and:I-EFFECT
an:I-EFFECT
excessive:I-EFFECT
local:I-EFFECT
exposure:I-EFFECT
,:I-EFFECT
Carige:I-EFFECT
has:I-EFFECT
piled:I-EFFECT
up:I-EFFECT
more:I-EFFECT
than:I-EFFECT
1.6:I-EFFECT
billion:I-EFFECT
euros:I-EFFECT
in:I-EFFECT
losses:I-EFFECT
since:I-EFFECT
2014:I-EFFECT
,:O
mostly:O
due:O
to:O
bad:B-CAUSE
loans.:I-CAUSE"""
NUM_TOKENS = 30

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
