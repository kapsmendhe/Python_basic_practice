from cProfile import Profile
from functools import wraps
import time
"""
add decorator @profile to any method it will calculate the time taken by that method
"""


def profile(function):
    """."""
    @wraps(function)
    def wrapper(*args, **kwargs):
        """."""
        cp = Profile()
        try:
            cp.enable()
            result = function(*args, **kwargs)
            cp.disable()
            return result
        finally:
            filename = "profile_method_name" + time.strftime('%m-%d-%Y-%H-%M-%S')
            cp.dump_stats(filename + ".dump")

    return wrapper
