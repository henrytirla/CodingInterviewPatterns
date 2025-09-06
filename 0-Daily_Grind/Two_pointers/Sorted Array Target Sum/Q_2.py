"""Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;
after removing the duplicates in-place return the new length of the array."""

#(Sorted Array Target Sum)


class Solution:
    def removeDuplicates(self, arr: list[int]) -> int:
        # Optimal Approach O(n) Time Complexity and O(1) Space Complexity
        if len(arr)==0:
            return 0
        left_pointer=0

        for right_pointer in range(1,len(arr)):
            if arr[left_pointer] != arr[right_pointer]:
                left_pointer += 1
                arr[left_pointer] = arr[right_pointer]
        return left_pointer + 1



def test_removeDuplicates():
    sol=Solution()
    assert sol.removeDuplicates([2,3,3,3,6,9,9]) == 4
    assert sol.removeDuplicates([2,2,2,11]) == 2
    assert sol.removeDuplicates([]) == 0



if __name__ == '__main__':
    test_removeDuplicates()


