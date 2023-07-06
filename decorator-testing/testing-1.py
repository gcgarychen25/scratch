# logging decorator
import logging

logging.basicConfig(level=logging.INFO)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Running '{func.__name__}' with arguments {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"'{func.__name__}' returned {result}")
        return result
    return wrapper

@log_decorator
def add(x, y):
    return x + y

print(add(3, 4))
