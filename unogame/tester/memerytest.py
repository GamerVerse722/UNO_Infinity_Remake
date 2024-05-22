from unogame.tester.helper.utils import *
import gc


data: dict = {}


starting_memory: float = memory_usage()

for _ in range(50000):
    data[name_gen(20)] = name_gen(20)
max_memory: float = memory_usage()

data.clear()
gc.collect()
end_memory: float = memory_usage()

print(f"Start Memory usage: {starting_memory:.3f} MB")
print(f"Max Memory usage: {max_memory:.3f} MB")
print(f"End Memory usage: {end_memory:.3f} MB")