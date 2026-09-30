import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("sky pro", " ", True),
    ("abc", "", True),
    ("", "1", False),
  ])
def test_capitalize_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected