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

        nums.sort()
        minimum_distance=float('inf')
        closest_sum=0

        for i in range(len(nums)-2):
            k= i+1
            n=len(nums)-1
            while k<n:
                current_sum= nums[i] + nums[k] +nums[n]
                current_distance= abs(current_sum-target)

                # If this sum is closer to target, update our best

                if current_distance< minimum_distance:
                   minimum_distance= current_distance
                   closest_sum=current_sum
                if current_distance==0:
                    return current_sum

                if current_sum < target:
                    k+=1
                else:
                    n-=1
        return closest_sum






def test_threeSumClosest():
    sol = Solution()
    # Test 1: Basic example from problem statement
    assert sol.threeSumClosest([-1, 2, 1, -4], 1) == 2, "Basic case from example"

    # Test 2: Exact match exists
    assert sol.threeSumClosest([0, 0, 0], 1) == 0, "Exact match with zeros"

    # Test 3: All positive numbers
    assert sol.threeSumClosest([1, 2, 3, 4, 5], 10) == 10, "All positive numbers"

    # Test 4: All negative numbers
    assert sol.threeSumClosest([-5, -3, -1, -2, -4], -6) == -6, "All negative numbers"

    # Test 5: Mix of positive and negative, target negative
    assert sol.threeSumClosest([-1, 0, 1, 1, 55], -3) == 0, "Mixed numbers, negative target"

    # Test 6: Minimum array size (3 elements)
    assert sol.threeSumClosest([1, 2, 3], 6) == 6, "Minimum size array with exact match"

    # Test 7: Large target value
    assert sol.threeSumClosest([1, 1, 1, 0], 100) == 3, "Large target, small numbers"

    # Test 8: Duplicates creating multiple same sums
    assert sol.threeSumClosest([0, 1, 2, 0, 1, 2], 3) == 3, "Array with duplicates"

    # Test 9: Target exactly between two possible sums
    assert sol.threeSumClosest([-1, 2, 1, -4], 0) == -1, "Target between possible sums"

    # Test 10: Large array with various distances
    assert sol.threeSumClosest([1, 1, -1, -1, 3, 5, 8, 2], 4) == 4, "Larger array multiple options"


if __name__ == '__main__':
    test_threeSumClosest()