import time
import sys
import numpy as np
from multiprocessing import Pool
from functools import partial
from bubble import bubble_sort
from introSort import introsort
from heapSort import heap_sort
from quickSort import quickSort
from timSort import TimSort
from selectionSort import selectionSort
from insertionSort import insertion_sort
from mergeSort import mergeSort
from basis import Hybrid_sort_700_run

# Input datasets
inputList = [
    'Half_Sorted/half_sorted_1000.txt', 'Half_Sorted/half_sorted_5000.txt',
    'Half_Sorted/half_sorted_10000.txt', 'Half_Sorted/half_sorted_50000.txt',
    'Half_Sorted/half_sorted_100000.txt',
    'Random/random_numbers_1000.txt', 'Random/random_numbers_5000.txt',
    'Random/random_numbers_10000.txt', 'Random/random_numbers_50000.txt',
    'Random/random_numbers_100000.txt',
    'Reversed__New/reverse_1000.txt', 'Reversed__New/reverse_5000.txt',
    'Reversed__New/reverse_10000.txt', 'Reversed__New/reverse_50000.txt',
    'Reversed__New/reverse_100000.txt',
    'Sorted_New/Sorted_1000.txt', 'Sorted_New/Sorted_5000.txt',
    'Sorted_New/Sorted_10000.txt', 'Sorted_New/Sorted_50000.txt',
    'Sorted_New/Sorted_100000.txt',
    '10mills_datasets_gitignored/half_sorted_5m.txt',
    '10mills_datasets_gitignored/random_numbers_5m.txt',
    '10mills_datasets_gitignored/reverse_5m-float.txt'
]
# '10mills_datasets_gitignored/Sorted_5m.txt'

sortingAlgos = [Hybrid_sort_700_run, TimSort, introsort, mergeSort, bubble_sort]

# Set recursion limit for quickSort
sys.setrecursionlimit(1000000000)

def run_iteration(algo, inputarray, iteration):
    """Run a single iteration of the sorting algorithm."""
    arr = inputarray.copy()
    if algo is quickSort:
        start = time.perf_counter()
        quickSort(arr, 0, len(arr) - 1)
        end = time.perf_counter()
    elif algo is heap_sort:
        start = time.perf_counter()
        heap_sort(arr)
        end = time.perf_counter()
    elif algo is introsort:
        start = time.perf_counter()
        introsort(arr)
        end = time.perf_counter()
    elif algo is bubble_sort:
        start = time.perf_counter()
        bubble_sort(arr)
        end = time.perf_counter()
    elif algo is TimSort:
        start = time.perf_counter()
        TimSort(arr)
        end = time.perf_counter()
    elif algo is selectionSort:
        start = time.perf_counter()
        selectionSort(arr, len(arr))
        end = time.perf_counter()
    elif algo is insertion_sort:
        start = time.perf_counter()
        insertion_sort(arr)
        end = time.perf_counter()
    elif algo is mergeSort:
        start = time.perf_counter()
        mergeSort(arr, 0, len(arr) - 1)
        end = time.perf_counter()
    elif algo is Hybrid_sort_700_run:
        start = time.perf_counter()
        Hybrid_sort_700_run(arr)
        end = time.perf_counter()
    else:
        return 0.0
    return end - start

def process_dataset(algo, path, num_iterations=99):

    print(f"Processing {algo.__name__} on {path}")

    # try:
    #     print(f"path: {path.split('/')[1]}")
    # except IndexError:
    #     print(f"Error: Path {path} does not have enough segments")

    with open(path, 'r') as fin:
        lines = fin.readlines()

    inputarray = [line for line in lines]

    # Parallelize iterations    
    with Pool(processes=32) as pool:
        iteration_times = pool.map(
            partial(run_iteration, algo, inputarray),
            range(num_iterations)
        )

    # Compute statistics
    _std = np.std(iteration_times)
    _median = np.median(iteration_times)
    _mean = np.mean(iteration_times)
    _max = np.max(iteration_times)
    _min = np.min(iteration_times)

    print("""Execution time summary:
    {:^12} {:^12} {:^12} {:^12} {:^12}
    {:^12.4f} {:^12.4f} {:^12.4f} {:^12.4f} {:^12.4f}
    """.format(
        "mean (ms)", "median (ms)", "max (ms)", "min (ms)", "std (ms)",
        _mean * 1000, _median * 1000, _max * 1000, _min * 1000, _std * 1000
    ))

if __name__ == "__main__":
    for algo in sortingAlgos:
        print("--------------------------------------------")
        print(f"{algo.__name__} times: ")
        for path in inputList:
            process_dataset(algo, path)