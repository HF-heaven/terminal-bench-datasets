import json
from pathlib import Path

PIXIU_ID = "cd73"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """WATER:O
RESOURCES:O
AND:O
FISHERIES:O
Madam:O
Speaker:O
,:O
Government:O
remains:O
committed:O
to:O
ensuring:O
access:O
to:O
safe:O
drinking:O
water:O
,:O
as:O
well:O
as:O
providing:O
timely:O
and:O
accurate:O
information:O
on:O
weather:O
and:O
climatic:O
conditions:O
for:O
the:O
nation:O
.:O
As:B-CAUSE
a:I-CAUSE
result:I-CAUSE
,:I-CAUSE
we:I-CAUSE
have:I-CAUSE
received:I-CAUSE
funds:I-CAUSE
from:I-CAUSE
the:I-CAUSE
African:I-CAUSE
Development:I-CAUSE
Bank:I-CAUSE
to:I-CAUSE
finance:I-CAUSE
the:I-CAUSE
Climate:I-CAUSE
Smart:I-CAUSE
Rural:I-CAUSE
WASH:I-CAUSE
Development:I-CAUSE
Project:I-CAUSE
for:I-CAUSE
infrastructure:I-CAUSE
and:I-CAUSE
service:I-CAUSE
improvement:I-CAUSE
over:I-CAUSE
a:I-CAUSE
period:I-CAUSE
of:I-CAUSE
about:I-CAUSE
sixty-three:I-CAUSE
(:I-CAUSE
63:I-CAUSE
):I-CAUSE
months:I-CAUSE
,:I-CAUSE
beginning:I-CAUSE
October:I-CAUSE
,:I-CAUSE
2018.:I-CAUSE
The:I-EFFECT
project:I-EFFECT
will:I-EFFECT
benefit:I-EFFECT
one:I-EFFECT
hundred:I-EFFECT
and:I-EFFECT
forty-four:I-EFFECT
(:I-EFFECT
144:I-EFFECT
):I-EFFECT
communities:I-EFFECT
and:I-EFFECT
increase:I-EFFECT
access:I-EFFECT
to:I-EFFECT
safe:I-EFFECT
water:I-EFFECT
by:I-EFFECT
17:I-EFFECT
%:I-EFFECT
and:I-EFFECT
safely-managed:I-EFFECT
sanitation:I-EFFECT
by:I-EFFECT
2:I-EFFECT
%:I-EFFECT
.:I-EFFECT"""
NUM_TOKENS = 105

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
