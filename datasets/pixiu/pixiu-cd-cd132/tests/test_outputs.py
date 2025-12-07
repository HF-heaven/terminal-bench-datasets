import json
from pathlib import Path

PIXIU_ID = "cd132"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """NYSEARCA:B-CAUSE
::I-CAUSE
EUSA:I-CAUSE
traded:I-CAUSE
down:I-CAUSE
$:I-CAUSE
0.78:I-CAUSE
during:I-CAUSE
trading:I-CAUSE
hours:I-CAUSE
on:I-CAUSE
Tuesday:I-CAUSE
,:O
hitting:B-EFFECT
$:I-EFFECT
59.39.:I-EFFECT
23,400:O
shares:O
of:O
the:O
stock:O
traded:O
hands:O
,:O
compared:O
to:O
its:O
average:O
volume:O
of:O
22,384.:O
iShares:O
MSCI:O
USA:O
Equal:O
Weighted:O
ETF:O
has:O
a:O
1:O
year:O
low:O
of:O
$:O
47.02:O
and:O
a:O
1:O
year:O
high:O
of:O
$:O
60.89:O
.:O"""
NUM_TOKENS = 54

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
