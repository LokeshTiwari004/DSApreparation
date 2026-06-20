#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lo, hi = 0, 0
        n = len(nums)
        win_sum = nums[0]
        win_len = n+1
        while True:
            if win_sum < target:
                if hi < n - 1:
                    hi += 1
                    win_sum += nums[hi]
                else:
                    break
            else:
                win_len = min(win_len, hi-lo+1)
                if lo < hi:
                    win_sum -= nums[lo]
                    lo += 1
                else:
                    break

        if win_len == n+1:
            return 0
        else:
            return win_len
# @lc code=end
