import json
from pathlib import Path

PIXIU_ID = "cd39"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """With:B-EFFECT
more:I-EFFECT
than:I-EFFECT
275:I-EFFECT
members:I-EFFECT
,:I-EFFECT
covering:I-EFFECT
the:I-EFFECT
whole:I-EFFECT
spectrum:I-EFFECT
of:I-EFFECT
the:I-EFFECT
listed:I-EFFECT
real:I-EFFECT
estate:I-EFFECT
industry:I-EFFECT
(:I-EFFECT
companies:I-EFFECT
,:I-EFFECT
investors:I-EFFECT
and:I-EFFECT
their:I-EFFECT
suppliers:I-EFFECT
):I-EFFECT
,:I-EFFECT
EPRA:I-EFFECT
represents:I-EFFECT
over:I-EFFECT
EUR:I-EFFECT
450:I-EFFECT
billion:I-EFFECT
of:I-EFFECT
real:I-EFFECT
estate:I-EFFECT
assetsand:I-EFFECT
94:I-EFFECT
%:I-EFFECT
of:I-EFFECT
the:I-EFFECT
market:I-EFFECT
capitalisation:I-EFFECT
of:I-EFFECT
the:I-EFFECT
FTSE:I-EFFECT
EPRA:I-EFFECT
Nareit:I-EFFECT
Europe:I-EFFECT
Index.:I-EFFECT
EPRA:O
's:O
mission:O
is:O
to:O
promote:O
,:O
develop:O
and:O
represent:O
the:O
European:O
public:O
real:O
estate:O
sector:O
.:O
We:B-CAUSE
achieve:I-CAUSE
this:I-CAUSE
through:I-CAUSE
the:I-CAUSE
provision:I-CAUSE
of:I-CAUSE
better:I-CAUSE
information:I-CAUSE
to:I-CAUSE
investors:I-CAUSE
and:I-CAUSE
stakeholders:I-CAUSE
,:I-CAUSE
active:I-CAUSE
involvement:I-CAUSE
in:I-CAUSE
the:I-CAUSE
public:I-CAUSE
and:I-CAUSE
political:I-CAUSE
debate:I-CAUSE
,:I-CAUSE
promotion:I-CAUSE
of:I-CAUSE
best:I-CAUSE
practices:I-CAUSE
and:I-CAUSE
the:I-CAUSE
cohesion:I-CAUSE
and:I-CAUSE
strengthening:I-CAUSE
of:I-CAUSE
the:I-CAUSE
industry.:I-CAUSE"""
NUM_TOKENS = 100

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
