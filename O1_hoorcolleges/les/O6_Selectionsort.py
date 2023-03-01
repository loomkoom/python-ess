# zoeken naar het kleinste element en dat naar voor brengen tot alles correct staat:

# groot probleem splitsen in deelproblemen / deelfuncties
#   en eerst het grote probleem oplossen / neerschrijven
#   nadien de deelfuncties oplossen

def selection_sort(lst):

    # volgende_pos = 0

    # while volgende_pos < len(lst) -1:
    for volgende_pos in range(0,len(lst)-1):

        pos_kleinste_element = index_smallest_of(lst,volgende_pos)
        lst[volgende_pos],lst[pos_kleinste_element] = lst[pos_kleinste_element], lst[volgende_pos]

        volgende_pos += 1

#    return None                overbodig als je geen return statement meegeeft krijg je standaard None

def index_smallest_of(lst, start=0):  # zie HB

    '''

    '''

    # if lst == []:
    if (start >= len(lst)) or (start < 0):
        return None

    smallest_index = start
    current_index = start + 1
#    start = start + 1              kan ook current_index overal vervangen door start



    # while current_index < len(lst):                             # probeer de min functie op een lijst te gebruiken
    for current_index in range(smallest_index,len(lst)):

        if lst[smallest_index] > lst[current_index]:
            smallest_index = current_index

        current_index += 1

    return smallest_index



## Test for index_smallest_of
assert index_smallest_of((77,-20,-4,100),0) == 1
assert index_smallest_of((-9,4,-20,-20,1,-20,-1),1) == 2
assert index_smallest_of((-300,-20,-4,100),0) == 0
assert index_smallest_of((-80,20,-4,-100),2) == 3
assert index_smallest_of("cbabc",0) == 2
assert index_smallest_of((),0) == None                      # error in if ==> lst == [] veranderen door len(lst) == 0
assert index_smallest_of((1,2,3),3) == None                 # dan komt er een nieuwe error ==> if (start >= len(str)) or (start <0)
assert index_smallest_of((1,2,3),-1) == None



## Tests for selection sort
#Empty list
lst = []
selection_sort(lst)
assert len(lst) == 0

# List with one element
lst = [20]
selection_sort(lst)
assert (len(lst) == 1) and (lst[0] == 20)

# List with several elements
lst = [10,20,-100]
lst2 = lst
selection_sort(lst)
assert (len(lst) == 3) and (lst[0] == -100) and\
       (lst[1] == 10) and (lst[2] == 20)
