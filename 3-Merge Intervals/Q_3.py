"""For two lists of closed intervals given as input, interval_list_a and interval_list_b,
where each interval has its own start and end time,
 write a function that returns the intersection of the two interval lists.

For example, the intersection of [3,8] and [5,10] is [5,8]
."""

class Solution:
    def interval_intersection(self,interval_list_a, interval_list_b):
        output_list = []
        i = 0
        j = 0
        while i < len(interval_list_a) and j < len(interval_list_b):
            start = max(interval_list_a[i][0], interval_list_b[j][0])
            end = min(interval_list_a[i][1], interval_list_b[j][1])
            if start <= end:
                output_list.append([start, end])
            if interval_list_a[i][1] < interval_list_b[j][1]:
                i += 1
            else:
                j += 1
        return output_list

def test_interval_intersection():
    sol = Solution()
    assert sol.interval_intersection([[1,4],[5,6],[7,8],[9,15]], [[2,4],[5,7],[9,15]]) == [[2,4],[5,6],[7,7],[9,15]]
    assert sol.interval_intersection([[1,4],[5,6],[7,8],[9,15]], [[2,4],[5,7],[9,15]]) == [[2,4],[5,6],[7,7],[9,15]]
    assert sol.interval_intersection([[1,3],[4,6],[8,10],[11,15]] , [[2,3],[10,15]]) == [[2,3],[10,10],[11,15]]



if __name__ == '__main__':
    test_interval_intersection()