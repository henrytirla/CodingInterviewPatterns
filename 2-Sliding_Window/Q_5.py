"""Given a string s and an integer k, find the length of the longest substring in s, where all characters are identical,
 after replacing, at most, k characters with any other lowercase English character."""

class Solution:

    def longest_repeating_character_replacement(self,s:str, k:int)->int:
        n = len(s)
        max_length = 0
        max_count = 0
        start = 0
        count = {}
        for i in range(n):

            count[s[i]] = count.get(s[i], 0) + 1
            max_count = max(max_count, count[s[i]])
            current_length=i - start + 1

            if (current_length - max_count )> k:
                count[s[start]] -= 1
                start += 1
            max_length = max(max_length, i - start + 1)
        return max_length


def test_longest_repeating_character_replacement():
    sol = Solution()
    assert sol.longest_repeating_character_replacement("ABAB", 2) == 4
    assert sol.longest_repeating_character_replacement("AABABBA", 1) == 4
    assert sol.longest_repeating_character_replacement("AABABBA", 0) == 2
    assert sol.longest_repeating_character_replacement("aaaaa", 2) == 5
    assert sol.longest_repeating_character_replacement("aaaaaaaaaa", 2) == 10




if __name__ == '__main__':
    test_longest_repeating_character_replacement()