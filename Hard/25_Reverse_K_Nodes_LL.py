'''Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.'''

def reverseKGroups(head,k):
    curr=head
    for _ in range(k):
        if not curr:
            return head
        curr=curr.next
    
    prev = None
    curr=head

    for _ in range(k):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    head.next = reverseKGroups(curr,k)

    return prev