"""Given the head of a singly linked list, return the middle node of the linked list. If the number of nodes in the linked list is even,
there will be two middle nodes, so return the second one."""
from linked_list import LinkedList

class Solution:
    def middleNode(self, head: LinkedList) -> LinkedList:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def test_middle_node():
    sol = Solution()

    input_linked_list = LinkedList()

    # Case 1: Even number of nodes in the linked list
    head1 = input_linked_list.create_linked_list([1, 2, 3, 4, 5, 6])
    assert sol.middleNode(head1).data == 4

    # Case 2: Odd number of nodes in the linked list
    input_linked_list2 = LinkedList()
    head2 = input_linked_list2.create_linked_list([1, 2, 3, 4, 5])
    assert sol.middleNode(head2).data == 3

    #Case 3
    input_linked_list3 = LinkedList()
    head2 = input_linked_list3.create_linked_list([1, 2, 3, 4,5,6,7])
    assert sol.middleNode(head2).data == 4

if __name__ == '__main__':
    test_middle_node()