from working import convert
import pytest

def main():
    test_valid()
    test_notvalid()


def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_notvalid():
    with pytest.raises(ValueError):
        convert('9 AM - 17 PM')
    with pytest.raises(ValueError):
        convert('17:00 AM to 23:00 PM' )



if __name__ == "__main__":
    main()