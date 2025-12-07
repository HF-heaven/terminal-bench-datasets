import json
from pathlib import Path

PIXIU_ID = "finerord508"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """In:O
accordance:O
with:O
General:O
Instruction:O
B.2:O
of:O
Form:O
8:O
-:O
K:O
,:O
the:O
information:O
in:O
this:O
Current:O
Report:O
on:O
Form:O
8:O
-:O
K:O
,:O
including:O
Exhibit:O
99.1:O
,:O
shall:O
not:O
be:O
deemed:O
to:O
be:O
":O
filed:O
":O
for:O
purposes:O
of:O
Section:O
18:O
of:O
the:O
Securities:O
and:O
Exchange:O
Act:O
of:O
1934:O
,:O
as:O
amended:O
(:O
the:O
":O
Exchange:O
Act:O
":O
):O
,:O
or:O
otherwise:O
subject:O
to:O
the:O
liability:O
of:O
that:O
section:O
,:O
and:O
shall:O
not:O
be:O
incorporated:O
by:O
reference:O
into:O
any:O
registration:O
statement:O
or:O
other:O
document:O
filed:O
under:O
the:O
Securities:O
Act:O
of:O
1933:O
,:O
as:O
amended:O
,:O
or:O
the:O
Exchange:O
Act:O
,:O
except:O
as:O
shall:O
be:O
expressly:O
set:O
forth:O
by:O
specific:O
reference:O
in:O
such:O
filing:O
.:O"""
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
