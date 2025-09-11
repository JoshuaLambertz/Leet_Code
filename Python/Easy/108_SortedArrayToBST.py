"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted

Example 2:
    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def arrayToBST(nums):
            if not nums:
                return None
            
            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            root.left = arrayToBST(nums[:mid])
            root.right = arrayToBST(nums[mid+1:])

            return root
        return arrayToBST(nums)