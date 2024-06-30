"""Given two strings, s and t, find the minimum window substring in s, which has the following properties:

It is the shortest substring of s that includes all of the characters present in t.

It must contain at least the same frequency of each character as in t.

The order of the characters does not matter here.

Note: If there are multiple valid minimum window substrings, return any one of them."""


class Solution:
    def shortest_substring(self,s:str,t:str):
        pass



def test_shortest_substring():
    sol=Solution()
    assert sol.shortest_substring("ADOBECODEBANC","ABC")=="BANC"


if __name__ == '__main__':
    test_shortest_substring()
