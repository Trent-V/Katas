import codewars_test as test
import SnailTrail

def testSnail():
        array = [[1,2,3],
                [4,5,6],
                [7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        test.assert_equals( expected, SnailTrail.snail(array))


        array = [[1,2,3],
                [8,9,4],
                [7,6,5]]
        expected = [1,2,3,4,5,6,7,8,9]
        test.assert_equals(expected, SnailTrail.snail(array))

if __name__ == "__main__":
    testSnail()