import json
from pathlib import Path

PIXIU_ID = "finerord602"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """The:O
dramatic:O
shift:O
in:O
spending:O
patterns:O
,:O
campaign:O
finance:O
lawyers:O
say:O
,:O
is:O
the:O
starkest:O
sign:O
yet:O
of:O
a:O
new:O
order:O
in:O
money:O
in:O
politics:O
,:O
one:O
no:O
longer:O
dominated:O
by:O
small:O
-:O
dollar:O
bundlers:O
beholden:O
to:O
federal:O
campaign:O
finance:O
regulations:O
but:O
rather:O
by:O
a:O
new:O
,:O
anything:O
-:O
goes:O
era:O
featuring:O
largely:O
unregulated:O
Super:O
PACs:O
and:O
the:O
billionaires:O
,:O
looking:O
to:O
influence:O
U.S:B-LOC
.:I-LOC
policy:O
,:O
who:O
fund:O
them:O
.:O"""
NUM_TOKENS = 71

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
