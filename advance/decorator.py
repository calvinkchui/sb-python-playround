import time

# Refer: https://blog.stackademic.com/20-python-concepts-i-wish-i-knew-way-earlier-40ed5674cd52
# Pitfalls: Overusing decorators or stacking many of them can make code harder to understand.


def timer_decorator(func):

  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"{func.__name__} executed in {end_time - start_time} seconds")
    return result

  return wrapper


@timer_decorator
def sample_function():
  time.sleep(2)


def demo():
  sample_function()  # sample_function executed in 2.0020077228546143 seconds
