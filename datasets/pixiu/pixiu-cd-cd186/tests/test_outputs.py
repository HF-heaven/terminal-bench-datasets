import json
from pathlib import Path

PIXIU_ID = "cd186"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """Openwork:B-EFFECT
By:I-EFFECT
Rachel:I-EFFECT
Mortimer:I-EFFECT
Openwork:I-EFFECT
gained:I-EFFECT
262:I-EFFECT
advisers:I-EFFECT
last:I-EFFECT
year:I-EFFECT
as:O
the:B-CAUSE
advice:I-CAUSE
network:I-CAUSE
continued:I-CAUSE
its:I-CAUSE
recruitment:I-CAUSE
drive:I-CAUSE
and:I-CAUSE
focus:I-CAUSE
on:I-CAUSE
the:I-CAUSE
company:I-CAUSE
's:I-CAUSE
academy:I-CAUSE
programme.:I-CAUSE"""
NUM_TOKENS = 26

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
