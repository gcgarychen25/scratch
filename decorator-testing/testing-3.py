#timing decorator
import time
import logging

logging.basicConfig(level=logging.INFO)

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"'{func.__name__}' took {end_time - start_time} seconds to run")
        return result
    return wrapper

@timing_decorator
def long_running_function():
    time.sleep(2)

long_running_function()
