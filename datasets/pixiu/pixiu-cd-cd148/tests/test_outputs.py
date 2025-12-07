import json
from pathlib import Path

PIXIU_ID = "cd148"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """Because:B-CAUSE
A:I-CAUSE
's:I-CAUSE
and:I-CAUSE
B:I-CAUSE
's:I-CAUSE
underlying:I-CAUSE
businesses:I-CAUSE
and:I-CAUSE
their:I-CAUSE
prospects:I-CAUSE
are:I-CAUSE
identical:I-CAUSE
,:O
it:B-EFFECT
also:I-EFFECT
appears:I-EFFECT
that:I-EFFECT
the:I-EFFECT
market:I-EFFECT
is:I-EFFECT
only:I-EFFECT
ascribing:I-EFFECT
$:I-EFFECT
750,000:I-EFFECT
in:I-EFFECT
value:I-EFFECT
to:I-EFFECT
the:I-EFFECT
$:I-EFFECT
1:I-EFFECT
million:I-EFFECT
excess:I-EFFECT
of:I-EFFECT
B:I-EFFECT
's:I-EFFECT
cash:I-EFFECT
balance:I-EFFECT
versus:I-EFFECT
A's.:I-EFFECT"""
NUM_TOKENS = 40

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
