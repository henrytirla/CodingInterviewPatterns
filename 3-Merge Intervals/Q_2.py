"""Given a sorted list of nonoverlapping intervals
and a new interval, your task is to insert the new interval
into the correct position while ensuring that the resulting
 list of intervals remains sorted and nonoverlapping.
 Each interval is a pair of nonnegative numbers,
the first being the start time and the second being the end time of the interval."""

class Solution:

    def insert_interval(self,existing_intervals, new_interval):
        output_list = []
        inserted= False

        for inputs in existing_intervals:
            if inputs[1] < new_interval[0]: #This condition checks if the current interval ends before the new interval starts.
                output_list.append(inputs)
            elif inputs[0] > new_interval[1]: #This condition checks if the current interval starts after the new interval ends.
                 if not inserted:
                     output_list.append(new_interval)
                     inserted = True
                 output_list.append(inputs)
            else:
                new_interval[0]= min(inputs[0],new_interval[0])
                new_interval[1]= max(inputs[1],new_interval[1])
        if not inserted:
            output_list.append(new_interval)

        return output_list


def test_insert_interval():
    sol = Solution()
    assert sol.insert_interval([[1,2],[3,4],[5,8],[9,15]], [2, 5]) == [[1,8],[9,15]]
    assert sol.insert_interval([[1,2],[3,4],[5,8],[9,15]], [2, 6]) == [[1,8],[9,15]]
    assert sol.insert_interval([[1,2],[3,4],[5,8],[9,15]], [2, 7]) == [[1,8],[9,15]]

if __name__ == '__main__':
    test_insert_interval()