'''
            TIJD: 55 minuten
            (geschat: 45 min)
'''

''' A
0.33 ~ 1/2^0 + 1/2^2 + 1/2^3 (4bit)
e = 1 ==> 001 (3bit)
0.1011E001
'''

''' B
    string[first:last][::-1]
    string[last-1:first-1:-1]
'''

''' C
    12
'''

''' D
    sets kunnen enkel hashable elementen bevatten en iets mutable is niet hashable.
    aangezien een st mutable is kan deze niet worden toegevoegd
    
    een frozenset is immutable, hieraan kunnen dus geen elementen worden toegevoegd
'''

''' E
    [-4, 0, 8, -6, 9, 0, 0, -22, 12, 13]  pivot = 12
    [-4, 0, 8, -6, 0, 0, -22, 9 12, 13]  pivot = 9

'''

''' F

    import math
    st = {1.0, -3.0, 0.0, float("inf"), 4.0}
    result = list(map((lambda x: math.sqrt(x) if x != float("inf") else None), filter(lambda y: y>0.0,st)))

    result = [1.0, 2.0, None]
'''

''' G
    last_names = ["Peters", None, "Jansen", "Steegmans"]
    first_names = ["Jan", "Peter", None]

    result = [str(first_names[i]) + " " + str(last_names[i]) for i in range(len(min(first_names,last_names,key=len))) if first_names[i] is not None and last_names[i] is not None]

    result = ["Jan Peters"]

'''

''' H
    SKIP
'''

''' I

class Trip:
    def __init__(self):
        self.__cities_ = []

t = Trip()
t._Trip__cities_.append("Leuven")
t.count = 1

    
'''


