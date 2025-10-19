# 700HPC

## To run
`python3 wrapper.py` 

--------------------------------------------

## submitjob.sh

- sinfo -N -o "%N %P %T %C %m %f %G"
- sbatch submitjob.sh
- squeue -u $USER

-----------------------------

#SBATCH --job-name=sorting_benchmark_g021_gpu_2
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=30
#SBATCH --mem=50G
#SBATCH --time=23:00:00
#SBATCH --output=sorting_g021_gpu_2%j.out
#SBATCH --error=sorting_g021_gpu_2%j.err
#SBATCH --constraint=gpu,eth_1g,r28c1,asu_int_6_64


## tobe saved as : sorting_g020_gpu_6cores_gpu_4GHz.out(154796) (hybrid th 10) (incomplete bubble sort)
- #SBATCH --job-name=sorting_benchmark_g020_gpu_1
- #SBATCH --partition=gpu
- #SBATCH --nodes=1
- #SBATCH --ntasks=1
- #SBATCH --cpus-per-task=6
- #SBATCH --mem=50G
- #SBATCH --time=23:00:00
- #SBATCH --output=sorting_%j.out
- #SBATCH --error=sorting_%j.err
- #SBATCH --constraint=gpu,eth_1g,r28c1,asu_int_6_64


### Saved as: sorting_g016_gpu_32cores_gpu_3GHz_best_th32.out (hybrid th 32) (almost all results except 5m by bubble sort)(Best config for our use case)
- #SBATCH --job-name=sorting_benchmark_g016_gpu_32cores_gpu_1
- #SBATCH --partition=gpu
- #SBATCH --nodes=1
- #SBATCH --ntasks=1
- #SBATCH --cpus-per-task=32
- #SBATCH --mem=60G
- #SBATCH --time=23:00:00
- #SBATCH --output=sorting_%j.out
- #SBATCH --error=sorting_%j.err
- #SBATCH --constraint=gpu,eth_10g,r27c1


### tobe saved as: sorting_g019_6cores_gpu_4GHz.out (hybrid th 32) (incomplete bubble sort)
- #SBATCH --job-name=sorting_benchmark_g019_gpu_1
- #SBATCH --partition=gpu
- #SBATCH --nodes=1
- #SBATCH --ntasks=1
- #SBATCH --cpus-per-task=6
- #SBATCH --mem=50G
- #SBATCH --time=23:00:00
- #SBATCH --output=sorting_%j.out
- #SBATCH --error=sorting_%j.err
- #SBATCH --constraint=gpu,eth_1g,r28c4

------------------------------

### sorting_g019_6cores_r28c4.out
- #SBATCH --job-name=sorting_benchmark_g019_r28c4
- #SBATCH --partition=gpu
- #SBATCH --nodes=1
- #SBATCH --ntasks=1
- #SBATCH --cpus-per-task=6
- #SBATCH --mem=50G
- #SBATCH --time=15:00:00
- #SBATCH --output=sorting_%j.out
- #SBATCH --error=sorting_%j.err
- #SBATCH --constraint=r28c4
- cd /moosefs/home/s265d007/projects/git/700HPC

----------------------------------------------

### sorting_g016_32cores_delint16128.out
- #SBATCH --job-name=sorting_benchmark_g016_gpu_32cores_delint16128
- #SBATCH --partition=gpu
- #SBATCH --nodes=1
- #SBATCH --ntasks=1
- #SBATCH --cpus-per-task=32
- #SBATCH --mem=120G
- #SBATCH --time=12:00:00
- #SBATCH --output=sorting_%j.out
- #SBATCH --error=sorting_%j.err
- #SBATCH --constraint=del_int_16_128


## TimSort times: 

