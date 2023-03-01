def erase_val(lst1,lst2,val,nb_occs,start=0):

    if nb_occs == 0:
        return True
    if (start > len(lst2) - nb_occs) or (start > len(lst1) - nb_occs):
        return False

    if lst1[start] == lst2[start] == val:
        if erase_val(lst1,lst2,val,nb_occs-1,start+1):
            del lst1[start]
            del lst2[start]
            return True
        else:
            return False
    return erase_val(lst1,lst2,val,nb_occs,start+1)

lst1 = [1,0,2,0,5,7,0,9,0,1,3,0,5,0,0,8]
lst2 = [3,0,0,5,2,6,0,8,0,2]

assert erase_val(lst1,lst2,0,2)
assert lst1 == [1,2,0,5,7,9,0,1,3,0,5,0,0,8]
assert lst2 == [3,0,5,2,6,8,0,2]

lst1 = [1,0,2,0,5,7,0,9,0,1,3,0,5,0,0,8]
lst2 = [3,0,0,5,2,6,0,8,0,2]

assert not erase_val(lst1,lst2,0,4)
assert lst1 == [1,0,2,0,5,7,0,9,0,1,3,0,5,0,0,8]
assert lst2 == [3,0,0,5,2,6,0,8,0,2]