"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        p1 = 0
        p2 = len(s) - 1
        
        while p1 < p2:
            temp = s[p2]
            s[p2] = s[p1]
            s[p1] = temp
            p1 += 1
            p2 -= 1