- Time taken for half_sorted_1000.txt: 0.0008
- Time taken for half_sorted_5000.txt: 0.0050
- Time taken for half_sorted_10000.txt: 0.0107
- Time taken for half_sorted_50000.txt: 0.0638
- Time taken for half_sorted_100000.txt: 0.1356
- Time taken for random_numbers_1000.txt: 0.0009
- Time taken for random_numbers_5000.txt: 0.0057
- Time taken for random_numbers_10000.txt: 0.0120
- Time taken for random_numbers_50000.txt: 0.0709
- Time taken for random_numbers_100000.txt: 0.1513
- Time taken for reverse_1000-float.txt: 0.0012
- Time taken for reverse_5000-float.txt: 0.0068
- Time taken for reverse_10000-float.txt: 0.0143
- Time taken for reverse_50000-float.txt: 0.0790
- Time taken for reverse_100000-float.txt: 0.1659
- Time taken for Sorted_1000.txt: 0.0004
- Time taken for Sorted_10000.txt: 0.0060
- Time taken for Sorted_50000.txt: 0.0375
- Time taken for Sorted_100000.txt: 0.0808

## quicksort times:

- Time taken for half_sorted_1000.txt: 0.0007
- Time taken for half_sorted_5000.txt: 0.0044
- Time taken for half_sorted_10000.txt: 0.0086
- Time taken for half_sorted_50000.txt: 0.0541
- Time taken for half_sorted_100000.txt: 0.1126
- Time taken for random_numbers_1000.txt: 0.0006
- Time taken for random_numbers_5000.txt: 0.0037
- Time taken for random_numbers_10000.txt: 0.0079
- Time taken for random_numbers_50000.txt: 0.0481
- Time taken for random_numbers_100000.txt: 0.0981
- Time taken for reverse_1000-float.txt: 0.0008
- Time taken for reverse_5000-float.txt: 0.0055
- Time taken for reverse_10000-float.txt: 0.0194
- Time taken for reverse_50000-float.txt: 0.1199
- Time taken for reverse_100000-float.txt: 0.3256
- Time taken for Sorted_1000.txt: 0.0060
- Time taken for Sorted_5000.txt: 0.4320
- Time taken for Sorted_10000.txt: 0.6767
- Time taken for Sorted_50000.txt: 44.8134
- Time taken for Sorted_100000.txt: 90.8357

## heap_sort times: 

- Time taken for half_sorted_1000.txt: 0.0014
- Time taken for half_sorted_5000.txt: 0.0091
- Time taken for half_sorted_10000.txt: 0.0197
- Time taken for half_sorted_50000.txt: 0.1251
- Time taken for half_sorted_100000.txt: 0.2733
- Time taken for random_numbers_1000.txt: 0.0014
- Time taken for random_numbers_5000.txt: 0.0093
- Time taken for random_numbers_10000.txt: 0.0204
- Time taken for random_numbers_50000.txt: 0.1237
- Time taken for random_numbers_100000.txt: 0.2860
- Time taken for reverse_1000-float.txt: 0.0013
- Time taken for reverse_5000-float.txt: 0.0086
- Time taken for reverse_10000-float.txt: 0.0187
- Time taken for reverse_50000-float.txt: 0.1157
- Time taken for reverse_100000-float.txt: 0.2430
- Time taken for Sorted_1000.txt: 0.0015
- Time taken for Sorted_10000.txt: 0.0192
- Time taken for Sorted_50000.txt: 0.1174
- Time taken for Sorted_100000.txt: 0.2522

## introsort times: 

- Time taken for half_sorted_1000.txt: 0.0009
- Time taken for half_sorted_5000.txt: 0.0048
- Time taken for half_sorted_10000.txt: 0.0105
- Time taken for half_sorted_50000.txt: 0.0597
- Time taken for half_sorted_100000.txt: 0.1282
- Time taken for random_numbers_1000.txt: 0.0008
- Time taken for random_numbers_5000.txt: 0.0052
- Time taken for random_numbers_10000.txt: 0.0100
- Time taken for random_numbers_50000.txt: 0.0594
- Time taken for random_numbers_100000.txt: 0.1236
- Time taken for reverse_1000-float.txt: 0.0018
- Time taken for reverse_5000-float.txt: 0.0146
- Time taken for reverse_10000-float.txt: 0.0320
- Time taken for reverse_50000-float.txt: 0.2169
- Time taken for reverse_100000-float.txt: 0.5179
- Time taken for Sorted_1000.txt: 0.0030
- Time taken for Sorted_10000.txt: 0.0457
- Time taken for Sorted_50000.txt: 0.1861
- Time taken for Sorted_100000.txt: 0.6125

