'''There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.

You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.

Example 1:
Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]
Output: 1
Explanation:
A square with side length 1 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 1. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.

Example 2:
Input: bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]
Output: 4
Explanation:
A square with side length 2 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 2 * 2 = 4. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.

Example 3: 
Input: bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]
Output: 1
Explanation:
A square with side length 1 can fit inside the intersecting region of any two rectangles. Also, no larger square can, so the maximum area is 1. Note that the region can be formed by the intersection of more than 2 rectangles.'''

def largestSquareArea(bottomLeft, topRight):
    maximal_size = 0 

    for i in range(len(bottomLeft)): 
        x10, y10 = bottomLeft[i]
        x11, y11 = topRight[i]
        if y11-y10<=maximal_size or x11-x10<=maximal_size: 
            continue

        for j in range(i+1, len(bottomLeft)): 
            x20, y20 = bottomLeft[j]
            x21, y21 = topRight[j]
            if y21-y20<=maximal_size or x21-x20<=maximal_size: 
                continue
            if x21 <= x10 or y21<=y10 or x20>=x11 or y20>=y11: 
                continue 
            size_x_intersect = min(x11, x21) - max(x10, x20)
            if size_x_intersect < maximal_size: 
                continue 
            size_y_intersect = min(y11, y21) - max(y10, y20)
            if size_y_intersect < maximal_size:
                continue 
            maximal_size = min(size_x_intersect, size_y_intersect)
                
    return maximal_size**2

bottomLeft = [[1,1],[2,2],[1,2]]
topRight = [[3,3],[4,4],[3,4]]

print(largestSquareArea(bottomLeft, topRight))