'''
        Tijd:  -DEEEL A: 30 min
               - TODO correctheidsbewijs

        geschat: 60 min
'''


# Deel A: functie
# Deel B: correctheid

# VERSIE 1
def merge_adjacent_elements(lst):
    i, deleted = 0, 0

    while i < len(lst) - 1:
        if lst[i] >= 0:
            if lst[i] + lst[i + 1] == 0:
                print(lst[i:i + 2])
                del lst[i:i + 2]
                deleted += 1
                i -= 1
            else:
                lst[i] += lst[i + 1]
                del lst[i + 1]
        elif lst[i] < 0:
            if lst[i] - lst[i + 1] == 0:
                print(lst[i:i + 2])
                del lst[i:i + 2]
                deleted += 1
                i -= 1
            else:
                lst[i] -= lst[i + 1]
                del lst[i + 1]
        i += 1
    print(deleted)
    print(lst)
    return deleted


# VERSIE 2

def merge_adjacent_elements(lst):
    i, deleted_zeros = 0, 0

    while i < len(lst) - 1:
        if lst[i] >= 0:
            lst[i] += lst[i + 1]
        else:
            lst[i] -= lst[i + 1]
        del lst[i + 1]

        if lst[i] == 0:
            del lst[i]
            deleted_zeros += 1
        else:
            i += 1
    print(deleted_zeros)
    print(lst)
    return deleted_zeros


lst = [12, 3, 3, 3, 5, -5, -7, -7, -9, 9, 0, 0, -4, -12, 0]
assert merge_adjacent_elements(lst) == 3
assert lst == [15, 6, -18, 8, 0]


# DEEL B:
# geg:
def nb_opposites(seq):
    current_pos = 0
    nb_opposites_so_far = 0
    while current_pos < len(seq) - 1:
        assert nb_opposites_so_far == nb_opposites(seq[:current_pos])
        if seq[current_pos] + seq[current_pos + 1] == 0:
            nb_opposites_so_far += 1
        current_pos += 2
    return nb_opposites_so_far


lst = [1, -1, 2, -2, 3, -3, 5, 6, 7, -7, 8, 8, 9, 10, -10]
print(nb_opposites(lst))  # 4
# LUS INVARIANT
# aantal tegengestelden is altijd gelijk aan het aantal even posities waarvan de som 0 is:
# nb_opposites_so_far == nb_opposites(seq[:current_pos]

# CORRECTHEIDSBEWIJS
# BASE STEP:
#     current_pos = 0
#     nb_opposites_so_far = 0
#   => 0 = nb_opposites(seq[:0] = 0

# INDUCTION STEP:
#     assume nb_opposites_so_far0 == nb_opposites(seq[:current_pos0]
#     prove  nb_opposites_so_far == nb_opposites(seq[:current_pos]
#
# * seq[current_pos0] + seq[current_pos0 + 1] == 0:
#   ==>   nb_opposites_so_far == nb_opposites_so_far0 + 1 [1]
#         current_pos == current_pos0 + 2                 [2]
#         seq[current_pos0] == -seq[current_pos0+1]       [3]

#          nb_opposites_so_far0 + 1 == nb_opposites(seq[:current_pos0 + 2]             [1][2]
#   since  nb_opposites(seq[:current_pos0 + 2] == nb_opposites(seq[:current_pos0] + 1  [3]
#    ==>   nb_opposites_so_far0 + 1 == nb_opposites(seq[:current_pos0]) + 1
#    <=>   nb_opposites_so_far0     == nb_opposites(seq[:current_pos0])