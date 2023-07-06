# caching/memoization decorator
import time

# A simple recursive implementation without caching.
def fibonacci_no_cache(n):
    if n in {0, 1}:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

# A caching decorator.
def memoize_decorator(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

# A recursive implementation with caching.
@memoize_decorator
def fibonacci_with_cache(n):
    if n in {0, 1}:
        return n
    return fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)

# Let's test for n=35
n = 35

# Without caching
start_time = time.time()
fibonacci_no_cache(n)
end_time = time.time()
print(f"Fibonacci without cache took {end_time - start_time} seconds")

# With caching
start_time = time.time()
fibonacci_with_cache(n)
end_time = time.time()
print(f"Fibonacci with cache took {end_time - start_time} seconds")
