import json
from pathlib import Path

PIXIU_ID = "cd119"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """Previous:B-CAUSE
MGI:I-CAUSE
research:I-CAUSE
highlighted:I-CAUSE
China:I-CAUSE
's:I-CAUSE
working-age:I-CAUSE
population:I-CAUSE
as:I-CAUSE
one:I-CAUSE
of:I-CAUSE
the:I-CAUSE
key:I-CAUSE
global:I-CAUSE
consumer:I-CAUSE
segments:I-CAUSE
by:I-EFFECT
2030:I-EFFECT
,:I-EFFECT
they:I-EFFECT
are:I-EFFECT
projected:I-EFFECT
to:I-EFFECT
account:I-EFFECT
for:I-EFFECT
12:I-EFFECT
cents:I-EFFECT
of:I-EFFECT
every:I-EFFECT
$:I-EFFECT
1:I-EFFECT
of:I-EFFECT
worldwide:I-EFFECT
urban:I-EFFECT
consumption.:I-EFFECT"""
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
