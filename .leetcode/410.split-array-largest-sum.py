#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo, hi = max(nums), sum(nums)
        def greedy(limit):
            win_sum = 0
            win_count = 1
            for num in nums:
                win_sum += num
                if win_sum > limit:
                    win_count += 1
                    win_sum = num
            
            if win_count > k:
                return False
            return True
        
        while lo < hi:
            mid = (lo + hi) // 2
            if greedy(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi
# @lc code=end