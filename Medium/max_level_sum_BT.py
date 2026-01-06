#Maximum level sum of a binary tree
# I used BFS to traverse every level of the tree and calculate sum and update maxsum

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def buildBTree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr.pop(0))
    i=1
    queue = deque([root])

    while i<len(arr):

        parent = queue.popleft()

        if i<len(arr) and arr[i] is not None:
            left_val = arr[i]
            parent.left = TreeNode(left_val)
            queue.append(parent.left)
        i+=1
        
        if i<len(arr) and arr[i] is not None:
            right_val = arr[i]
            parent.right = TreeNode(right_val)
            queue.append(parent.right)
        i+=1
    
    return root


def MaxSumBinaryTree(root):
    if not root:
        return 0
    
    q = deque([root])
    level=1
    bestlevel = 1
    maxsum = float('-inf')

    while q:
        levelsum = 0
        
        for _ in range(len(q)):
            node = q.popleft()
            levelsum += node.val

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
            
        if levelsum > maxsum:
            maxsum = levelsum
            bestlevel = level

        level += 1
    
    return bestlevel


arr = [989,None,10250,98693,-89388,None,None,None,-32127]
root = buildBTree(arr)

print(MaxSumBinaryTree(root))