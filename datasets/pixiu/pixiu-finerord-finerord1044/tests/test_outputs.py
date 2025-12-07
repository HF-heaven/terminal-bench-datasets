import json
from pathlib import Path

PIXIU_ID = "finerord1044"
LABEL_TYPE = "named entity recognition (NER)"
EXPECTED_ANSWER = """“:O
The:O
September:O
presentations:O
are:O
scheduled:O
as:O
follows:O
::O
When:O
::O
11:30:O
AM:O
–:O
1:00:O
PM:O
Tuesday:O
,:O
September:O
29th:O
,:O
2015:O
Where:O
::O
Green:B-LOC
Hills:I-LOC
Country:I-LOC
Club:I-LOC
500:B-LOC
Ludeman:I-LOC
Lane:I-LOC
,:I-LOC
Millbrae:I-LOC
,:I-LOC
CA:I-LOC
94030:I-LOC
Complimentary:O
Lunch:O
Provided:O
When:O
::O
11:30:O
AM:O
–:O
1:00:O
PM:O
Wednesday:O
,:O
September:O
30th:O
,:O
2015:O
Where:O
::O
1101:B-LOC
Fifth:I-LOC
Avenue:I-LOC
,:I-LOC
Suite:I-LOC
310:I-LOC
–:I-LOC
San:I-LOC
Rafael:I-LOC
,:I-LOC
CA:I-LOC
94901:I-LOC
Complimentary:O
Lunch:O
Provided:O
To:O
RSVP:O
please:O
call:O
Kelley:B-PER
at:O
925-219-0080:O
,:O
or:O
RSVP:O
at:O
info(:O
at):O
donormotivationnorcal:O
(:O
dot:O
):O
com:O
About:O
Yerba:B-ORG
Buena:I-ORG
Wealth:I-ORG
Advisors:I-ORG
,:I-ORG
LLC:I-ORG
Based:O
in:O
San:B-LOC
Rafael:I-LOC
,:I-LOC
CA:I-LOC
Yerba:B-ORG
Buena:I-ORG
Wealth:I-ORG
Advisors:I-ORG
,:I-ORG
LLC:I-ORG
consultancy:O
firm:O
specializes:O
in:O
helping:O
their:O
non-profit:O
clients:O
,:O
their:O
donors:O
,:O
entrepreneurs:O
,:O
and:O
accredited:O
investors:O
make:O
an:O
even:O
greater:O
impact:O
on:O
the:O
people:O
and:O
causes:O
they:O
care:O
about:O
deeply:O
.:O"""
NUM_TOKENS = 138

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
