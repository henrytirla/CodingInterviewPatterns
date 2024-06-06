"""Check whether or not a linked list contains a cycle. If a cycle exists, return TRUE. Otherwise, return FALSE.
The cycle means that at least one
 node can be reached again by traversing the next pointer."""

from linked_list import LinkedList
class Solution:
    def has_cycle(self, head: LinkedList) -> bool:
        if head is None:
            return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False




def test_has_cycle():
    sol = Solution()
    input_linked_list = LinkedList()
    # Case 1: Create a cycle in the linked list
    head = input_linked_list.create_linked_list([2, 4, 6, 8, 10, 12])
    head.next.next.next.next.next.next = head.next.next  # Creating a cycle
    assert sol.has_cycle(head) == True


    """This line of code manually creates a cycle in the linked list. Here's how it works:

        head points to the node with value 2.
        head.next points to the node with value 4.
        head.next.next points to the node with value 6.
        head.next.next.next points to the node with value 8.
        head.next.next.next.next points to the node with value 10.
        head.next.next.next.next.next points to the node with value 12.
        head.next.next.next.next.next.next should normally be None (end of the list).
        By setting head.next.next.next.next.next.next = head.next.next, you are making the next pointer of the node with value 12 point to the node with value 6.
        
        2 -> 4 -> 6 -> 8 -> 10 -> 12
              ^               |
              |---------------|


"""

    # Case 2: No cycle in the linked list
    input_linked_list = LinkedList()
    head = input_linked_list.create_linked_list([1, 3, 5, 7, 9, 11])
    assert sol.has_cycle(head) == False

    #Case 3:

    input_linked_list = LinkedList()
    head = input_linked_list.create_linked_list([0, 1, 2, 3, 4, 6])
    head.next.next.next.next.next.next = head.next
    assert sol.has_cycle(head) == True






if __name__ == '__main__':
    test_has_cycle()


