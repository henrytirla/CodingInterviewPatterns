"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums


def test():
    sol = Solution()
    assert sol.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sol.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert sol.sortedSquares([-5, -3, -2, -1]) == [1, 4, 9, 25]


if __name__ == '__main__':
    test()