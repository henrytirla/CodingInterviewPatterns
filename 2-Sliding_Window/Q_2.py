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