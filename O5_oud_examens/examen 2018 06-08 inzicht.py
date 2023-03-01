'''
        TIJD:    NVT
        geschat: 30 min

'''

'''     A
    675
'''

'''     B
    [5,3]
'''

'''     C
    [-6,2,0,-2,2,|2|,4,10,9,6,4,16,4]
'''

'''     D
rats = [ Rational(3,4),Rational(12,6), Rational(4,5)]
#result = { Rational.get_numerator(Rat)/Rat.get_denominator() for Rat in rats if not Rat.is_normalised()}
result = { Rational.get_value(Rat) for Rat in rats if not Rat.is_normalised()}

assert result == {  0.75, 0.80 }
'''

''' E
    result = max(a,b)
    to_add = min(a,b)
    while to_add > 0:
        # result == max(a,b) + (min(a,b)-to_add)
        result += 1
        to_add -= 1
    
    # correctheidsbewijs
    # base step:
        result    = max(a,b)
        to_add    = min(a,b)
      ->result   == max(a,b) + (min(a,b)-to_add)
      ->result   == max(a,b) + (min(a,b)-min(a,b))
      ->result   == max(a,b)
      ->max(a,b) == max(a,b)
      
    #induction step:
    given  - result0 == max(a,b) + (min(a,b)-to_add0)
            result = result0 + 1
            to_add = to_add0 - 1
    to prove:
           - result == max(a,b) + (min(a,b)-to_add)
    proof:
        result0 + 1 == max(a,b) + (min(a,b)-to_add0 - 1)
        result0 + 1 == max(a,b) + (min(a,b)-to_add0) + 1
        result0     == max(a,b) + (min(a,b)-to_add0)
        result0     == result0
        
'''