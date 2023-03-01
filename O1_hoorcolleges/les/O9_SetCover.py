def cover_set(sets,universe):

    """
        Return a cover for the given universe involving
        sets of the given set of sets.
        - The returned cover is kept as small as possible
          without a guarantee that it is the smallest
          possible cover.
    """

    cover_so_far = set()
#    universe = set(universe)
    universe = set.copy(universe)               # lokale copy opdat de originele set ongewijzigd blijft
    sets = set.copy(sets)

    while len(universe) > 0:

        best_set_to_add = largest_common_set(sets,universe)
        set.add(cover_so_far,best_set_to_add)               # voeg beste set toe aan de huidige cover
        set.remove(sets,best_set_to_add)                    # verwijder uit de sets
        universe -= best_set_to_add                         # verwijder uit universe

    return cover_so_far

def largest_common_set(sets,universe):

    """
        Return the smallest set in the given set of sets
        that has the most elements in common with the given
        universe.
        - No other set in the set of sets has more elements
          in common with the universe, and sets that have an
          equal number of elements in common with the
          universe have at least as many elements as the
          returned set.
    """

    best_set_so_far = set()
    nb_best_commons = 0

    for sett in sets:

        nb_common_elements = len(sett & universe)             #lengte van de verzameling v/d doorsnede

        if nb_common_elements > nb_best_commons or (nb_common_elements == nb_best_commons and len(sett) < len(best_set_so_far)):
            best_set_so_far = sett
            nb_best_commons = nb_common_elements

    return best_set_so_far



assert largest_common_set({ frozenset((1,2,5,6)),frozenset((6,7,9)),frozenset((1,10,8)), frozenset() },{1,2,3,4,5,6,7,8,9})== {1,2,5,6}
assert largest_common_set({ frozenset((1,2,3)),frozenset((4,5,6,10)) },{1,2,3,4,5,6,7,8,9})== {1,2,3}
assert largest_common_set({ frozenset((1,2,5,6)),frozenset((6,7,9)), frozenset((1,10,8)), frozenset() },{"a","b","c"}) == set()


assert cover_set({ frozenset((1,2,3,4,5,6)),frozenset((6,7,9)),frozenset((1,10,8)), frozenset(("a","b","c")) },{1,2,3,4,5,6,7,8,9}) == { frozenset((1,2,3,4,5,6)),frozenset((6,7,9)),frozenset((1,10,8)) }
assert cover_set({ frozenset((1,2,3,4,5,6)) },set((1,2,3,4)))== { frozenset((1,2,3,4,5,6)) }
assert cover_set({ frozenset((1,2,3,4,5,6)),frozenset((6,7,9)), frozenset((1,10,8)), frozenset(("a","b","c")) }, set()) == set()
assert cover_set(set(),set()) == set()

