'''Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head):
        stack = []
        
        temp=head
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        
        stack.sort(reverse=True)
        
        temp=head
        while temp is not None:
            temp.val = stack.pop()
            temp = temp.next
        
        return head