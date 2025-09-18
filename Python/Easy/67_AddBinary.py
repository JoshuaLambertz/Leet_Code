"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

    0+0=0
    1+0=0
    0+1=0
    1+1=0  1 is taken over to next column

     11
    +01
    ----
    100
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b, 2))

        return sum[2:]
    
def addBin(a, b):
    max_length = max(len(a), len(b))
    a = a.zfill(max_length)
    b = b.zfill(max_length)

    res = ''

    