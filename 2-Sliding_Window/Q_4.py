"""Given two strings, str1 and str2,find the shortest substring in str1 such that str2 is a subsequence of that substring.
 A substring is defined as a contiguous sequence of characters within a string.
  A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.
   Let’s say you have the following two strings: str1 = “abbcb ” str2 = “ ac ” In this example, “ abbc ”
   is a substring of str1, from which we can derive str2 simply by deleting both the instances of the character  b .
   Therefore, str2 is a subsequence of this substring.
   Since this substring is the shortest among all the substrings in which str2 is present as a subsequence,
   the function should return this substring, that is, “abbc ”.
    If there is no substring in str1 that covers all characters in str2, return an empty string.
    If there are multiple minimum-length substrings that meet the subsequence requirement, return the one with the left-most starting index."""


class Solution:
    def find_min_subsequence(self,str1:str,str2:str)->str:
        n = len(str1)
        m = len(str2)
        min_length = float("inf")
        min_substring = ""
        for i in range(n):
            subseq_index = 0
            for j in range(i, n):
                if str1[j] == str2[subseq_index]:
                    subseq_index += 1
                    if subseq_index == m:
                        if (j - i + 1) < min_length:
                            min_length = j - i + 1
                            min_substring = str1[i:j + 1]
                        break

        return min_substring

def test_min_subsequence():
    sol=Solution()
    assert sol.find_min_subsequence("abbcb","ac")=="abbc"
    assert sol.find_min_subsequence("abcdebdde","bde")=="bcde"
    assert sol.find_min_subsequence("fgrqsqsnodwmxzkzxwqegkndaa","kzed")=="kzxwqegknd"
    assert sol.find_min_subsequence("michmznaitnjdnjkdsnmichmznait","michmznait")=="michmznait"


if __name__ == '__main__':

    test_min_subsequence()