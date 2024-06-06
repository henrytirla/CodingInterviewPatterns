""" Given a singly linked list, remove the 𝑛𝑡ℎn th

 node from the end of the list and return its head.  """


class Solution:
    def removeNthFromEnd(self, head: list, n: int) -> list:
       left=0
       right=n
       end=len(head)-1
       while right<=end:
           left+=1
           right+=1
           if right==end:
               head.pop(left+1)
               return head







def test_remove_nth_from_end():
    sol=Solution()
    assert sol.removeNthFromEnd([23,28,10,5,67,39,70,28], 2) == [23,28,10,5,67,39,28]
    assert sol.removeNthFromEnd([34,53,6,95,38,28,17,63,16,76], 3) == [34,53,6,95,38,28,17,16,76]
    assert sol.removeNthFromEnd([288,224,275,390,4,383,330,60,193], 4) == [288,224,275,390,4,330,60,193]
    assert sol.removeNthFromEnd([1,2,3,4,5,6,7,8,9], 1) == [1,2,3,4,5,6,7,8]


if __name__ == '__main__':
    test_remove_nth_from_end()