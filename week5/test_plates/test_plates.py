from plates import is_valid

def test_begin_with_two_letters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("C") == False


def test_length():
    assert is_valid("PIV314") == True
    assert is_valid("HEY") == True
    assert is_valid("OUTATIME") == False


def test_num():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS05T") == False
    assert is_valid("CSE005") == False


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("HEY!") == False
