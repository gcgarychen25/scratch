# testing logging decorators 

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
def add(x=0, y=0):
    return x + y
add(3, 4)
add(3, y=4)
add(x=3, y=4)
'''
# in addition to the logging ingo, the print command will return the results of the function again
print(add(3, 4))
print()
print()
'''