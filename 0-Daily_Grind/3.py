"""Given a sorted array, create a new array
containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]"""


class Solution:
    def makeSquares(self, arr: list[int]) -> list[int]:
        n = len(arr)
        result = [0] * n  # Create new array
        left = 0
        right = n - 1
        resultIdx = n - 1  # Fill from right to left

        while left <= right:
            leftSquare = arr[left] * arr[left]
            rightSquare = arr[right] * arr[right]

            if leftSquare > rightSquare:
                result[resultIdx] = leftSquare
                left += 1
            else:
                result[resultIdx] = rightSquare
                right -= 1

            resultIdx -= 1

        return result




def test_makeSquares():
    sol = Solution()
    assert sol.makeSquares([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]
    assert sol.makeSquares([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]

if __name__ == '__main__':
    test_makeSquares()

