'''You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 

Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.
Example 2:

Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.'''

def minimumCost(source,target,original,changed,cost):
    
    arr = [[float('inf')] * 26 for _ in range(26)]
    for i in range(26):
        arr[i][i] = 0
    
    #build initial graph
    for i in range(len(original)):
        val1 = ord(original[i]) - ord('a')
        val2 = ord(changed[i]) - ord('a')
        arr[val1][val2] = min(arr[val1][val2], cost[i])
    
    #Floyd-Warshall algorithm
    for i in range(26):
        for j in range(26):
            for k in range(26):
                arr[j][k] = min(arr[j][k], arr[j][i]+arr[i][k])
    
    ans = 0
    for i in range(len(source)):
        v1 = ord(source[i]) - ord('a')
        v2 = ord(target[i]) - ord('a')
        
        if v1 == v2:
            continue
        
        if arr[v1][v2] == float('inf'):
            return -1
        
        ans += arr[v1][v2]
    
    return ans

source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]

print(minimumCost(source,target,original,changed,cost)) # Output : 28