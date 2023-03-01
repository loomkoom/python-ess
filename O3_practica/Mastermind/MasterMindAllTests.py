from MasterMindAsked import (ALL_COLORS,
                             get_nb_black_white_matches,
                             create_combination,
                             any_color_in_combination,
                             all_colors_in_combination,
                             is_sublist_of)




# Tests for get_nb_black_white_matches(given, guess)
simple_combination = ["red", "green", "blue", "white"]
assert get_nb_black_white_matches(["white", "red", "red", "blue"], ["white", "white", "white", "white"]) == (1, 0)
assert get_nb_black_white_matches(["white", "red", "red", "blue"], ["white", "red", "red", "red"]) == (3, 0)
assert get_nb_black_white_matches(["orange", "white", "blue", "yellow"], ["yellow", "blue", "white", "orange"]) == (0, 4)
assert get_nb_black_white_matches(["red", "white", "blue", "orange"], ["red", "white", "blue", "orange"]) == (4,0)
assert get_nb_black_white_matches(["blue", "yellow", "yellow", "blue"], ["blue", "yellow", "blue", "yellow"]) == (2, 2)
assert get_nb_black_white_matches(["blue", "yellow", "yellow", "blue"], ["yellow", "blue", "blue", "yellow"]) == (0, 4)
assert get_nb_black_white_matches(["red", "green"], ["green", "green"]) == (1,0)
assert get_nb_black_white_matches(simple_combination, simple_combination) == (4, 0)



# Test for create_combination(nb_elements)
combination = create_combination(6)
assert len(combination) == 6
assert combination[0] in ALL_COLORS
assert combination[3] in ALL_COLORS
assert combination[5] in ALL_COLORS



# Tests for any_color_in_combination(any, given)
simple_combination = ["red", "green", "blue", "white"]
assert any_color_in_combination(["orangered", "periwinkle", "white"], simple_combination)
assert any_color_in_combination(["white"], simple_combination)
assert any_color_in_combination(["purple", "red"], simple_combination)
assert not any_color_in_combination(["re", "gree", "blu", "whit"], simple_combination)
assert not any_color_in_combination([True, True], simple_combination)
assert not any_color_in_combination(["orange"], simple_combination)



# Tests for all_colors_in_combination(colors, given)
simple_combination = ["red", "green", "blue", "white"]
assert all_colors_in_combination(simple_combination, simple_combination)
assert all_colors_in_combination(["red", "red", "red"], ["red"])
assert all_colors_in_combination(["blue", "green"], ["blue", "red", "green"])
assert all_colors_in_combination(["white", "green", "white", "red", "red"], simple_combination)
assert not all_colors_in_combination(["red", "green", "yellow"], simple_combination)
assert not all_colors_in_combination(["orange"], simple_combination)



# Tests for is_sublist_of(sublist, given)
simple_list = [1, 2, 3, 4]
color_list = ["red", "green", "blue"]
for element in simple_list:
    assert is_sublist_of([element], simple_list)
assert not is_sublist_of([5], simple_list)
assert not is_sublist_of([1, 3, 4], simple_list)
assert not is_sublist_of([1, 2, 4], simple_list)
assert is_sublist_of(color_list, color_list)
assert is_sublist_of(["red", "green"], color_list)
assert not is_sublist_of(["red", "green", "blue", "red"], color_list)
assert not is_sublist_of(["white"], color_list)
# A general test that checks that is_sublist_of returns True for
# every possible sublist of a given list
def test_is_sublist_of(test_list):
    for start_slice in range(len(test_list)):
        for end_slice in range(start_slice, (len(test_list)+1)):
            assert is_sublist_of(test_list[start_slice:end_slice], test_list)
test_is_sublist_of(range(10))
