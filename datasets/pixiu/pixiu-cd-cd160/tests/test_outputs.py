import json
from pathlib import Path

PIXIU_ID = "cd160"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """Therefore:B-CAUSE
,:I-CAUSE
the:I-CAUSE
maximum:I-CAUSE
cantonal:I-CAUSE
tax:I-CAUSE
relief:I-CAUSE
is:I-CAUSE
set:I-CAUSE
at:I-CAUSE
70:I-CAUSE
%:I-CAUSE
.:I-CAUSE
The:I-CAUSE
capital:I-CAUSE
tax:I-CAUSE
on:I-CAUSE
equity:I-CAUSE
relating:I-CAUSE
to:I-CAUSE
investments:I-CAUSE
,:I-CAUSE
patents:I-CAUSE
,:I-CAUSE
and:I-CAUSE
similar:I-CAUSE
intangibles:I-CAUSE
as:I-CAUSE
well:I-CAUSE
as:I-CAUSE
intercompany:I-CAUSE
loans:I-CAUSE
will:I-CAUSE
also:I-CAUSE
be:I-CAUSE
reduced:I-CAUSE
under:I-CAUSE
the:I-CAUSE
Canton:I-CAUSE
Zurich:I-CAUSE
tax:I-CAUSE
reform.:I-CAUSE
Consequently:I-EFFECT
,:I-EFFECT
taxable:I-EFFECT
equity:I-EFFECT
attributable:I-EFFECT
to:I-EFFECT
qualifying:I-EFFECT
investments:I-EFFECT
,:I-EFFECT
loans:I-EFFECT
to:I-EFFECT
group:I-EFFECT
companies:I-EFFECT
,:I-EFFECT
and:I-EFFECT
qualifying:I-EFFECT
intellectual:I-EFFECT
property:I-EFFECT
will:I-EFFECT
be:I-EFFECT
reduced:I-EFFECT
by:I-EFFECT
90:I-EFFECT
%:I-EFFECT
.:I-EFFECT
Researcher:I-EFFECT
and:I-EFFECT
lecturer:I-EFFECT
at:I-EFFECT
University:I-EFFECT
of:I-EFFECT
Lausanne:I-EFFECT
Davide:I-EFFECT
Anghileri:I-EFFECT
is:I-EFFECT
a:I-EFFECT
PhD:I-EFFECT
candidate:I-EFFECT
at:I-EFFECT
the:I-EFFECT
University:I-EFFECT
of:I-EFFECT
Lausanne:I-EFFECT
,:I-EFFECT
where:I-EFFECT
he:I-EFFECT
is:I-EFFECT
writing:I-EFFECT
his:I-EFFECT
thesis:I-EFFECT
on:I-EFFECT
the:I-EFFECT
attribution:I-EFFECT
of:I-EFFECT
profits:I-EFFECT
to:I-EFFECT
PEs.:I-EFFECT"""
NUM_TOKENS = 99

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
