import json
from pathlib import Path

PIXIU_ID = "cd225"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """-:O
-:O
Sell:O
Ratings:O
-:O
Hold:O
Ratings:O
-:O
Buy:O
Ratings:O
-:O
Strong:O
Buy:O
Ratings:O
-:O
Rating:O
Score:O
-:O
Cambium:O
Networks:O
-:O
0:O
-:O
2:O
-:O
4:O
-:O
0:O
-:O
2.67:O
-:O
Pointer:O
Telocation:O
-:O
0:O
-:O
2:O
-:O
0:O
-:O
0:O
-:O
2.00:O
Cambium:B-CAUSE
Networks:I-CAUSE
presently:I-CAUSE
has:I-CAUSE
a:I-CAUSE
consensus:I-CAUSE
target:I-CAUSE
price:I-CAUSE
of:I-CAUSE
$:I-CAUSE
13.58:I-CAUSE
,:O
suggesting:B-EFFECT
a:I-EFFECT
potential:I-EFFECT
upside:I-EFFECT
of:I-EFFECT
38.46:I-EFFECT
%:I-EFFECT
.:I-EFFECT"""
NUM_TOKENS = 63

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
