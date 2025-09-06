"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000



"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)



def test():
    sol = Solution()
    assert sol.intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert sol.intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]
    assert sol.intersection([1, 2, 3], [4, 5, 6]) == []

if __name__ == '__main__':
    test()