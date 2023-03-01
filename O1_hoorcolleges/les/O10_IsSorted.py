def IsSorted(val):

    if len(val) <= 1:
        return True

    return (val[0] <= val[1]) and (IsSorted(val[1:]))


assert IsSorted((1,6,9,23,456,789))
assert not IsSorted((3,4,6,2,10))
assert not IsSorted((1,5,9,789,3))
assert not IsSorted((10, -2, 6, 20 ,36))
assert IsSorted((33,))
assert IsSorted(())
