import time 
import sys
import numpy as np
import csv
import os
from bubble import bubble_sort
from introSort import introSort
from heapSort import heap_sort
from quickSort import quickSort
from timSort import TimSort
from selectionSort import selectionSort
from insertionSort import insertion_sort
from mergeSort import mergeSort
from hpc_project import tim_run_detect_sorted
from hpc_project import Hybrid_sort_700_run_sorted

sys.setrecursionlimit(1000000000)

def is_sorted(arr):
    print(arr)
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

inputList = [
    # 'Half_Sorted/half_sorted_1000.txt',
    # 'Half_Sorted/half_sorted_5000.txt',
    # 'Half_Sorted/half_sorted_10000.txt',
    # 'Half_Sorted/half_sorted_50000.txt',
    'Random/random_numbers_1000.txt',
    'Random/random_numbers_5000.txt',
    'Random/random_numbers_10000.txt',
    'Random/random_numbers_50000.txt',
    'Reversed_New/reverse_1000.txt',
    'Reversed_New/reverse_5000.txt',
    'Reversed_New/reverse_10000.txt',
    'Reversed_New/reverse_50000.txt',
    'Sorted_New/Sorted_1000.txt',
    'Sorted_New/Sorted_5000.txt',
    'Sorted_New/Sorted_10000.txt',
    'Sorted_New/Sorted_50000.txt',
    'Sorted_New/Sorted_100000.txt',
    'Random/random_numbers_100000.txt',
    'Reversed_New/reverse_100000.txt',
    'Half_Sorted/half_sorted_100000.txt'
]

# sortingAlgos = [Hybrid_sort_700_run_sorted,tim_run_detect_sorted,mergeSort,introsort, bubble_sort]
sortingAlgos = [bubble_sort]

output_csv = 'sorting_results_bubble_2.csv'
os.makedirs("sorted_outputs", exist_ok=True)

if os.path.exists(output_csv):
    os.remove(output_csv)

with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Algorithm", "Dataset", "Mean(ms)", "Median(ms)", "Max(ms)", "Min(ms)", "Std(ms)"])

for algo in sortingAlgos:
    algo_name = algo.__name__
    algo_output_dir = os.path.join("sorted_outputs", algo_name)
    os.makedirs(algo_output_dir, exist_ok=True)

    print(f"\nRunning algorithm {algo_name}")

    for path in inputList:
        top_folder = os.path.basename(os.path.dirname(path)).replace("_New", "")
        dataset_name = os.path.splitext(os.path.basename(path))[0]
        output_subdir = os.path.join(algo_output_dir, top_folder)
        os.makedirs(output_subdir, exist_ok=True)

        iterationTimes = []
        saved_result = None

        for i in range(1, 100):
            with open(path, 'r') as fin:
                lines = fin.readlines()
            # inputarray = [int(line.strip()) for line in lines]
            inputarray = [line for line in lines]
            start = time.perf_counter()

            if algo is quickSort:
                result = inputarray.copy()
                quickSort(result, 0, len(result) - 1)
            elif algo is heap_sort:
                result = heap_sort(inputarray.copy())
            elif algo is introSort:
                result = introSort(inputarray.copy())
            elif algo is bubble_sort:
                result = bubble_sort(inputarray.copy())
            elif algo is TimSort:
                result = TimSort(inputarray.copy())
            elif algo is selectionSort:
                result = selectionSort(inputarray.copy(), len(inputarray))
            elif algo is insertion_sort:
                result = insertion_sort(inputarray.copy())
            elif algo is mergeSort:
                result = inputarray.copy()
                mergeSort(result, 0, len(result) - 1)
            else:
                result = algo(inputarray.copy())

            end = time.perf_counter()

            if not is_sorted(result):
                print(f"Warning: {algo_name} failed on {dataset_name} (iter {i})")

            # Save only once
            if i == 1:
                saved_result = result
                save_path = os.path.join(output_subdir, f"{dataset_name}.txt")
                with open(save_path, "w") as fout:
                    for val in result:
                        fout.write(f"{val}\n")

            iterationTimes.append(end - start)

        if len(iterationTimes) == 0:
            print(f"Skipping {dataset_name} due to empty results")
            continue

        mean_time = np.mean(iterationTimes) * 1000
        median_time = np.median(iterationTimes) * 1000
        max_time = np.max(iterationTimes) * 1000
        min_time = np.min(iterationTimes) * 1000
        std_time = np.std(iterationTimes) * 1000

        print(f"Finished {dataset_name} | mean: {mean_time:.2f} ms")

        with open(output_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([algo_name, dataset_name, mean_time, median_time, max_time, min_time, std_time])
