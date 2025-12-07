import json
from pathlib import Path

PIXIU_ID = "finerord923"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """Getty:O
Images:O
by:O
Jocelyn:B-PER
McClurg:I-PER
Jean:B-PER
Louise:I-PER
Finch:I-PER
-:O
better:O
known:O
to:O
millions:O
of:O
To:O
Kill:O
a:O
Mockingbird:O
fans:O
as:O
Scout:O
-:O
is:O
all:O
grown:O
up:O
and:O
on:O
a:O
train:O
from:O
New:B-LOC
York:I-LOC
City:I-LOC
,:O
headed:O
home:O
to:O
Maycomb:B-LOC
,:O
as:O
Go:O
Set:O
a:O
Watchman:O
opens:O
.:O"""
NUM_TOKENS = 47

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
