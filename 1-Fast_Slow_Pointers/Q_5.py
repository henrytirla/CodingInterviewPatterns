"""Given an array of positive numbers, nums, such that the values lie in the range
 [1,n], inclusive, and that there are n+1
 numbers in the array, find and return the duplicate number present in nums.
 There is only one repeated number in nums.

 Note: You cannot modify the given array nums.
 You have to solve the problem using only constant extra space.

 constraints: All the integers in nums are unique, except for one integer that will appear more than once.


 """
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast = slow = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

def test_findDuplicate():
    sol=Solution()
    assert sol.findDuplicate([1, 5, 4, 3, 2, 4, 6]) == 4
    assert  sol.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3

if __name__ == '__main__':
    test_findDuplicate()

