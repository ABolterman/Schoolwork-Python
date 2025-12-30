import matplotlib.pyplot as plt

import time


#Given example
def compute_time_to_add(list_to_add_to, item):
    start = time.perf_counter()
    list_to_add_to.append(item)
    end = time.perf_counter()
    return end-start


timings = []
some_list = []
values = range(10_000_000)
for n in values:
    timings.append(compute_time_to_add(some_list, n))

plt.plot(values, timings)
plt.show()


# Removing from list

timings = []
some_list = []
values = list(range(10_000))
for n in range(10_000):
    start = time.perf_counter()
    del values[0]
    end = time.perf_counter()
    timings.append(end-start)
values = list(range(10_000, 0, -1))
plt.plot(values, timings)
plt.show()

timings = []
some_list = []
values = list(range(10_000))
for n in range(50, 10_000):
    start = time.perf_counter()
    del values[50]
    end = time.perf_counter()
    timings.append(end-start)
values = list(range(10_000, 50, -1))
plt.plot(values, timings)
plt.show()

# Insert item
timings = []
some_list = []

for n in range(100_000):
    start = time.perf_counter()
    some_list.insert(0, n)
    end = time.perf_counter()
    timings.append(end-start)
values = list(range(100_000))
plt.plot(values, timings)
plt.show()


