from src.fib import fib

def test_first_fibonacci_number():
    assert fib(0) == 0

def test_second_fibonacci_number():
    assert fib(1) == 1

def test_fifth_fibonacci_number():
    assert fib(4) == 3