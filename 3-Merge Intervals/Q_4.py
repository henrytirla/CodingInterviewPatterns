"""You’re given a list containing the schedules of multiple employees. Each person’s schedule is a list of non-overlapping intervals in sorted order.
An interval is specified with the start and end time, both being positive integers.
Your task is to find the list of finite intervals representing the free time for all the employees."""

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")"


class Solution:
    def free_time(self, schedule):
        intervals = sorted([interval for s in schedule for interval in s], key=lambda x: x.start)

        ans = []
        end = intervals[0].end
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start > end:
                ans.append(Interval(end, interval.start))
            end = max(end, interval.end)
        return ans


def test_free_time():
    sol = Solution()
    free_times = sol.free_time([[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]])
    assert [str(interval) for interval in free_times] == ["[5, 6]", "[7, 9]"]
    testcase2=sol.free_time([[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]])
    assert [str(interval) for interval in testcase2] == ["[3, 4]"]


if __name__ == '__main__':
    test_free_time()


