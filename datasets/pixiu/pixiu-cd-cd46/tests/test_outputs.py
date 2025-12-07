import json
from pathlib import Path

PIXIU_ID = "cd46"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """Outlook:B-CAUSE
::I-CAUSE
Sector:I-CAUSE
tailwinds:I-CAUSE
intact:I-CAUSE
We:I-CAUSE
expect:I-CAUSE
pan-India:I-CAUSE
player:I-CAUSE
ACC:I-CAUSE
to:I-CAUSE
be:I-CAUSE
a:I-CAUSE
prime:I-CAUSE
beneficiary:I-CAUSE
of:I-CAUSE
the:I-CAUSE
positive:I-CAUSE
industry:I-CAUSE
fundamentals:I-CAUSE
.:I-CAUSE
We:I-EFFECT
continue:I-EFFECT
to:I-EFFECT
value:I-EFFECT
the:I-EFFECT
stock:I-EFFECT
at:I-EFFECT
12x:I-EFFECT
CY20e:I-EFFECT
EV/Ebitda:I-EFFECT
and:I-EFFECT
maintain:I-EFFECT
'BUY/SP'.:I-EFFECT"""
NUM_TOKENS = 34

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
