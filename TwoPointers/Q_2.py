"""Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.

Note: A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward.

Constraints:
the string s will not contain any white space and will only consist of ASCII characters(digits and letters)."""
class Solution:
    def palindrome(self,s:str):
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True





def test_palindrome():
    sol=Solution()
    assert sol.palindrome("kayak") == True
    assert sol.palindrome("ABCDABCD") == False
    assert sol.palindrome("RaCEACAR") == False
    assert sol.palindrome("RACECAR") == True
    assert sol.palindrome("hello") == False



if __name__ == '__main__':
    test_palindrome()


nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == target:
                    return True
                elif currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
        return False