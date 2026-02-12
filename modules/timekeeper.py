# import atexit
from time import strftime, localtime
from datetime import timedelta

# This function converts the time to a string for printing in a 
# standardized format
def seconds_to_str(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))
    
# Prints a nicely formatted timestamp
def log(s, elapsed=None):
    # Sets a divider of ========================================
    line = "="*50
    print(line)
    
    # Prints time with provided string following it
    print(seconds_to_str(), '-', s)
    
    # If elapsed time provided, prints it on a new line
    if elapsed:
        print(f"Elapsed time: {elapsed} seconds")
    print(line)
    print()
    
# def endlog():
#     end = time()
#     elapsed = end - start
#     log("End Program", seconds_to_str(elapsed))
    
# start = time()
# atexit.register(endlog)
# log("Start Program")