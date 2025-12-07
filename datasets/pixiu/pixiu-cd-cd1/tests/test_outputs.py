import json
from pathlib import Path

PIXIU_ID = "cd1"
LABEL_TYPE = "causal detection (sequence labeling)"
EXPECTED_ANSWER = """REUTERS/Aly:O
Song/File:O
Photo:O
(:O
Reuters:O
):O
-:O
Tencent:B-CAUSE
Holdings:I-CAUSE
Ltd:I-CAUSE
and:I-CAUSE
private:I-CAUSE
equity:I-CAUSE
partner:I-CAUSE
Hammer:I-CAUSE
Capital:I-CAUSE
have:I-CAUSE
offered:I-CAUSE
$:I-CAUSE
16:I-CAUSE
per:I-CAUSE
share:I-CAUSE
to:I-CAUSE
buy:I-CAUSE
out:I-CAUSE
the:I-CAUSE
other:I-CAUSE
shareholders:I-CAUSE
in:I-CAUSE
Chinese:I-CAUSE
car:I-CAUSE
comparison:I-CAUSE
website:I-CAUSE
Bitauto:I-CAUSE
Holdings:I-CAUSE
Ltd:I-CAUSE
,:O
valuing:B-EFFECT
the:I-EFFECT
company:I-EFFECT
at:I-EFFECT
just:I-EFFECT
under:I-EFFECT
$:I-EFFECT
1.2:I-EFFECT
billion.:I-EFFECT"""
NUM_TOKENS = 46

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
