import json
from pathlib import Path

PIXIU_ID = "finerord524"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """Key:O
Topics:O
Covered:O
::O
2:O
Introduction:O
to:O
Bahrain:B-LOC
Upstream:O
Oil:O
and:O
Gas:O
Markets:O
3:O
Importance:O
of:O
Bahrain:O
Upstream:O
Market:O
in:O
Region:O
and:O
Global:O
Front:O
4:O
Key:O
Trends:O
,:O
Market:O
Drivers:O
and:O
Challenges:O
Facing:O
Companies:O
in:O
Bahrain:B-LOC
Upstream:O
Sector:O
5:O
Bahrain:B-LOC
oil:O
and:O
gas:O
production:O
and:O
consumption:O
forecasts:O
to:O
2025:O
6:O
Bahrain:B-LOC
Oil:O
and:O
gas:O
Field:O
Details:O
7:O
Bahrain:B-LOC
Field:O
wise:O
Oil:O
and:O
Gas:O
Production:O
,:O
2005:O
-:O
2012:O
8:O
Bahrain:B-LOC
Exploration:O
Sector:O
Analysis:O
9:O
Bahrain:B-LOC
Exploration:O
and:O
Production:O
Market:O
Competitive:O
Landscape:O
10:O
Company:O
Oil:O
and:O
Gas:O
Operations:O
13:O
Latest:O
Development:O
and:O
their:O
Impact:O
on:O
Bahrain:B-LOC
Exploration:O
and:O
Production:O
Market:O
14:O
Appendix:O"""
NUM_TOKENS = 101

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
