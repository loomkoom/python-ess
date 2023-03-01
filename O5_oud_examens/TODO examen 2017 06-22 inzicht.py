'''
        TIJD:    25 min  (zonder complexiteit)
        geschat: 30 min

'''

'''     A
    6 bits
    2^-1 + 2^-3 + 2^-5 = 0.65625
    => ja
    => 0.101010

'''

'''     B
    LST = [10,20,20,100,90,50]
'''

'''     C
    1.25
'''

'''     D
    LST = [1,3,4,5,7,12,8,0,10]
'''

'''     E

def quicksort(lst,low=0,high=None):
 if high == None:                               # O(1)
    high = len(lst)                             # O(1)
 if low < high - 1:                             # O(1)
    pivot1,pivot2 = partition(lst,low,high)     # O(n)
    quicksort(lst,low,pivot1)
    quicksort(lst,pivot1,pivot2)
    quicksort(lst,pivot2,high) 
    
    SKIP

'''

'''     F
def issorted(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))

sequences = {(4,), (), (1, 2, 3), (6, 5, 4), (3, 7, 1, 0)}
result = {seq[::-1] for seq in sequences if issorted(seq)}

'''

'''     G
    ==> fout t.__x_ is bereikbaar buiten de klasse (enkel als t._Temp__x_)
        => het wordt geinterpreteerd als een nieuw atribuut en kan dus niet verhoogd worden
'''
