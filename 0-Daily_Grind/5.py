"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]

such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105"""

#(Sorted Array Target Sum)

class Solution:
    def Sumthree(self, arr: list[int]):
        arr.sort()
        result = []
        for k in range(len(arr) - 2):
            # Skip duplicate fixed elements
            if k > 0 and arr[k] == arr[k - 1]:
                continue

            i = k + 1
            j = len(arr) - 1

            while i < j:
                currentSum = arr[k] + arr[i] + arr[j]

                if currentSum == 0:
                    result.append([arr[k], arr[i], arr[j]])

                    # Skip duplicate left values
                    if arr[i] == arr[i + 1]:
                        i += 1
                    # Skip duplicate right values
                    if arr[j] == arr[j - 1]:
                        j -= 1

                    i += 1
                    j -= 1

                elif currentSum < 0:
                    i += 1
                else:
                    j -= 1

        return result






def   test_Sumthree():
    sol = Solution()


    # Test 1: Basic case with multiple triplets
    assert sol.Sumthree([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

    # Test 2: Array with duplicates
    assert sol.Sumthree([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]

    # Test 3: All zeros
    assert sol.Sumthree([0, 0, 0]) == [[0, 0, 0]]

    # Test 4: No valid triplets
    assert sol.Sumthree([1, 2, 3]) == []

    # Test 5: Minimum length array with solution
    assert sol.Sumthree([-1, 0, 1]) == [[-1, 0, 1]]

    # Test 6: Minimum length array with no solution
    assert sol.Sumthree([1, 2, 3]) == []

    # Test 7: Array with many duplicates
    assert sol.Sumthree([-1, -1, -1, 0, 1, 2]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol.Sumthree([-2,0,0,2,2]) == [[-2,0,2]]

    # Test 8: Large numbers
    assert sol.Sumthree([-4, -2, -1, 0, 3, 5]) == [[-4, -1, 5], [-2, -1, 3]]

    # Test 9: Mix of positive and negative with duplicates
    assert sol.Sumthree([-2, -1, -1, 1, 1, 2, 2]) == [[-2, 1, 1], [-1, -1, 2]]

    # Test 10: Array with four zeros
    assert sol.Sumthree([0, 0, 0, 0]) == [[0, 0, 0]]


if __name__ == '__main__':
    test_Sumthree()
