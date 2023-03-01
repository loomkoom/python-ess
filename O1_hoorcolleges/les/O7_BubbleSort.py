# algoritme dat sorteert door telkens de volgende waarde te wisselen als deze kleiner is


def bubble_sort(lst):
    '''

    '''

    start_sorted_part = len(lst)

    while start_sorted_part >= 2:
        # swap alle elementen vanaf positie 0 tot positie 'start_sorted_part'

        swap_elements(lst, start_sorted_part)

        start_sorted_part -= 1


def swap_elements(lst, start_sorted_part):
    volgende_pos = 0
    while volgende_pos < start_sorted_part - 1:

        if lst[volgende_pos] > lst[volgende_pos + 1]:
            lst[volgende_pos], lst[volgende_pos + 1] = lst[volgende_pos + 1], lst[volgende_pos]
        volgende_pos += 1


# Empty list
lst = []
bubble_sort(lst)
assert lst == []

# List with one element
lst = [1]
bubble_sort(lst)
assert lst == [1]

# List with several elements
lst = [7, 5, 1, 8, 2, 3, 9, 0, 4, 6]
bubble_sort(lst)
assert lst == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sorted list
lst = [1,2,3]
bubble_sort(lst)
assert lst == [1,2,3]

# Inverted list
lst = [3,2,1]
bubble_sort(lst)
assert lst == [1,2,3]
