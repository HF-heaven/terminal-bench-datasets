import json
from pathlib import Path

PIXIU_ID = "cd215"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """Capital:B-EFFECT
gains:I-EFFECT
tax:I-EFFECT
(:I-EFFECT
CGT:I-EFFECT
):I-EFFECT
is:I-EFFECT
charged:I-EFFECT
at:I-EFFECT
the:I-EFFECT
rate:I-EFFECT
of:I-EFFECT
10:I-EFFECT
%:I-EFFECT
on:I-EFFECT
gains:I-EFFECT
(:I-EFFECT
including:I-EFFECT
any:I-EFFECT
held:I-EFFECT
over:I-EFFECT
gains:I-EFFECT
coming:I-EFFECT
into:I-EFFECT
charge:I-EFFECT
):I-EFFECT
where:O
net:B-CAUSE
total:I-CAUSE
taxable:I-CAUSE
gains:I-CAUSE
and:I-CAUSE
income:I-CAUSE
is:I-CAUSE
below:I-CAUSE
the:I-CAUSE
income:I-CAUSE
tax:I-CAUSE
basic:I-CAUSE
rate:I-CAUSE
band:I-CAUSE
threshold.:I-CAUSE"""
NUM_TOKENS = 42

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
