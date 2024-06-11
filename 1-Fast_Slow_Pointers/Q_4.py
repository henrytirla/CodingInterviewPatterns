"""We are given a circular array of non-zero integers, nums, where each integer represents the number of steps to be taken either forward or backward from its current index. Positive values indicate forward movement, while negative values imply backward movement. When reaching either end of the array, the traversal wraps around to the opposite end.

The input array may contain a cycle, which is a sequence of indexes characterized by the following:

The sequence starts and ends at the same index.
The length of the sequence is at least two.
The loop must be in a single direction, forward or backward.
Note: A cycle in the array does not have to originate at the beginning. It may begin from any point in the array.

Your task is to determine if nums has a cycle. Return TRUE if there is a cycle. Otherwise return FALSE.

"""

class Solution:
    def circular_array_loop(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            slow, fast = i, i
            direction = nums[i] > 0
            while True:
                slow = (slow + nums[slow]) % n
                fast = (fast + nums[fast]) % n
                if (nums[fast] > 0) != direction:
                    break
                fast = (fast + nums[fast]) % n
                if (nums[fast] > 0) != direction:
                    break
                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

        return False


def test_circular_array_loop():
    sol= Solution()
    assert sol.circular_array_loop([1,3,-2,-4,1]) == True
    assert sol.circular_array_loop([2,1,-1,-2]) == False
    assert sol.circular_array_loop([5,4,-2,-1,3]) == False
    assert sol.circular_array_loop([1,2,-3,3,4,7,1]) == True
    assert sol.circular_array_loop([3,3,1,-1,2]) == True

if __name__ == '__main__':
    test_circular_array_loop()