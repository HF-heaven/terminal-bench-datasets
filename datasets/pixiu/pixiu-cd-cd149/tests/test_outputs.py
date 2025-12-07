import json
from pathlib import Path

PIXIU_ID = "cd149"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """by:O
Tyler:O
Durden:O
Sat:O
,:O
09/14/2019:O
-:O
07:35:O
0:O
SHARES:O
A:O
new:O
study:O
published:O
by:O
the:O
International:O
Monetary:O
Fund:O
has:O
found:O
that:O
$:O
15:O
trillion:O
of:O
the:O
world:O
's:O
foreign:O
direct:O
investments:O
are:O
phantom:O
capital:O
-:O
a:O
term:O
used:O
to:O
describe:O
capital:O
that:O
is:O
designed:O
to:O
minimize:O
tax:O
bills:O
of:O
multinational:O
firms:O
.:O
This:B-EFFECT
total:I-EFFECT
makes:I-EFFECT
up:I-EFFECT
40:I-EFFECT
%:I-EFFECT
of:I-EFFECT
the:I-EFFECT
world:I-EFFECT
's:I-EFFECT
foreign:I-EFFECT
direct:I-EFFECT
investments:I-EFFECT
,:I-EFFECT
and:I-EFFECT
is:I-EFFECT
the:I-EFFECT
equivalent:I-EFFECT
to:I-EFFECT
the:I-EFFECT
combined:I-EFFECT
GDP:I-EFFECT
of:I-EFFECT
China:I-EFFECT
and:I-EFFECT
Germany:I-EFFECT
,:I-EFFECT
according:I-EFFECT
to:I-EFFECT
Bloomberg.:I-EFFECT
These:I-CAUSE
types:I-CAUSE
of:I-CAUSE
investments:I-CAUSE
have:I-CAUSE
risen:I-CAUSE
about:I-CAUSE
10:I-CAUSE
%:I-CAUSE
over:I-CAUSE
the:I-CAUSE
past:I-CAUSE
decade:I-CAUSE
despite:I-CAUSE
global:I-CAUSE
efforts:I-CAUSE
to:I-CAUSE
curb:I-CAUSE
tax:I-CAUSE
avoidance:I-CAUSE
,:I-CAUSE
according:I-CAUSE
to:I-CAUSE
the:I-CAUSE
IMF:I-CAUSE
study.:I-CAUSE"""
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
