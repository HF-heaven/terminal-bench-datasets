import json
from pathlib import Path

PIXIU_ID = "cd69"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """Select:B-CAUSE
your:I-CAUSE
country:I-CAUSE
Continue:I-CAUSE
Create:I-CAUSE
a:I-CAUSE
free:I-CAUSE
ResearchPool:I-CAUSE
account:I-CAUSE
to:I-CAUSE
access:I-CAUSE
full:I-CAUSE
reports:I-CAUSE
,:I-CAUSE
get:I-CAUSE
a:I-CAUSE
personalised:I-CAUSE
dashboard:I-CAUSE
and:I-CAUSE
follow:I-CAUSE
providers:I-CAUSE
or:I-CAUSE
companies:I-CAUSE
First:I-CAUSE
nameLast:I-CAUSE
nameGet:I-CAUSE
financial:I-CAUSE
insights:I-CAUSE
straight:I-CAUSE
to:I-CAUSE
your:I-CAUSE
inbox:I-CAUSE
Do:I-CAUSE
you:I-CAUSE
want:I-CAUSE
to:I-CAUSE
use:I-CAUSE
these:I-CAUSE
details:I-CAUSE
for:I-CAUSE
invoicing:I-CAUSE
Sign-up:I-CAUSE
Now:I-CAUSE
Email:I-CAUSE
Password:I-CAUSE
Sign-in:I-CAUSE
CIS:I-CAUSE
Market:I-CAUSE
Daily:I-CAUSE
-:I-CAUSE
April:I-CAUSE
24:I-CAUSE
,:I-CAUSE
2018:I-CAUSE
MARKET:I-CAUSE
COMMENT:I-CAUSE
-:I-CAUSE
LATE:I-CAUSE
RALLY:I-CAUSE
TRIMS:I-CAUSE
EARLIER:I-CAUSE
LOSSES:I-CAUSE
AS:I-CAUSE
INVESTORS:I-CAUSE
SCRUTINIZE:I-CAUSE
SANCTION:I-CAUSE
NEWSThe:I-CAUSE
RTS:I-CAUSE
was:I-CAUSE
trading:I-CAUSE
down:I-CAUSE
some:I-CAUSE
1.8:I-CAUSE
%:I-CAUSE
intraday:I-CAUSE
when:I-CAUSE
US:I-CAUSE
agency:I-CAUSE
OFAC:I-CAUSE
announced:I-CAUSE
a:I-CAUSE
series:I-CAUSE
of:I-CAUSE
clarifications:I-CAUSE
on:I-CAUSE
its:I-CAUSE
sanctions:I-CAUSE
on:I-CAUSE
RUSAL:I-CAUSE
and:I-CAUSE
other:I-CAUSE
companies.:I-CAUSE
The:I-EFFECT
market:I-EFFECT
subsequently:I-EFFECT
gained:I-EFFECT
more:I-EFFECT
than:I-EFFECT
2:I-EFFECT
pp:I-EFFECT
before:I-EFFECT
falling:I-EFFECT
back:I-EFFECT
for:I-EFFECT
an:I-EFFECT
overall:I-EFFECT
decline:I-EFFECT
of:I-EFFECT
0.1:I-EFFECT
%:I-EFFECT
for:I-EFFECT
the:I-EFFECT
day:I-EFFECT
at:I-EFFECT
1,145.:I-EFFECT"""
NUM_TOKENS = 115

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
