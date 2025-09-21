"""
Given an integer array nums and an integer k, return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k. 

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}

        for i, j in enumerate(nums):
            if j in dic and i - dic[j] <= k:
                return True
            dic[j] = i
        return False

#Time limit exceed but worked
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
                elif abs(i - j) > k:
                    break
        return False