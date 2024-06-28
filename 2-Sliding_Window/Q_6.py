"""Given two strings, s and t, find the minimum window substring in s, which has the following properties:

It is the shortest substring of s that includes all of the characters present in t.

It must contain at least the same frequency of each character as in t.

The order of the characters does not matter here.

Note: If there are multiple valid minimum window substrings, return any one of them."""

# def longest_substring(s:str,k:int)->int:
#      n=len(s)
#      start=0
#      count={}
#      max_count=0
#      max_length=0
#      for i in range(n):
#          count[s[i]]= count.get(s[i],0)+1
#          max_count= count[s[i]]
#          if i-start+1 -max_count>k:
#             count[s[start]]=-1
#             start+=1
#          max_length=max(i-start+1,max_count)
#      return max_length
#
#
# print(longest_substring('abab',2))