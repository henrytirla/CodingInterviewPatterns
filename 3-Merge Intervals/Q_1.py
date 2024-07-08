"""We are given an array of closed intervals,
intervals, where each interval has a start time and an end time.
The input array is sorted with respect to the start times of each interval. For example,
intervals = [[1,4],[3,6],[7,9]][ [1,4], [3,6], [7,9] ]
is sorted in terms of start times 1,31, 3, and 77.

Your task is to merge the overlapping intervals
and return a new output array consisting of only the non-overlapping intervals."""

class Solution:
    def merge_intervals(self,intervals):
        merged=[]
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1],interval[1])
        return merged

def test_merge_intervals():
    sol=Solution()
    assert sol.merge_intervals([[1,4],[3,6],[7,9]])==[[1,6],[7,9]]
    assert sol.merge_intervals([[1,4],[2,3],[4,6]])==[[1,6]]
    assert sol.merge_intervals([[1,4],[5,6],[7,9]])==[[1,4],[5,6],[7,9]]
    assert sol.merge_intervals([[1,4],[0,2],[3,5]])==[[1,5]]

if __name__ == '__main__':
    test_merge_intervals()
