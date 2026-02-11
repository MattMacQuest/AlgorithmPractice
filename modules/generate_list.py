import random
import concurrent.futures
from config import MAX_VALUE, MIN_VALUE, MAX_PROCESSES, LIST_PREVIEW_LENGTH
from modules.timekeeper import *

# Worker process to generate slices of the overall list
def generate_random_ints(count):
    int_list = []
    for i in range(0, count):
        int_list.append(random.randint(MIN_VALUE, MAX_VALUE))
    
    return int_list

# This function take size as an input and generates an unsorted list of random numbers of the provided size.
# It splits the task into os.cpu_count() number of tasks to make generating large lists significantly faster.
# The function also times the process of generating the list, providing a benchmark that could be saved
# to a provided "app" object for later reference as needed. Mostly it's just for show at the moment
def generate_unsorted_list(size, seed=None):
    log("Generating random list")
    start = perf_counter()
    if seed:
        random.seed(seed)
    else:
        random.seed()
    
    # Fills a list with worker processes using python's concurrent futures library.
    with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_PROCESSES) as executor:
        futures = [
            executor.submit(generate_random_ints, size // MAX_PROCESSES)
            for i in range(MAX_PROCESSES)
        ]
    
    unsorted_list = []
    
    # Extends the final unsorted list with the result of each generate_random_ints() call
    for future in futures:
        unsorted_list.extend(future.result())
        
    while len(unsorted_list) < size:
        unsorted_list.append(random.randint(MIN_VALUE, MAX_VALUE))
    
    end = perf_counter()
    if size <= LIST_PREVIEW_LENGTH:
        print(unsorted_list, "\n")
    else:
        print("[", end="")
        for i in range(LIST_PREVIEW_LENGTH):
            if i < LIST_PREVIEW_LENGTH - 1:
                print(unsorted_list[i], end=", ")
            else:
                print(unsorted_list[i], end=", ...]\n")
    # Added input to make everything actually readable
    log("Completed random list", end - start)
    input("Press enter to continue")
        
    return unsorted_list


# Left in for posterity, and if for some reason I need a single threaded generation function
def generate_random_ints_slow(size, seed=None):
    if seed:
        random.seed(seed)
    else:
        random.seed()
    
    list = []
    while len(list) < size:
        list.append(random.randint(MIN_VALUE, MAX_VALUE))
    
    return list