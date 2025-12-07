import json
from pathlib import Path

PIXIU_ID = "cd108"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """Enerplus:B-CAUSE
Corp:I-CAUSE
(:I-CAUSE
NYSE:I-CAUSE
::I-CAUSE
ERF:I-CAUSE
):I-CAUSE
Announces:I-CAUSE
$:I-CAUSE
0.01:I-CAUSE
Monthly:I-CAUSE
Dividend:I-CAUSE
Daily:I-CAUSE
Ratings:I-CAUSE
&:I-CAUSE
News:I-CAUSE
for:I-CAUSE
Enerplus:I-CAUSE
Complete:I-CAUSE
the:I-CAUSE
form:I-CAUSE
below:I-CAUSE
to:I-CAUSE
receive:I-CAUSE
the:I-CAUSE
latest:I-CAUSE
headlines:I-CAUSE
and:I-CAUSE
analysts:I-CAUSE
':I-CAUSE
recommendations:I-CAUSE
for:I-CAUSE
Enerplus:I-CAUSE
with:I-CAUSE
our:I-CAUSE
free:I-CAUSE
daily:I-CAUSE
email:I-CAUSE
newsletter:I-CAUSE
::I-CAUSE
Enerplus:I-CAUSE
Corp:I-CAUSE
(:I-CAUSE
NYSE:I-CAUSE
::I-CAUSE
ERF:I-CAUSE
):I-CAUSE
(:I-CAUSE
TSE:I-CAUSE
::I-CAUSE
ERF:I-CAUSE
):I-CAUSE
announced:I-CAUSE
a:I-CAUSE
monthly:I-CAUSE
dividend:I-CAUSE
on:I-CAUSE
Tuesday:I-CAUSE
,:I-CAUSE
August:I-CAUSE
20th:I-CAUSE
,:I-CAUSE
NASDAQ:I-CAUSE
reports.:I-CAUSE
Investors:I-EFFECT
of:I-EFFECT
record:I-EFFECT
on:I-EFFECT
Friday:I-EFFECT
,:I-EFFECT
August:I-EFFECT
30th:I-EFFECT
will:I-EFFECT
be:I-EFFECT
given:I-EFFECT
a:I-EFFECT
dividend:I-EFFECT
of:I-EFFECT
0.008:I-EFFECT
per:I-EFFECT
share:I-EFFECT
by:I-EFFECT
the:I-EFFECT
oil:I-EFFECT
and:I-EFFECT
natural:I-EFFECT
gas:I-EFFECT
company:I-EFFECT
on:I-EFFECT
Monday:I-EFFECT
,:I-EFFECT
September:I-EFFECT
16th.:I-EFFECT
This:O
represents:O
a:O
$:O
0.10:O
dividend:O
on:O
an:O
annualized:O
basis:O
and:O
a:O
dividend:O
yield:O
of:O
1.31:O
%:O
.:O"""
NUM_TOKENS = 111

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
