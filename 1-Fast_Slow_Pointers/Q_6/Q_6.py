"""Given the head of a linked list, your task is to check whether the linked list is a palindrome or not.
Return TRUE if the linked list is a palindrome; otherwise, return FALSE."""

from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list
class Solution:


    def palindrome(self,head):
        # Replace this placeholder return statement with your code
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = reverse_linked_list(slow)
        fast = head
        while slow:
            if slow.data != fast.data:
                return False
            slow = slow.next
            fast = fast.next
        return True

def test_palindrome():
    sol= Solution()
    input_linked_list = LinkedList()
    head1 = input_linked_list.create_linked_list([3,4,5,6,5,4,3])
    assert sol.palindrome(head1) == True

    input_linked_list2 = LinkedList()
    head2 = input_linked_list2.create_linked_list([1, 2, 3, 4, 5])
    assert sol.palindrome(head2) == False

if __name__ == '__main__':
    test_palindrome()