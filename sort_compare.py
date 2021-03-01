import argparse
# other imports go here
import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    for index in range(1,len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position-1] > current_value:
            a_list[position] = a_list[position-1]
            position = position - 1
        a_list[position] = current_value



def shell_sort(a_list):
    sublist_count = len(a_list)//2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            sublist_count = sublist_count // 2



def python_sort(a_list):
    return sorted(a_list)

if __name__ == "__main__":
    """Main entry point"""
    random.seed(100)
    list_sizes = [500,1000,5000]
    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            mylist = get_me_random_list(list_size)
            start = time.time()
            ordered_list = python_sort(mylist)
            end = time.time()
            sort_time = end - start
            total_time += sort_time
        average = total_time /100.
        print(f'Average time to sort a list of {list_size} using Python is {average: 0.8f} seconds')

        for list_size in list_sizes:
            for i in range(100):
                mylist = get_me_random_list(list_size)
                start = time.time()
                insertion_sort(mylist)
                end = time.time()
                sort_time = end - start
                total_time += sort_time
            average = total_time / 100
            print(f'Average time to sort a list of {list_size} using Insertion sort is {average: 0.8f} seconds')

        for list_size in list_sizes:
            for i in range(100):
                mylist = get_me_random_list(list_size)
                start = time.time()
                shell_sort(mylist)
                end = time.time()
                sort_time = end - start
                total_time += sort_time
            average = total_time / 100.
            print(f'Average time to sort a list of {list_size} using Shell sort is {average: 0.8f} seconds')