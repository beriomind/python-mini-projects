# --------------------------------------
# - CPU Characteristics (cpu-characteristics.py)
# - Version 2
# --------------------------------------
import os

logical_threads = os.cpu_count()
estimated_cores = logical_threads // 2

print(f"Your PC has {logical_threads} logical processors (threads).")
print(f"Assuming standard hyperthreading, that usually means {estimated_cores} physical cores.")


# --------------------------------------
# - CPU Characteristics (cpu-characteristics.py)
# - Version 1
# --------------------------------------

import multiprocessing as mp

print(f"Your PC have {mp.cpu_count()} CPUs ")
print(f"That means you have {mp.cpu_count()/2} Cores and {mp.cpu_count()} Threads ")
