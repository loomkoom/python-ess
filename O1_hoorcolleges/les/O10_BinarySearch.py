"""
    Iteratief
"""


def binary_search(seq, val):
    """
    Check whether the given value is part of the given
    sequence.
    - The given sequence must be sorted in ascending
      order.
    """
    start = 0
    end = len(seq)

    while start < end:
        mid = (start + end) // 2

        if seq[mid] == val:
            return True
        elif seq[mid] < val:
            start = mid + 1
        else:
            end = mid
    return False


'''
    Recursiuef
'''

def binary_search(seq, val):

    if len(seq) == 0:
        return False

    mid = len(seq) // 2

    if seq[mid] == val:
        return True
    elif seq[mid] < val:
        return binary_search(seq[mid+1:],val)
    else:
        return binary_search(seq[:mid],val)

    # sneller / meer efficient:

def binary_search(seq, val, start=0, end=None):

    if end == None:
        end = len(seq)

    if start == end:
        return False

    mid = (start+end)//2

    if seq[mid] == val:
        return True
    elif seq[mid] < val:
        return binary_search(seq,val,mid+1,end)
    else:
        return binary_search(seq,val,start,mid)

assert binary_search((2,4,6,7,9,12,33,77),33)
assert not binary_search((2,4,6,7,9,12,33,77),11)
assert not binary_search((),5)
assert not binary_search((2,4,6,8,10),8,0,2)
assert not binary_search((2,4,6,8,10),4,2)
assert not binary_search((2,5,7),5,2,1)
