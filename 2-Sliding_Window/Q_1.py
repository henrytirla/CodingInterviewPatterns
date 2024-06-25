

"""
Maximum sum subarray of size K: Given an array of integers and a positive integer k,
 find the maximum sum of any contiguous subarray of size k.
 
 array= [4,2,-1,9,7,-3,5]
"""

class Solution:
    def max_sum_subarray(self,array:list,k:int)->int:
        window_sum= sum(array[:k])
        max_sum = window_sum
        for i in range(len(array)-k):
            window_sum= window_sum-array[i]+ array[i+k]
            max_sum = max(max_sum,window_sum)
        return max_sum






def test_Max_subarray():
    sol=Solution()

    assert sol.max_sum_subarray([4,2,-1,9,7,-3,5],4) == 18
    assert sol.max_sum_subarray([4,2,-2,0,9,0,2],4)!=4


if __name__ == '__main__':
    test_Max_subarray()







