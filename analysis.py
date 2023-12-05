import os
import sys
import time
import tracemalloc

from branch_and_bound import branch_and_bound
from greedy import greedy
from read_store_file import read_from_txt


def main():
    dataset_path = 'dataset'
    for filename in os.listdir(dataset_path):
        full_path = os.path.join(dataset_path, filename)
        data = read_from_txt(full_path)

        print(f'Greedy           {filename: <13}', end=' ')
        tracemalloc.start()
        start_time = time.time()
        output = greedy(data[0], data[1], data[2])
        memory_usage = tracemalloc.get_traced_memory()
        end_time = time.time()
        tracemalloc.stop()
        print(f'cost = {output[1]: <10}', end=' ')
        print(f'memory = {memory_usage.__str__():<10}', end=' ')
        print(f'{(end_time - start_time) * 1000: <10} ms')

        print(f'Branch and Bound {filename: <10}', end=' ')
        tracemalloc.start()
        start_time = time.time()
        output = branch_and_bound(data[0], data[1], data[2])
        memory_usage = tracemalloc.get_traced_memory()
        end_time = time.time()
        tracemalloc.stop()
        print(f'cost = {output[1]: <10}', end=' ')
        print(f'memory = {memory_usage.__str__():<10}', end=' ')
        print(f'{(end_time - start_time) * 1000: <10} ms')

        print()


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    main()
