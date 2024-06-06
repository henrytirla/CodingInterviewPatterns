"""Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

Note: A valid triplet consists of elements with distinct indexes. This means, for the triplet nums[i], nums[j], and nums[k], i
≠=j, i ≠=k and j ≠=k.
ie nums [3,7,1,2,8,4,5] target = 20

"""
class Solution:
    def threeSum(self, nums: list, target: int) -> bool:
        nums.sort()
        for i in range(len(nums)-2):
            left = i +1
            right = len(nums) -1
            while left < right:
                currentSum =nums[i] + nums[left] + nums[right]
                if currentSum == target:
                    return True
                elif currentSum < target:
                    left += 1
                else :
                    right -= 1
        return False








def test_three_sum():
    sol=Solution()
    assert sol.threeSum([3,7,1,2,8,4,5], 20) == True
    assert sol.threeSum([3,7,1,2,8,4,5], 55) == False



if __name__ == '__main__':
    test_three_sum()


