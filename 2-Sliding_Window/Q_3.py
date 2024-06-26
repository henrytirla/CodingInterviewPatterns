"""Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) of size w.

Example: nums =[-4,2,-5,3,6]
         Window size = 3
         output= [2,3,6]
"""

class Solution:
    def find_max_slidding_window(self,nums:list,w:int)->list:

        if not nums: #taking care of edge cases
            return []
        if w==1:
            return nums
        max_values = []
        for i in range(len(nums)-w+1):
            max_values.append(max(nums[i:i+w]))
        return max_values

def test_max_slidding_window():
    sol=Solution()
    assert sol.find_max_slidding_window([-4,2,-5,3,6],3) == [2,3,6]
    assert sol.find_max_slidding_window([1,2,3,4,5,6,7,8,9],3) == [3,4,5,6,7,8,9]

if __name__ == '__main__':
    test_max_slidding_window()
