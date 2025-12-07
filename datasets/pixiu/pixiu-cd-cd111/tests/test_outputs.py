import json
from pathlib import Path

PIXIU_ID = "cd111"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """BlackRock:B-CAUSE
Enhanced:I-CAUSE
Global:I-CAUSE
Dividend:I-CAUSE
Trust:I-CAUSE
(:I-CAUSE
NYSE:I-CAUSE
::I-CAUSE
BOE:I-CAUSE
):I-CAUSE
Holdings:I-CAUSE
Decreased:I-CAUSE
by:I-CAUSE
BB:I-CAUSE
&:I-CAUSE
T:I-CAUSE
Securities:I-CAUSE
LLC:I-CAUSE
BB:I-CAUSE
&:I-CAUSE
T:I-CAUSE
Securities:I-CAUSE
LLC:I-CAUSE
lessened:I-CAUSE
its:I-CAUSE
stake:I-CAUSE
in:I-CAUSE
shares:I-CAUSE
of:I-CAUSE
BlackRock:I-CAUSE
Enhanced:I-CAUSE
Global:I-CAUSE
Dividend:I-CAUSE
Trust:I-CAUSE
(:I-CAUSE
NYSE:I-CAUSE
::I-CAUSE
BOE:I-CAUSE
):I-CAUSE
by:I-CAUSE
10.5:I-CAUSE
%:I-CAUSE
during:I-CAUSE
the:I-CAUSE
second:I-CAUSE
quarter:I-CAUSE
,:I-CAUSE
according:I-CAUSE
to:I-CAUSE
the:I-CAUSE
company:I-CAUSE
in:I-CAUSE
its:I-CAUSE
most:I-CAUSE
recent:I-CAUSE
disclosure:I-CAUSE
with:I-CAUSE
the:I-CAUSE
SEC.:I-CAUSE
The:O
fund:O
owned:O
48,333:O
shares:O
of:O
the:O
financial:O
services:O
provider:O
's:O
stock:O
after:O
selling:O
5,662:O
shares:O
during:O
the:O
quarter:O
.:O
BB:B-EFFECT
&:I-EFFECT
T:I-EFFECT
Securities:I-EFFECT
LLC:I-EFFECT
's:I-EFFECT
holdings:I-EFFECT
in:I-EFFECT
BlackRock:I-EFFECT
Enhanced:I-EFFECT
Global:I-EFFECT
Dividend:I-EFFECT
Trust:I-EFFECT
were:I-EFFECT
worth:I-EFFECT
$:I-EFFECT
518,000:I-EFFECT
as:I-EFFECT
of:I-EFFECT
its:I-EFFECT
most:I-EFFECT
recent:I-EFFECT
SEC:I-EFFECT
filing.:I-EFFECT"""
NUM_TOKENS = 103

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
