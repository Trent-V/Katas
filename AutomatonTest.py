import codewars_test as test
from Automaton import Automaton

my_automaton = Automaton()

test.assert_equals(my_automaton.read_commands(["1"]), True)
test.assert_equals(my_automaton.read_commands(["1","0"]), False)
test.assert_equals(my_automaton.read_commands(["1", "0", "0", "1"]), True)