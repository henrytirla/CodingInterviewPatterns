"""
Given a string, s, that represents a DNA subsequence, and a number 𝑘
, return all the contiguous subsequences (substrings) of length k
 that occur more than once in the string. The order of the returned subsequences does not matter. If no repeated substring is found, the function should return an empty set.

The DNA sequence is composed of a series of nucleotides abbreviated as
𝐴A, 𝐶C, 𝐺G, and 𝑇T
. For example, 𝐴𝐶𝐺𝐴𝐴𝑇𝑇𝐶𝐶𝐺
ACGAATTCCG
 is a DNA sequence. When studying DNA, it is useful to identify repeated sequences in it.

 """

#CHAT GPT VERY INTUITIVE EXPLANATION ON HOW AND WHY WINDOWS RANGE IS SET
"""The loop for i in range(n - k + 1) ensures that you correctly iterate through all possible contiguous substrings of length k within the given string word. Here's an intuitive explanation with an example:

Explanation:
Given a string word of length n and a desired substring length k:

If you start at index i and want a substring of length k, it will end at index i + k - 1.
You need to ensure that the substring does not exceed the length of the word.
Thus, the loop range n - k + 1 ensures that the starting index i only goes up to the point where the substring can still be of length k.

Example:
Consider word = "abcdefg" and k = 3.

Length of word (n) is 7.
You want all substrings of length 3.
The possible substrings of length 3 are:

Start at index 0: "abc"
Start at index 1: "bcd"
Start at index 2: "cde"
Start at index 3: "def"
Start at index 4: "efg"
Let's break down the indices:

The first possible start index is 0.
The last possible start index is n - k which is 7 - 3 = 4.
So, the loop needs to run from 0 to 4 (inclusive), which is why we use range(n - k + 1), i.e., range(7 - 3 + 1), or range(5)."""

class Solution:
    def find_repeated_sequences(self,s, k):
        sequence_count = {}
        repeated_sequences = set()

        # Slide over the string and count all k-length subsequences
        for i in range(len(s) - k + 1):
            subsequence = s[i:i + k]
            if subsequence in sequence_count:
                sequence_count[subsequence] += 1
            else:
                sequence_count[subsequence] = 1

            # Check if the subsequence has been seen more than once
            if sequence_count[subsequence] == 2:
                repeated_sequences.add(subsequence)

        return repeated_sequences



def test_repeated_sequences():
    sol=Solution()
    assert sol.find_repeated_sequences("ACGAATTCCG", 2) == {'CG'}
    assert sol.find_repeated_sequences("AGCTGAAAGCTTAGCTG", 5) == {'AGCTG'}
    assert sol.find_repeated_sequences("TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT",10)=={"CCCCCCCTTT","CCCCCCTTTT","CCCCCTTTTT","CCCCTTTTTT","TCCCCCCCTT","TTCCCCCCCT","TTTCCCCCCC","TTTTCCCCCC","TTTTTCCCCC"}


if __name__ == '__main__':
    test_repeated_sequences()