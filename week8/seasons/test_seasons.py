import pytest
from seasons import convert, count_days


def test_count_days():
    assert count_days("2023-08-13") == 366
    assert count_days("1998-05-24") == 9578
    assert count_days("2001-01-01") == 8625
    assert count_days("2020-06-01") == 1534


def test_convert():
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(
        9578) == "Thirteen million, seven hundred ninety-two thousand, three hundred twenty minutes"
    assert convert(8625) == "Twelve million, four hundred twenty thousand minutes"
    assert convert(1534) == "Two million, two hundred eight thousand, nine hundred sixty minutes"


def test_invalid_date():
    with pytest.raises(SystemExit) as sample:
        count_days("February 6th, 1998")
    assert sample.type == SystemExit
    assert sample.value.code == "Invalid Date"
