"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
    Input: nums = [3,2,3]
    Output: 3

Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
"""

#Fastest approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

#Dictionary approach
def majorityElement(self, nums: List[int]) -> int:
    num = {}

    for i in nums:
        if i not in num:
            num[i] = 1
        else:
            num[i] += 1
    
    return max(num, key=num.get)