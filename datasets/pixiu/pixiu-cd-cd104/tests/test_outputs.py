import json
from pathlib import Path

PIXIU_ID = "cd104"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """The:B-CAUSE
mandate:I-CAUSE
to:I-CAUSE
issue:I-CAUSE
refunds:I-CAUSE
comes:I-CAUSE
under:I-CAUSE
a:I-CAUSE
provision:I-CAUSE
in:I-CAUSE
the:I-CAUSE
Affordable:I-CAUSE
Care:I-CAUSE
Act:I-CAUSE
that:I-CAUSE
limits:I-CAUSE
how:I-CAUSE
much:I-CAUSE
companies:I-CAUSE
can:I-CAUSE
keep:I-CAUSE
for:I-CAUSE
overhead:I-CAUSE
and:I-CAUSE
profit.:I-CAUSE
The:O
bulk:O
of:O
the:O
rebates:O
-:O
a:O
total:O
of:O
$:O
80.4:O
million:O
from:O
four:O
companies:O
-:O
will:O
go:O
to:O
those:O
who:O
overpaid:O
for:O
plans:O
purchased:O
on:O
the:O
individual:O
market:O
in:O
2018:O
,:O
according:O
to:O
data:O
from:O
the:O
federal:O
Centers:O
for:O
Medicaid:O
and:O
Medicare:O
Service:O
analyzed:O
by:O
the:O
Kaiser:O
Family:O
Foundation:O
.:O
The:B-EFFECT
rest:I-EFFECT
,:I-EFFECT
roughly:I-EFFECT
$:I-EFFECT
11.5:I-EFFECT
million:I-EFFECT
,:I-EFFECT
will:I-EFFECT
be:I-EFFECT
refunded:I-EFFECT
by:I-EFFECT
two:I-EFFECT
insurers:I-EFFECT
to:I-EFFECT
more:I-EFFECT
than:I-EFFECT
500:I-EFFECT
large:I-EFFECT
Texas:I-EFFECT
employers:I-EFFECT
who:I-EFFECT
bought:I-EFFECT
plans:I-EFFECT
for:I-EFFECT
their:I-EFFECT
workers:I-EFFECT
last:I-EFFECT
year:I-EFFECT
,:I-EFFECT
the:I-EFFECT
data:I-EFFECT
showed.:I-EFFECT"""
NUM_TOKENS = 109

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
