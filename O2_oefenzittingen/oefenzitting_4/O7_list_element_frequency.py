def count_list_elements(lst):
    """
        Write a function that given a sequence returns the number of times each element occurs as a list of tuples.
        e.g. count_list_elements( ["a", "b", "c", "b", "c", "b", "a"] ) == [("a", 2), ("b", 3), ("c", 2)]
        As an extra, adjust your program so the output list is sorted on the first value of the tuple.
    """

    lst = list(lst)
    count_list = list()
    checked = list()

    for elem in lst:
        count = lst.count(elem)
        if elem not in checked:
            checked.append(elem)
            count_list += [(elem, count)]

    count_list = sorted(count_list)
    return count_list

# zonder count methode
def count_list_elements2(lst):
    """
        Write a function that given a sequence returns the number of times each element occurs as a list of tuples.
        e.g. count_list_elements( ["a", "b", "c", "b", "c", "b", "a"] ) == [("a", 2), ("b", 3), ("c", 2)]
        As an extra, adjust your program so the output list is sorted on the first value of the tuple.
    """

    lst = list(lst)
    count_list = list()
    checked = list()
    index = None

    for elem in lst:
        if elem not in checked:
            checked.append(elem)
            count_list += [(elem, 1)]
        else:
            for n in count_list:
                if n[0] == elem:
                    index = count_list.index(n)
            count_list[index] = (elem, count_list[index][1] + 1)

    count_list = sorted(count_list)
    print(count_list)
    return count_list


assert count_list_elements(["a", "b", "c", "b", "c", "b", "a"]) == [("a", 2), ("b", 3), ("c", 2)]
assert count_list_elements(["c", "b", "a", "a", "b", "c", "b"]) == [("a", 2), ("b", 3), ("c", 2)]
assert count_list_elements([1, 4, 2, 3, 2, 9, 1]) == [(1, 2), (2, 2), (3, 1), (4, 1), (9, 1)]
print("\n")
assert count_list_elements2(["a", "b", "c", "b", "c", "b", "a"]) == [("a", 2), ("b", 3), ("c", 2)]
assert count_list_elements2(["c", "b", "a", "a", "b", "c", "b"]) == [("a", 2), ("b", 3), ("c", 2)]
assert count_list_elements2([1, 4, 2, 3, 2, 9, 1]) == [(1, 2), (2, 2), (3, 1), (4, 1), (9, 1)]
