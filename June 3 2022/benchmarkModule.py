import time

def benchmark(func):

    def inner(*args, **kwargs):

        start = time.time()
        value = func(*args, **kwargs)
        end  = time.time()
        runtime = end - start
        print(f"The {func.__name__} took {runtime} seconds to complete the function")

        return value

    return inner