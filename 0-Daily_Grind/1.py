""" Given an array of integers, return the indices of the two numbers
in it that add up to a specific "goal" number.

Suppose we had an array [1, 3, 6, 7, 9], and let's say our "goal" number was 10.
Our numbers to sum to it could be 3 and 7,
and we would return an array of indices 1 and 3 respectively."""

#(Sorted Array Target Sum)

class Solution:
    def twoNumberSum(self,arr,targetSum:int):
        seen={}
        for i , num in enumerate(arr):
            complement = targetSum - num
            if complement in seen:
                return (arr[complement], arr[num])
            seen[num]=i
        return []






def test_two_number_sum():
    sol=Solution()
    assert sol.twoNumberSum([1, 3, 6, 7, 11], 10) == (3, 7)
    assert sol.twoNumberSum([3,2,4], 6) == (2,4)
    assert sol.twoNumberSum([2, 7, 11, 15], 9) == (2, 7)
    assert sol.twoNumberSum([2, 3, 5,7,11, 13], 14) == (3, 11)
    assert sol.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 20) == []

if __name__ == '__main__':
    test_two_number_sum()

