import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("50/100") == 50
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

def test_value_error():
    with pytest.raises(ValueError):
        convert("a/b")
        convert("2/1")


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
