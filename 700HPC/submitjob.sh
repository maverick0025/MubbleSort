#!/bin/bash

#SBATCH --job-name=sorting_benchmark_g021_gpu
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=30
#SBATCH --mem=50G
#SBATCH --time=23:00:00
#SBATCH --output=sorting_g021_gpu_2%j.out
#SBATCH --error=sorting_g021_gpu_%j.err
#SBATCH --constraint=gpu,eth_1g,r28c1,asu_int_6_64

cd /moosefs/home/s265d007/projects/git2/700HPC

python3 wrapper.py