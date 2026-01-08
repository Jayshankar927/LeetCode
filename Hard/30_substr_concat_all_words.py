'''You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.'''
from collections import Counter

def findSubString(s,words):
    if not s or not words:
        return []
    
    wordLen = len(words[0])
    wordCount = len(words)
    totalLen = wordCount * wordLen
    freq = Counter(words)

    res = []

    for i in range(wordLen):
        left=i
        count=0
        seen = Counter()

        for right in range(i,len(s)-wordLen+1,wordLen):
            word = s[right:right+wordLen]

            if word in freq:
                seen[word] +=1
                count +=1

                while seen[word] > freq[word]:
                    leftword = s[left:left+wordLen]
                    seen[leftword] -= 1
                    left += wordLen
                    count -= 1

                if count == wordCount:
                    res.append(left)
            else:
                seen.clear()
                left = right + wordLen
                count=0
    
    return res

s = "barfoothefoobarman"
words = ["foo","bar"]

print(findSubString(s,words)) # output: [0,9]