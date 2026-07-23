def add(a, b):
    return a + b


def run_tests():
    print("Running tests...")

    assert add(2, 3) == 5
    assert add(10, 20) == 30
    assert add(-5, 5) == 0

    print("✅ All tests passed!")


if __name__ == "__main__":
    run_tests()