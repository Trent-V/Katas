import codewars_test as test
import RangeExtraction

test.describe("Sample Test Cases")

test.it("Simple Tests")
test.assert_equals(RangeExtraction.solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
test.assert_equals(RangeExtraction.solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')