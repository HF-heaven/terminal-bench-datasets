import json
from pathlib import Path

PIXIU_ID = "cd154"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """Invesco:B-CAUSE
PureBeta:I-CAUSE
FTSE:I-CAUSE
Developed:I-CAUSE
ex-North:I-CAUSE
America:I-CAUSE
ETF:I-CAUSE
to:I-CAUSE
Issue:I-CAUSE
-:I-CAUSE
Dividend:I-CAUSE
of:I-CAUSE
$:I-CAUSE
0.17:I-CAUSE
(:I-CAUSE
BATS:I-CAUSE
::I-CAUSE
PBDM:I-CAUSE
):I-CAUSE
.:I-CAUSE
Stockholders:O
of:O
record:O
on:O
Tuesday:O
,:O
September:O
24th:O
will:O
be:O
paid:O
a:O
dividend:O
of:O
0.1747:O
per:O
share:O
on:O
Monday:O
,:O
September:O
30th:O
.:O
This:B-EFFECT
represents:I-EFFECT
a:I-EFFECT
dividend:I-EFFECT
yield:I-EFFECT
of:I-EFFECT
3:I-EFFECT
%:I-EFFECT
.:I-EFFECT"""
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
