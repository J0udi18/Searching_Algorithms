# To Do...
# Add merge sort
# Loop program

import random


# ******  Functions go here ********


# function below checks that user input is an integer
def intcheck(question, low=None, high=None):
    # sets up error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue


# List Generator
# Set up items list
def get_data(how_many, list_type):
    items = []

    upper_limit = how_many * 10

    if list_type == "Random" or list_type == "Reverse" or list_type == "Nearly":
        for item in range(0, how_many):
            item_value = random.randint(0, upper_limit)
            items.append(item_value)

    else:
        if how_many <= 20:
            choose_from = 3
        else:
            choose_from = how_many // 10

        for item in range(0, how_many):
            item_value = random.randint(0, choose_from)
            items.append(item_value)

    if list_type == "Reverse":
        items.sort(reverse=True)

    elif list_type == "Nearly":
        items.sort()  # sort items
        no_to_move = len(items) // 4  # number of items to go out of order

        for item in range(0, no_to_move):
            move_from = random.randint(0, no_to_move)
            move_to = random.randint(0, no_to_move)
            items.insert(move_to, items.pop(move_from))

    return (items)


def algorithm_checker(question):
    valid = False
    while not valid:

        choice = input(question).lower()

        if choice == "q" or choice == "quick":
            choice = "Quick Sort"
            return choice
        elif choice == "i" or choice == "insertion":
            choice = "Insertion Sort"
            return choice
        elif choice == "m" or choice == "merge":
            choice = "Merge Sort"
            return choice
        else:
            print("I don't understand...\n")


# Quick Sort Functions...
def test_quick_sort(data):
    '''Create a random list and measure the performance of quicksort on it'''
    sample_list = data
    comparisons_made = quick_sort(sample_list)
    return (comparisons_made)


def quick_sort(sample_list):
    '''Perform quicksort on values in sample_list and
    return the number of comparisons required'''
    # based on code from "Problem Solving with Algorithms and Data Structures"
    # By Brad Miller and David Ranum, runestoneinteractive.org
    return quicksort_partial_list(sample_list, 0, len(sample_list) - 1)


def quicksort_partial_list(sample_list, first, last):
    '''Recursively quicksort sample_list between first and last inclusive'''
    comparisons = 0
    if first < last:
        partition_point = partition(sample_list, first, last)
        comparisons += (last - first)  # partition compares one less than items in list
        left_comps = quicksort_partial_list(sample_list, first, partition_point - 1)
        right_comps = quicksort_partial_list(sample_list, partition_point + 1, last)
        comparisons += left_comps + right_comps
        return comparisons
    else:
        return 0  # no comparisons as sublist is empty


def partition(alist, first, last):
    '''Partition alist into smaller and larger values,
    returns pivot position'''
    pivotvalue = alist[first]
    left_to_right, right_to_left = first + 1, last
    done = False
    while not done:
        while left_to_right <= right_to_left and alist[left_to_right] <= pivotvalue:
            left_to_right = left_to_right + 1
        while alist[right_to_left] >= pivotvalue and left_to_right <= right_to_left:
            right_to_left = right_to_left - 1
        if right_to_left < left_to_right:
            done = True
        else:
            alist[left_to_right], alist[right_to_left] = alist[right_to_left], alist[left_to_right]
    alist[first], alist[right_to_left] = alist[right_to_left], alist[first]
    return right_to_left


def insertion_sort(arr, simulation=False):
    count = 0

    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
            count += 1
        # Break and do the final swap
        arr[pos] = cursor
        # count += 1

    # count += 1

    return count


# Merge Sort function
# source: https://stackoverflow.com/questions/42608630/how-to-add-a-comparison-counter-for-merge-sort-in-python


def mergesort(argshuffledlist):
    int_num_comps = 0

    if len(argshuffledlist) > 1:
        int_mid_val = len(argshuffledlist) // 2
        list_left_half = argshuffledlist[:int_mid_val]
        list_right_half = argshuffledlist[int_mid_val:]

        left_part = mergesort(list_left_half)
        right_part = mergesort(list_right_half)

        int_num_comps += left_part[1] + right_part[1]

        i = 0
        j = 0
        k = 0
        while i < len(list_left_half) and j < len(list_right_half):
            int_num_comps += 1
            if list_left_half[i] < list_right_half[j]:
                argshuffledlist[k] = list_left_half[i]
                i = i + 1

            else:
                argshuffledlist[k] = list_right_half[j]
                j = j + 1

            k = k + 1

        while i < len(list_left_half):
            argshuffledlist[k] = list_left_half[i]
            i = i + 1
            k = k + 1
            int_num_comps += 1

        while j < len(list_right_half):
            argshuffledlist[k] = list_right_half[j]
            j = j + 1
            k = k + 1
            int_num_comps += 1

    return argshuffledlist, int_num_comps


# ****** Main Routine goes here ******

# Get user input

print("**** SQIM Sort - How To")
print()
print("This program allows you to see how many comparisons\n might be needed to \nsort various types "
      "of data quick sort, selection sort or merge sort.\n"
      "\n"
      ""
      "If you know what type of data you need to sort, this \nwill inform your choice "
      " of sorting algorithm"
      "\n"
      "\nRun the program several times using the same data size and sorting algorithm.  What do you notice?\n"
      "\nTry using different data sizes (eg: 10, 100, 500, (maximum of 996)\n and see how\n "
      "your chosen algorithm compares with selection sort.\n\n")

again = ""
while again == "":
    how_many = intcheck("How many items? ", 1, 996)
    choose_algorithm = algorithm_checker("Which algorithm? \n"
                                         "for Quick Sort, type 'q'\n"
                                         "for Merge Sort, type 'm' \n"
                                         "for Insertion Sort, type 'i'\n")

    data_types = ["Random", "Reverse", "Nearly", "Few Unique"]

    print()

    print("***** {} Comparison ********".format(choose_algorithm))

    if choose_algorithm == "Insertion Sort":
        print("Note: If the # of comparisons for 'reverse' data is LESS than\n"
              "selection sort, that is because the data includes at duplicates")
        print()

    elif choose_algorithm == "Merge Sort":
        print(''' Note: Whilst merge sort may have fewer comparisons
compared with other methods, it is not always
the most efficient option.

This tool only counts comparisons.  This does 
not show the full cost of merge sort as 
merge sort requires extra space.

Generally we'd use quick sort instead 
of merge sort as it uses less space 
and the actual cost is less.

For a more detailed explanation, please 
google this question.''')
        print()

    select_sort = (how_many * (how_many - 1)) / 2

    for item in data_types:
        data = get_data(how_many, item)
        # print(data)

        if choose_algorithm == "Quick Sort":
            comparisons = quick_sort_random = test_quick_sort(data)
        elif choose_algorithm == "Insertion Sort":
            comparisons = insertion_sort(data)
        else:
            merge_comp = mergesort(data)
            merge_comp = merge_comp[1]
            comparisons = merge_comp - how_many + 1

        print("{} - {}".format(item, comparisons))

    print()
    print("Selection Sort: {:.0f}".format(select_sort))
    print()
    again = input("Press <enter> to run this program again or any key to quit ")

print("Thank you.  Hopefully you have gained an insight into when quick sort is a good option")