## selectionSort times: 

- Time taken for half_sorted_1000.txt: 0.0218
- Time taken for half_sorted_5000.txt: 0.5353
- Time taken for half_sorted_10000.txt: 2.1253
- Time taken for half_sorted_50000.txt: 53.0566
- Time taken for half_sorted_100000.txt: 217.6798
- Time taken for random_numbers_1000.txt: 0.0221
- Time taken for random_numbers_5000.txt: 0.5806
- Time taken for random_numbers_10000.txt: 2.1845
- Time taken for random_numbers_50000.txt: 55.5730
- Time taken for random_numbers_100000.txt: 214.4332
- Time taken for reverse_1000-float.txt: 0.0209
- Time taken for reverse_5000-float.txt: 0.5299
- Time taken for reverse_10000-float.txt: 2.1108
- Time taken for reverse_50000-float.txt: 52.8744
- Time taken for reverse_100000-float.txt: 212.7102
- Time taken for Sorted_1000.txt: 0.0203
- Time taken for Sorted_10000.txt: 2.0868
- Time taken for Sorted_50000.txt: 53.5365
- Time taken for Sorted_100000.txt: 211.3493

## insertion_sort times:

- Time taken for half_sorted_1000.txt: 0.0100
- Time taken for half_sorted_5000.txt: 0.3154
- Time taken for half_sorted_10000.txt: 0.9970
- Time taken for half_sorted_50000.txt: 31.6051
- Time taken for half_sorted_100000.txt: 103.3768
- Time taken for random_numbers_1000.txt: 0.0128
- Time taken for random_numbers_5000.txt: 0.3035
- Time taken for random_numbers_10000.txt: 1.2091
- Time taken for random_numbers_50000.txt: 30.2923
- Time taken for random_numbers_100000.txt: 125.8403
- Time taken for reverse_1000-float.txt: 0.0214
- Time taken for reverse_5000-float.txt: 0.4496
- Time taken for reverse_10000-float.txt: 2.1848
- Time taken for reverse_50000-float.txt: 45.7298
- Time taken for reverse_100000-float.txt: 221.3846
- Time taken for Sorted_1000.txt: 0.0023
- Time taken for Sorted_10000.txt: 0.2161
- Time taken for Sorted_50000.txt: 15.0970
- Time taken for Sorted_100000.txt: 22.0687

## bubble_sort times: 

- Time taken for half_sorted_1000.txt: 0.0246
- Time taken for half_sorted_5000.txt: 0.7215
- Time taken for half_sorted_10000.txt: 2.7867
- Time taken for half_sorted_50000.txt: 78.1301
- Time taken for half_sorted_100000.txt: 293.2752
- Time taken for random_numbers_1000.txt: 0.0261
- Time taken for random_numbers_5000.txt: 0.7098
- Time taken for random_numbers_10000.txt: 2.8648
- Time taken for random_numbers_50000.txt: 73.4194
- Time taken for random_numbers_100000.txt: 293.9530
- Time taken for reverse_1000-float.txt: 0.0281
- Time taken for reverse_5000-float.txt: 0.7519
- Time taken for reverse_10000-float.txt: 3.3535
- Time taken for reverse_50000-float.txt: 78.1032
- Time taken for reverse_100000-float.txt: 343.0905
- Time taken for Sorted_1000.txt: 0.0164
- Time taken for Sorted_10000.txt: 1.8992
- Time taken for Sorted_50000.txt: 27.3857
- Time taken for Sorted_100000.txt: 197.7079