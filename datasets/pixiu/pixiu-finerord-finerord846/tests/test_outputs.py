import json
from pathlib import Path

PIXIU_ID = "finerord846"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """Opposition:O
Leader:O
Bill:B-PER
Shorten:I-PER
has:O
played:O
up:O
the:O
risk:O
to:O
jobs:O
from:O
the:O
China:B-LOC
FTA:O
even:O
though:O
his:O
stance:O
appears:O
at:O
odds:O
with:O
several:O
Labor:O
leaders:O
including:O
Victorian:O
Premier:O
Daniel:B-PER
Andrews:I-PER
and:O
South:O
Australian:O
Premier:O
Jay:B-PER
Weatherill:I-PER
,:O
who:O
back:O
the:O
deal:O
.:O"""
NUM_TOKENS = 43

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
