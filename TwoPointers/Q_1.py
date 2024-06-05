import pytest
""" Given an array of integers, return the indices of the two numbers 
in it that add up to a specific "goal" number.

Suppose we had an array [1, 3, 6, 7, 9], and let's say our "goal" number was 10. 
Our numbers to sum to it could be 3 and 7, 
and we would return an array of indices 1 and 3 respectively."""



# arr = [1, 3, 6, 7, 10]
# targetSum = 10

class Solution:
    def twoNumberSum(self,arr:list,targetSum:int):
        sortedArr = sorted(arr)
        left = 0
        right = len(arr) - 1
        while left < right:
            currentSum = sortedArr[left] + sortedArr[right]
            if currentSum == targetSum:
                return sortedArr[left], sortedArr[right]
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
        return []



def test_two_number_sum():
    sol=Solution()
    assert sol.twoNumberSum([1, 3, 6, 7, 11], 10) == (3, 7)
    assert sol.twoNumberSum([2, 7, 11, 15], 9) == (2, 7)
    assert sol.twoNumberSum([2, 3, 5,7,11, 13], 14) == (3, 11)
    assert sol.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 20) == []


if __name__ == '__main__':
    test_two_number_sum()






