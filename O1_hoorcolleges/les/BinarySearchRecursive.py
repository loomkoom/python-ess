def binary_search(seq,val,start=0,end=None):

  """
    Check whether the given value is part of the slice
    seq[start:end].
    - The given sequence must be sorted in ascending
      order.
    - A default value of None for the end position
      actually means a value of len(seq).
  """

  if end == None:
    end = len(seq)

  #print( "To search:",val,"   Given:", seq[start:end])

  if start >= end:
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
assert not binary_search((2,4,6,8,10),8,0,2)
assert not binary_search((2,4,6,8,10),4,2)
assert not binary_search((2,5,7),5,2,1)
assert not binary_search((),5)
