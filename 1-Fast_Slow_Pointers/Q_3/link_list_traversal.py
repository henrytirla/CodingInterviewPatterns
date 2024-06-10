# Template for traversing a linked list

def traverse_linked_list(head):
    current, nxt = head, None
    while current:
      nxt = current.next
      current = nxt