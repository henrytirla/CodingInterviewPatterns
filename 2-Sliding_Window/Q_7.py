"""Given a string, input_str, return the length of the longest substring without repeating characters.


eg:p,w,w,k,e,w Output_length = 3

"""


class Solution:
    def longest_substring(self, input_str: str) -> int:
        n = len(input_str)
        start = 0
        max_length = 0
        char_index = {}
        for i in range(n):
            if input_str[i] in char_index:
                start = max(start, char_index[input_str[i]] + 1)
            char_index[input_str[i]] = i
            max_length = max(max_length, i - start + 1)
        return max_length


def test_longest_substring():
    sol = Solution()
    assert sol.longest_substring("abcdbea") == 5
    assert sol.longest_substring("aba") == 2
    assert sol.longest_substring("abccabcabcc") == 3
    assert sol.longest_substring("aaaabaaa") == 2
    assert sol.longest_substring("bbbbb") == 1

if __name__ == '__main__':
    test_longest_substring()