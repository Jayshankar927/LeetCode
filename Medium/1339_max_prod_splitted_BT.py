'''Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 10**9 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.'''

def get_subtree_sums(node,subTreeSums):
    if not node:
        return 0
    
    totalSum = node.val
    totalSum += get_subtree_sums(node.left, subTreeSums)
    totalSum += get_subtree_sums(node.right, subTreeSums)
    subTreeSums.append(totalSum)

    return totalSum

def get_max_product(root):
    subTreeSums = list()
    totalSum = get_subtree_sums(root,subTreeSums)

    maxProd = 0

    for s in subTreeSums:
        prod = s * (totalSum - s)
        if prod > maxProd:
            maxProd = prod
        
    return maxProd % 10**9 + 7