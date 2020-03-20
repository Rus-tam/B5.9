# -*- coding: utf-8 -*-
import time

def time_this(num_runs=10):
    def func1(empty_function):
        def func2(*args, **kwargs):
            average = 0
            for i in range(0, num_runs):
                s_t = time.time()
                empty_function(*args, **kwargs)
                f_t = time.time()
                average = average + (f_t - s_t)
            average = average/num_runs
            print(average)
        return func2()
    return func1

@time_this(num_runs=100)
def f():
    for j in range(1000000):
        pass