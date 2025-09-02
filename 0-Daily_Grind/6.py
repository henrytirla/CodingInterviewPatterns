"""Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104"""

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
       pass




def test_threeSumClosest():
    sol = Solution()
    assert sol.threeSumClosest([-1,2,1,-4], 1) == 2
    assert sol.threeSumClosest([0,0,0], 1) == 0


if __name__ == '__main__':
    test_threeSumClosest()