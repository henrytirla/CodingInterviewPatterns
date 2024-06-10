# Template for reversing a linked list

def reverse_linked_list(head):
	prev, curr = None, head
	while curr:
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt
	return prev
