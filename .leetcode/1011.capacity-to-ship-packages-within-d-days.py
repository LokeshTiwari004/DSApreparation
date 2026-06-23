#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if not weights:
            return 0

        lo, hi = weights[0], 0
        for w in weights:
            lo = max(w, lo)
            hi += w
        while lo < hi:        
            mid = (lo+hi) // 2
            req_days = 1
            capacity = mid
            for w in weights:
                if w > capacity:
                    req_days += 1
                    capacity = mid
                capacity -= w
            

            if req_days > days:
                lo = 1 + (lo+hi) // 2
            else:
                hi = (lo+hi) // 2
        return hi
# @lc code=end

