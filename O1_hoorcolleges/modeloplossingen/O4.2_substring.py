def pos_leftmost_occ\
        (string, substring, start=0, end=None):

  """
    Return the start position of the leftmost occurrence
    of the given substring in the portion of the given
    string delimited by start and end.
    None is returned if no such occurrence can be found.
  """

  if end == None:
    end = len(string)

  result = None

  while (start < end-len(substring)+1) and\
          (result == None) :
    if string[start:start+len(substring)] == substring:
      result = start
    start += 1

  return result



assert pos_leftmost_occ("abcdef","bcd") == 1
assert pos_leftmost_occ("abcdef","bdc") == None
assert pos_leftmost_occ("abcdef","abc") == 0
assert pos_leftmost_occ("abcdef","def") == 3
assert pos_leftmost_occ("abcdef","abcdef") == 0
assert pos_leftmost_occ("abcdef","") == 0
assert pos_leftmost_occ("","") == 0
assert pos_leftmost_occ("abcdef","abcdefg") == None
assert pos_leftmost_occ("abcdef","defg") == None
assert pos_leftmost_occ("abcdef","zab") == None
assert pos_leftmost_occ("abcabd","ab",1,5) == 3
assert pos_leftmost_occ("abab","ab",1,2) == None
assert pos_leftmost_occ("abab","ab",2,4) == 2