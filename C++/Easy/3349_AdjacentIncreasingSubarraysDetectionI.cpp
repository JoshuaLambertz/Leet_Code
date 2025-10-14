/*
Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that
both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:
Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.

Example 1:
    Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3
    Output: true
    Explanation:
        The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
        The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
        These two subarrays are adjacent, so the result is true.

Example 2:
    Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5
    Output: false
*/

#include <iostream>
#include <vector>
using namespace std;

bool hasIncreasingSubarrays(vector<int>& nums, int k) {
    int count = 1;

    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] == nums[i-1]+1) {
            count++;

            if (count == k) return true;
        } else {
            count = 1;
        }
    }

    return false;
}

int main() {
    vector<int> nums = {2,5,7,8,9,2,3,4,3,1};
    int k = 3;
    
    if (hasIncreasingSubarrays(nums, k))
        cout << "true" << k << endl;
    else
        cout << "false" << k << endl;

    return 0;
}



#include <vector>
using namespace std;

class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int mx = 0;
        int prev = 0;
        int cur = 0;

        for (int i = 0; i < n; i++) {
            cur++;
            if (i == n - 1 || nums[i] >= nums[i + 1]) {
                mx = max({mx, cur / 2, min(prev, cur)});
                prev = cur;
                cur = 0;
            }
        }
        return mx >= k;
    }
};