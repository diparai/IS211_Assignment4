import argparse
# other imports go here

import random
import time
from multiprocessing.resource_sharer import stop


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    
def sequential_search(a_list,item):
    starttime = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(a_list,item):
    pos = 0
    found = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def binary_search_iterative(a_list,item):
    first = 0
    last = len(a_list)-1
    found = False
    while first <= last and not found:
        midpoint = (first+last)//2
        if a_list[midpoint]== item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
        return found

    
def binary_search_recursive(a_list,item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list)//2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint],item)
        else:
            return binary_search_recursive(a_list[midpoint+1:],item)



if __name__ == "__main__":
    """Main entry point"""
    random.seed(100)
    list_sizes = [500, 1000, 5000]
    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            mylist = get_me_random_list(list_size)
            start = time.time()
            ordered_list = sequential_search(mylist,-1)
            end = time.time()
            search_time = end - start
            total_time += search_time
        average = total_time / 100.
        print(f'Average time to sort a list of {list_size} using sequential search is {average: 0.8f} seconds')

    for list_size in list_sizes:
        for i in range(100):
            mylist = get_me_random_list(list_size)
            start = time.time()
            ordered_list = ordered_sequential_search(mylist,-1)
            end = time.time()
            search_time = end - start
            total_time += search_time
        average = total_time /100.
        print(f'Average time to sort a list of {list_size} using Ordered sequential search is {average: 0.8f} seconds')

    for list_size in list_sizes:
        for i in range(100):
            mylist = get_me_random_list(list_size)
            start = time.time()
            ordered_list = binary_search_iterative(mylist,-1)
            end = time.time()
            search_time = end - start
            total_time += search_time
        average = total_time /100.
        print(f'Average time to sort a list of {list_size} using Binary iterative search is {average: 0.8f} seconds')

    for list_size in list_sizes:
        for i in range(100):
            mylist = get_me_random_list(list_size)
            start = time.time()
            ordered_list = binary_search_recursive(mylist,-1)
            end = time.time()
            search_time = end - start
            total_time += search_time
        average = total_time /100.
        print(f'Average time to sort a list of {list_size} using Binary recursive search is {average: 0.8f} seconds')

