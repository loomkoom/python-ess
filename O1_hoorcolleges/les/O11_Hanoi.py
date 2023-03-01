# recursief
def hanoi(n,source,target,spare):

    """
      Print all basic moves to be done in transferring n
      disks from the given source rod to the given target
      rod, involving the given spare rod to temporarily
      store disks.
      Only one disk can be moved at a time, and no larger
      disk may even be put on top of a smaller disk.

        - Transfer n-1 disks from source to spare via target
        - Move disk from source to target
        - Transfer n-1 disks from spare to target via source
    """

    if n == 1:
        print("move disk from",source,"to",target)
    else:                                               # dim n-1 < n dus veronderstel dat alles conform de regels verloopt
        hanoi(n-1,source,spare,target)
        print("move this from",source,"to",target)
        hanoi(n-1,spare,target,source)

# iteratief
def hanoi(n,source,target,spare):

    """
      Print all basic moves to be done in transferring n
      disks from the given source rod to the given target
      rod, involving the given spare rod to temporarily
      store disks.
      Only one disk can be moved at a time, and no larger
      disk may even be put on top of a smaller disk.

        - Transfer n-1 disks from source to spare via target
        - Move disk from source to target
        - Transfer n-1 disks from spare to target via source
    """

    to_do =[(n,source,target,spare)]

    while len(to_do) > 0:
        current_task = list.pop(to_do,0)
        current_n, current_source, current_target, current_spare = current_task   # variabelen krijgen overeenkomstige waarde va, het tuple

        if current_n == 1:
            print("move disk from",current_source,"to",current_target)
            # pass
        else:
            task1 = (current_n-1,current_source,current_spare,current_target)
            task2 = (1,current_source,current_target,current_spare)
            task3 = (current_n-1,current_spare,current_target,current_source)

            to_do[0:0] = [task1,task2,task3]                                        # invoegen aan het begin van de lijst
            #print(len(to_do))


hanoi(10,"S","T","X")            #  aantal zetten verhoogt met 2^n



# def hanoi(n, source, target, spare,indent=""):
#     """
#       Print all basic moves to be done in transferring n
#       disks from the given source rod to the given target
#       rod, involving the given spare rod to temporarily
#       store disks.
#       Only one disk can be moved at a time, and no larger
#       disk may even be put on top of a smaller disk.
#
#     """
#
#     if n == 1:
#         print(indent,"move disk from", source, "to", target)
#
#     else:  # dim n-1 < n dus veronderstel dat alles conform de regels verloopt
#         print(indent,"move n disks on top of"...)
#         hanoi(n - 1, source, spare, target,indent)
#         indent += "    "
#         print("move this from", source, "to", target)
#         hanoi(n - 1, spare, target, source,indent)
#
# hanoi(3,"S","T","X")
