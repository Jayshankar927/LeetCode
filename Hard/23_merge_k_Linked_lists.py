'''You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.'''

class ListNode:
    def __init__(self,val,next=None):
        self.val = val 
        self.next = next

def mergeKLists(lists:list):
    if not lists:
        return None
    
    if len(lists) == 1:
        return lists[0]
    
    mid = len(lists)//2

    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])

    return merge(left,right)

def merge(left,right):
    dummy = ListNode(0)
    curr = dummy
    while left and right:
        if left.val < right.val:
            curr.next = left
            left=left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next

    curr.next = left or right

    return dummy.next
        
