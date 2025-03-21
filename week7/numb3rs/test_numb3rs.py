from numb3rs import validate


def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("cat") == False
    assert validate("275.3.6.28") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.f.2.ab") == False
    assert validate("127.1.1.259") == False
    assert validate("198.162.1.1") == True
