"""Given a sentence, reverse the order of its words without affecting the order of letters within the given word.

Constraints:

The sentence contains English uppercase and lowercase letters, digits, and spaces.

The order of the letters within a word is not to be reversed.

input: "Hello World"
output: "World Hello"

"""

import re
class Solution:
    def reverseWords(self, sentence: str) -> str:
        sentence = re.sub(' +', ' ', sentence.strip())

        sentence = list(sentence)
        str_len = len(sentence) - 1

        self.str_rev(sentence, 0, str_len)
        start = 0

        for end in range(0, str_len + 1):
            if end == str_len or sentence[end] == ' ':
                end_idx = end if end == str_len else end - 1
                self.str_rev(sentence, start, end_idx)
                start = end + 1

        return ''.join(sentence)

    def str_rev(self,_str, start_rev, end_rev):
        while start_rev < end_rev:
            _str[start_rev], _str[end_rev] = _str[end_rev], _str[start_rev]
            start_rev += 1
            end_rev -= 1








def test_reverse_words():
    sol=Solution()
    assert sol.reverseWords("Hello World") == "World Hello"
    assert sol.reverseWords("Henry Tirla") == "Tirla Henry"



if __name__ == '__main__':

    test_reverse_words()