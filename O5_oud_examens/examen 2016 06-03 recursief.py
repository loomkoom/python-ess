'''
            TIJD:  NVT
            (geschat: 60 min)

'''


# De functie
# moet de herschikking doorvoeren op de gegeven heap
# De onderliggende binaire
# boom moet dus nog steeds compleet en geordend zijn
# 2 testen:
# -  3 en 80 in die volgorde toevoegen aan die voorbeeldheap (HB).

# Als de waarde in de wortel van een heap zich in een dergelijke lijst bevindt op positie
# R, dan is de waarde in de wortel van de linkerdeelboom terug te vinden op positie 2*R+1, en de
# waarde in de wortel van de rechterdeelboom op positie 2*R+2

# Als h de heap uit Figuur 18 van de cursustekst was,
# zou length(h,1) de waarde 6 teruggeven,
# zou has_complete_lowest_level(h,1) de waarde False teruggeven,
# en zou has_complete_lowest_level(h,3) de waarde True teruggeven.

def length(heap, index_root = 0):
    """
    Return the length of the heap that starts at the given index.
    """


def has_complete_lowest_level(heap, index_root = 0):
    """
    Check whether the heap that starts at the given index has a lowest level
    that is completely filled.
    """


def add(heap, element, index_root = 0):
    index_left_child = index_root * 2 + 1
    index_right_child = index_root * 2 + 2

    if index_root >= len(heap):
        heap.append(element)
    if heap[index_root] < element:
        old_root = heap[index_root]
        heap[index_root] = element
        add(heap, old_root, index_root)
    elif length(heap, index_left_child) == length(index_right_child) or not has_complete_lowest_level(heap, index_left_child):
        add(heap, element, index_left_child)
    else:
        add(heap, element, index_right_child)
