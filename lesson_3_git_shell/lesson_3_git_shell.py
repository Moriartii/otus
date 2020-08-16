#!/usr/bin/python3

'''
def expone(*args, exponenta=1):
    after_exp = []
    for x in args:
        x = x**exponenta
        after_exp.append(x)
    return after_exp, exponenta
'''


def timing_decorator(func):
    import time       
    def wrapper(*args, **kwargs):
        start_time = time.time()
        return_value = func(*args, **kwargs)
        stop_time = time.time()
        time_diff = stop_time - start_time
        print(f'Время выполнения: {time_diff} секунд.')
        return return_value
    return wrapper


@timing_decorator
def expone(*args, exponenta=1):
    after_exp = []
    for x in args:
        x = x**exponenta
        after_exp.append(x)
    return after_exp, exponenta


expone(1,2,3,4,5, exponenta=3)
