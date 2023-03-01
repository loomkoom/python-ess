# Experiment 1
def f(lst):
  lst[2] += lst[3]
the_list = [1,2,3,4]
f(the_list)
print(the_list[2])

# Experiment 2
def f(lst):
  a = lst[2]
  a += lst[3]
the_list = [1,2,3,4]
f(the_list)
print(the_list[2])

# Experiment 3
def f(lst):
  other = lst
  other[2] += 20
the_list = [1,2,3,4]
f(the_list)
print(the_list[2])

# Experiment 4
def f(lst):
  other = [10,20,30,40]
  lst = other
the_list = [1,2,3,4]
f(the_list)
print(the_list[2])

# Exam
def f(lst1,lst2):
  lst1, lst2 = lst2, lst1
  lst2[0] = lst1[2]
  lst1 = list(lst2)
  lst1[0] = lst2[2]

list1 = [1,2,3,4]
list2 = [5,6,7,8,9]
f(list1,list2)
print(list1[0]+list2[0])

