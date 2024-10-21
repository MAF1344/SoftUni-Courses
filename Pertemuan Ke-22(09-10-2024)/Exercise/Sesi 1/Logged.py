def logged(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_message = f"you called {func.__name__}{args}\nit returned {result}"
        return log_message  # Return the formatted log message instead of printing it
    return wrapper

@logged
def func(*args):
    return 3 + len(args)

@logged
def sum_func(a, b):
    return a + b

# test zero
import unittest

class LoggedTests(unittest.TestCase):
    def test_zero(self):
        @logged
        def func(*args):
            return 3 + len(args)
        result = func(4, 4, 4)
        self.assertEqual(result, 'you called func(4, 4, 4)\nit returned 6')

if __name__ == '__main__':
    unittest.main()