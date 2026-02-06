import random
import concurrent.futures
from config import MAX_VALUE, MIN_VALUE, MAX_PROCESSES
from modules.timekeeper import *

# Worker process to generate slices of the overall list
def generate_random_ints(count):
    int_list = []
    for i in range(0, count):
        int_list.append(random.randint(MIN_VALUE, MAX_VALUE))
    
    # print("Generated list:", int_list)
    
    return int_list

def generate_unsorted_list(size, seed=None):
    log("Generating random list")
    start = perf_counter()
    if seed:
        random.seed(seed)
    else:
        random.seed()
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_PROCESSES) as executor:
        futures = [
            executor.submit(generate_random_ints, size // MAX_PROCESSES)
            for i in range(MAX_PROCESSES)
        ]
        
    unsorted_list = []
    
    for future in futures:
        unsorted_list.extend(future.result())
        
    while len(unsorted_list) < size:
        unsorted_list.append(random.randint(MIN_VALUE, MAX_VALUE))
    
    end = perf_counter()
        
    log("Completed random list", end - start)
        
    return unsorted_list


def generate_random_ints_slow(size, seed=None):
    if seed:
        random.seed(seed)
    else:
        random.seed()
    
    list = []
    while len(list) < size:
        list.append(random.randint(MIN_VALUE, MAX_VALUE))
    
    return list