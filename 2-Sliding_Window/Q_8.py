"""Given an array of positive integers, nums, and a positive integer, target, find the minimum length of a contiguous subarray
whose sum is greater than or equal to the target. If no such subarray is found, return 0."""


class Solution:
    def min_sub_array_len(self,nums, target:int)->int:
        window_size = float('inf')
        start = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                curr_subarr_size = (i + 1) - start
                window_size = min(window_size, curr_subarr_size)
                sum -= nums[start]
                start += 1

        if window_size != float('inf'):
            return window_size

        return 0


def test_min_subarray():
    sol=Solution()
    assert sol.min_sub_array_len([2,3,1,2,4,3],7)==2
    assert sol.min_sub_array_len([1,4,4],4)==1
    assert sol.min_sub_array_len([1,1,1,1,1,1,1,1],11)==0

if __name__ == '__main__':
    test_min_subarray()