from fib import fib


def test_fib(benchmark):
    result = benchmark(fib, 30)
    assert result == 1346269



# Commands to perform tests with pytest-benchmark: 
# pytest --benchmark-autosave
# pytest --benchmark-autosave --benchmark-compare

