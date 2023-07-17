from um import count

def main():
    test_valid()


def test_valid():
    assert count("um?") == 1
    assert count("yummy") == 0
    assert count("   um   ") == 1
    assert count("Um") == 1




if __name__ == "__main__":
    main()