import prtpy, benchmark, logging
from matplotlib import pyplot as plt
from partition_random import partition_random_items

algorithm = prtpy.partitioning.ilp
numbins = 4

benchmark.logger.setLevel(logging.INFO)
benchmark.logger.addHandler(logging.StreamHandler())


results = benchmark.find_max_solvable_size(
    partition_random_items,
    "numitems",
    range(1, 101, 10),
    max_time_in_seconds=10,
    algorithm=algorithm,
    numbins=numbins,
    minvalue=1,
    maxvalue=100,
    objective=prtpy.obj.MaximizeSmallestSum,
    outputtype=prtpy.out.SmallestSum,
)

results.plot(plt)
