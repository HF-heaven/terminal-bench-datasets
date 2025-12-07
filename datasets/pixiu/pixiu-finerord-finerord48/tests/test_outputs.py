import json
from pathlib import Path

PIXIU_ID = "finerord48"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """Being:O
forced:O
to:O
live:O
in:O
the:O
moment:O
is:O
different:O
to:O
evangelically:O
boring:O
on:O
about:O
it:O
;:O
but:O
if:O
there:O
’s:O
one:O
thing:O
worse:O
than:O
someone:O
you:O
ca:O
n’t:O
get:O
hold:O
of:O
,:O
it:O
’s:O
the:O
person:O
unable:O
to:O
“:O
go:O
dark:O
”:O
without:O
bleating:O
“:O
do:O
you:O
know:O
where:O
I:O
can:O
charge:O
my:O
phone:O
?:O
”:O
to:O
every:O
other:O
person:O
.:O"""
NUM_TOKENS = 61

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
