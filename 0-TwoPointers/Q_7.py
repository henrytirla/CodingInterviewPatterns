"""Statement
Write a function that takes a string as input
 and checks whether it can be a valid palindrome
 by removing at most one character from it."""

class Solution:
    def valid_palindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        mismatch_count = 0

        while left < right:
            if s[left]!= s[right]:
                mismatch_count += 1
                if mismatch_count > 1:
                    return False
                if left + 1 < right and s[left] == s[left + 1]:
                    left += 1
                else:
                    right -= 1
            else:
                left += 1
                right -= 1

        return True






def test_valid_palindrome():
    sol = Solution()
    assert sol.valid_palindrome("abbababa") == True
    assert sol.valid_palindrome("RACEACAR") == True
    assert sol.valid_palindrome("madame") == True
    assert sol.valid_palindrome("eeccccbebaeeabebccceea") == False

if __name__ == '__main__':
    test_valid_palindrome()

