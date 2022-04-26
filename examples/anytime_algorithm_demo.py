""" 
Demonstrates using an anytime algorithm.

Author: Erel Segal-Halevi
Since:  2022-03
"""

import prtpy
import numpy as np
from time import perf_counter

rng = np.random.default_rng()

start = perf_counter()
numbins = 100
numitems = numbins * 4  # recommendation from here https://or.stackexchange.com/q/8122/2576 
values = rng.normal(500,200, numitems//2) + rng.normal(1000,200, numitems//2) 
print("Greedy: ", prtpy.partition(algorithm=prtpy.partitioning.greedy, numbins=numbins, items=values, outputtype=prtpy.out.ExtremeSums))
print(f"\t {perf_counter()-start} seconds")
start = perf_counter()
print("Complete greedy: ")
for time_in_seconds in [0.25,0.5,1,2,4,8,16]:
    start = perf_counter()
    print(f"\t{time_in_seconds}: ", prtpy.partition(algorithm=prtpy.partitioning.complete_greedy, numbins=numbins, items=values, outputtype=prtpy.out.ExtremeSums, time_in_seconds=time_in_seconds))
    print(f"\t {perf_counter()-start} seconds")
