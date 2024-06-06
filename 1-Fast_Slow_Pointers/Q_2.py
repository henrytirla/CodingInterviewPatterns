"""Check whether or not a linked list contains a cycle. If a cycle exists, return TRUE. Otherwise, return FALSE.
The cycle means that at least one
 node can be reached again by traversing the next pointer."""


class Solution:
    def has_cycle(self, head: list) -> bool:
        pass



def test_has_cycle():
    sol = Solution()
    assert sol.has_cycle([3,2,0,-4]) == True
    assert sol.has_cycle([1,2]) == True
    assert sol.has_cycle([1]) == False
    assert sol.has_cycle([1,2,3]) == False


if __name__ == '__main__':
    test_has_cycle()


