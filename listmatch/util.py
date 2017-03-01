from itertools import tee


def pairwise(iterable):
    """
    [a, b, c] -> [(a, b), (b, c)]
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def make_fluent_func(cls):
    def func(*args, **kwargs):
        return cls(*args, **kwargs)
    return func
