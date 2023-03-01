def intersection(seq_1,seq_2):

    """
      Write a function that returns the intersection (common elements) of two sequences.
      The return value should be a tuple.
      Some examples:

      [0,1,2] , [1,2,3]                         (1,2)
      "abc" ,  "bde"                            ("b",)
      (1,2,3), (3,4,5)                          (3,)
      ('a', 'bc', 'd') , ('bc', 'z', 2, 'd')    ('bc', 'd')
      ( [1,2], [2,3] ), ( [2,3], [5,6] )        ( [2,3], )
      ( (1,2), (2,3) ), ( (2,3) , (5,6) )       ((2,3),)
    """
    #
    # common_value = []
    #
    # for index in range(len(seq_1)):
    #     if seq_1[index] in seq_2:
    #         common_value.append(seq_1[index])
    #
    # common_occurences = tuple(common_value)
    #
    # return common_occurences


    common_values = ()

    for index in range(len(seq_1)):
        if seq_1[index] in seq_2:
            common_values = common_values + (seq_1[index],)
    return common_values


print(intersection([0,1,2] , [1,2,3]))

assert   intersection([0,1,2] , [1,2,3] )                        == (1,2)
assert   intersection( "abc" ,  "bde" )                          == ("b",)
assert   intersection((1,2,3), (3,4,5))                          == (3,)
assert   intersection( ('a', 'bc', 'd') , ('bc', 'z', 2, 'd'))    == ('bc', 'd')
assert   intersection( ( [1,2], [2,3] ), ( [2,3], [5,6] ))        == ( [2,3], )
assert   intersection(( (1,2), (2,3) ), ( (2,3) , (5,6) ))       == ((2,3),)
