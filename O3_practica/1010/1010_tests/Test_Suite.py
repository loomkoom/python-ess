# Execute this program to test your code.
# - Start with working out the functions in the module Position,
#   followed by those of Disk, Board and Drop7 in that order.
# - Comment out all the tests of functions that you have not worked
#   out.
# - The final score you get from this collection of tests is integrated
#   in the final score for this "practicum".


import Position_Test
import Block_Test
import Board_Test
import Game_Test

import multiprocessing


def run_tests(test_functions):
    if __name__ == '__main__':

        max_score = multiprocessing.Value("i", 0)
        score = multiprocessing.Value("i", 0)
        failed_tests = []

        for test_function in test_functions:

            old_score = score.value
            old_max_score = max_score.value

            # Start test as a process
            test = multiprocessing.Process \
                (target=test_function, name=test_function.__name__, args=(score, max_score))
            test.start()

            # Terminate test
            test.join(70)

            if test.is_alive():
                failed_tests.append("Timed out --> " + test_function.__doc__)
            elif score.value - old_score != max_score.value - old_max_score:
                failed_tests.append("Failed --> " + test_function.__doc__)

        return (score.value, max_score.value, failed_tests)


if __name__ == '__main__':
    test_functions = \
        set.union(
            Position_Test.position_test_functions,
            Block_Test.block_test_functions,
            Board_Test.board_test_functions,
            Game_Test.game_test_functions
        )

    (score, max_score, failed_tests) = run_tests(test_functions)

    print("Score: ", score, "/", max_score, end="")
    print(" (", score * 100 // max_score, "%)")
    if len(failed_tests) > 0:
        print()
        print("Details")
        for failed_test in failed_tests:
            print("   ", failed_test)
