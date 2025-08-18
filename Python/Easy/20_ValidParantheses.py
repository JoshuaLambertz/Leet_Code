"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Example 5:
    Input: s = "([)]"
    Output: false
"""


#Answer without Mapping
class Solution:
    def isValid(self, s: str) -> bool:
        x = "()"
        y = "[]"
        
        ans = []

        for i in range(len(s)):

            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                ans.append(s[i])
            elif len(ans) > 0 and ans[-1] == "(" and s[i] == ")" or \
               len(ans) > 0 and ans[-1] == "[" and s[i] == "]" or \
               len(ans) > 0 and ans[-1] == "{" and s[i] == "}":
                ans.pop()
            else:
                return False

        if len(ans) == 0:
            return True
        else:
            return False
        
#Copied Answer with Mapping
class Solution:
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []