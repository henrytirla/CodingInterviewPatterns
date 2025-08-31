
#(Sorted Array Target Sum)

"""You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

Hint1 : If you simulate the problem, it will be O(n^2) which is not efficient.


Hint 2: Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.

Hint 3: How can you calculate the amount of water at each step?



Index:  0 1 2 3 4 5 6 7 8
Height: 1 8 6 2 5 4 8 3 7

Visual representation:
8 |   █     █
7 |   █     █   █
6 |   █ █   █   █
5 |   █ █ █ █   █
4 |   █ █ █ █ █ █
3 |   █ █ █ █ █ █ █
2 |   █ █ █ █ █ █ █
1 | █ █ █ █ █ █ █ █
0 +─┴─┴─┴─┴─┴─┴─┴─┴─
  0 1 2 3 4 5 6 7 8
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0

        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            current_height = min(height[left_pointer], height[right_pointer])
            current_area = width * current_height
            max_area = max(max_area, current_area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area




def test_maxArea():
     sol = Solution()

     # Testcases
     assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
     assert sol.maxArea([1,1]) == 1
     assert sol.maxArea([4,3,2,1,4]) == 16
     assert sol.maxArea([1,2,1]) == 2
     assert sol.maxArea([3,1,2,4])== 9

if __name__ == '__main__':
    test_maxArea()