import json
from pathlib import Path

PIXIU_ID = "finerord190"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """Wed:O
,:O
Jul:O
1:O
,:O
2015:O
,:O
14:29:O
BST:O
-:O
UK:B-LOC
Markets:O
close:O
in:O
2:O
hrs:O
1:O
mins:O
Permanent:O
tsb:O
becomes:O
latest:O
Irish:O
lender:O
to:O
cut:O
mortgage:O
rates:O
Reuters:B-ORG
-:O
UK:B-LOC
Focus:O
–:O
6:O
hours:O
ago:O
4.73:O
+0.380:O
DUBLIN:B-LOC
,:O
July:O
1:O
(:O
Reuters:B-ORG
):O
-:O
Ireland:B-LOC
(:O
Other:O
OTC:O
::O
IRLD:B-ORG
-:O
news:O
):O
's:O
Permanent:O
tsb:O
(:O
Berlin:O
::O"""
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
