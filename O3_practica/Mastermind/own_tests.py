from MasterMindAsked import  (ALL_COLORS,
                             get_nb_black_white_matches,
                             create_combination,
                             any_color_in_combination,
                             all_colors_in_combination,
                             is_sublist_of)



''' Testen
1. geen matchen
'''

# Tests for get_nb_black_white_matches(given, guess)
assert get_nb_black_white_matches(["blue", "yellow", "yellow", "blue"], ["blue", "yellow", "blue", "yellow"]) == (2, 2)
assert get_nb_black_white_matches(['white','green'],['red','red']) == (0,0)
assert get_nb_black_white_matches(['yellow', 'yellow'],['yellow', 'green']) == (1,0)
assert get_nb_black_white_matches(['yellow', 'yellow'],['yellow', 'green']) == (1,0)
assert get_nb_black_white_matches(['yellow', 'yellow'],['green', 'yellow']) == (1,0)
assert get_nb_black_white_matches(['yellow', 'yellow','green','yellow'],['yellow', 'green']) == (1,1)
assert get_nb_black_white_matches(['gr', 'ye','ge','ro'],['gr', 'gr','gr','gr']) == (1,0)
assert get_nb_black_white_matches(['gr', 'gr','ge','ro'],['gr', 'gr','gr','gr']) == (2,0)
assert get_nb_black_white_matches(['gr', 'gr','gr','gr'],['bl', 'ge','ye','gr']) == (1,0)
assert get_nb_black_white_matches(['gr', 'gr','gr','gr'],['bl', 'gr','ye','gr']) == (2,0)
assert get_nb_black_white_matches(['gr', 'gr','gr','gr'],['gr', 'gr','ye','gr']) == (3,0)
assert get_nb_black_white_matches(['gr', 'gr','gr','gr'],['gr', 'gr','gr','gr']) == (4,0)
assert get_nb_black_white_matches(['gr', 'ge','gr','ge'],['ge', 'gr','ge','gr']) == (0,4)
assert get_nb_black_white_matches(['gr', 'bl','gr','bl'],['ge', 'gr','ge','gr']) == (0,2)
assert get_nb_black_white_matches(['gr', 'bl','gr','gr'],['bl', 'gr','gr','gr']) == (2,2)

assert get_nb_black_white_matches(['gr', 'ge','gr','ro'],['gr', 'gr','gr','gr']) == (2,0)
assert get_nb_black_white_matches(['bl', 'ge','ye','gr'],['gr', 'gr','gr','gr']) == (1,0)
assert get_nb_black_white_matches(['blue', 'blue', 'red', 'green'],['blue', 'blue','blue','blue']) == (2,0)