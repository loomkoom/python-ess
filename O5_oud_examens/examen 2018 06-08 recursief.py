def herverdeel(lst,start = 0):

    if len(lst) == start:
        if (start == 0 or start%2 ==1 or lst[start-1] == lst[start-2]):
            return ()
        else:
            return None
    rest = None
    for i in range(start,len(lst)):
        lst[start],lst[i] = lst[i],lst[start]

        if start % 2 == 1:
            rest =  herverdeel(lst,start+1)
        elif start == 0 or lst[start-1] == lst[start-2]+ lst[start]:
            rest = herverdeel(lst,start+1)

        lst[start], lst[i] = lst[i], lst[start]

        if rest is not None:
            print((lst[i],) + rest)
            return (lst[i],) + rest
    return None
assert herverdeel([]) == ()
assert herverdeel([3]) == (3,)
assert herverdeel([3,3]) == (3,3)
assert herverdeel([1,6]) is None
assert herverdeel([2,3,5]) in { (2,5,3), (3,5,2) }
assert herverdeel([7,3,8]) is None
assert herverdeel([3,12,-12,4,9,-3,7,-12]) == \
 (4,7,3,12,9,-3,-12,-12)
assert herverdeel([10,20,30,40,60]) == (10,30,20,60,40)