def cache(func):
    log = {}  # Create a log dictionary to store results

    def wrapper(n):
        if n not in log:  # Only calculate if not cached
            log[n] = func(n)  # Store the result in the log
        return log[n]

    wrapper.log = log  # Attach log to the wrapper function
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# test first zero
import unittest


class CacheTests(unittest.TestCase):
    def test_zero_first(self):
        @cache
        def fibonacci(n):
            if n < 2:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        fibonacci(3)
        self.assertEqual(fibonacci.log, {1: 1, 0: 0, 2: 1, 3: 2})


if __name__ == '__main__':
    unittest.main()
