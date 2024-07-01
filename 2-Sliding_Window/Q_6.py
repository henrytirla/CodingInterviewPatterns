"""Given two strings, s and t, find the minimum window substring in s, which has the following properties:

It is the shortest substring of s that includes all of the characters present in t.

It must contain at least the same frequency of each character as in t.

The order of the characters does not matter here.

Note: If there are multiple valid minimum window substrings, return any one of them."""

from collections import Counter
class Solution:
    def min_windows(self,s:str,t:str):
        if not s or not t or len(s)<len(t):
            return ""

        frequeny_t = Counter(t)
        required_chars= len(frequeny_t)
        formed=0
        left,right=0,0
        window_counts={}
        min_length=float("inf")
        min_window=""
        while right<len(s):
            char = s[right]
            window_counts[char]=window_counts.get(char,0)+1
            if char in frequeny_t and window_counts[char]==frequeny_t[char]:
                formed+=1
            while left<=right and formed==required_chars:
                char = s[left]
                current_length=right-left+1
                if current_length<min_length:
                    min_length=current_length
                    min_window=s[left:right+1]
                window_counts[char]-=1
                if char in frequeny_t and window_counts[char]<frequeny_t[char]:
                    formed-=1
                left+=1
            right+=1
        return min_window






def test_min_windows():
    sol=Solution()
    assert sol.min_windows("ADOBECODEBANC","ABC")=="BANC"
    assert sol.min_windows("ABXYZJKLSNFC","ABC")=="ABXYZJKLSNFC"



if __name__ == '__main__':
    test_min_windows()
