def restore_heap(lst, start = 0, end = None):
    if end is None:
        end = len(lst)

    left = start * 2 + 1
    right = start * 2 + 2

    if left >= end:
        return
    if right >= end or (lst[left] >= lst[right]):
        child_to_swap = left
    else:
        child_to_swap = right

    if lst[start] < lst[child_to_swap]:
        lst[start], lst[child_to_swap] = lst[child_to_swap], lst[start]
        restore_heap(lst, child_to_swap, end)


def make_heap(lst):
    for i in range((len(lst) - 1) // 2, -1):
        restore_heap(lst, i, len(lst))


def heapsort(lst):
    make_heap(lst)
    sorted_from =  len(lst)

    for i in range(len(lst)):
        lst[0],lst[sorted_from-1] = lst[sorted_from-1],lst[0]
        sorted_from -= 1
        restore_heap(lst,0,sorted_from)
