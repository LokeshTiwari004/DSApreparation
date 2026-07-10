#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_dec = deque()
        res = []
        for idx in range(len(nums)):
            num = nums[idx]
            
            while mono_dec and nums[mono_dec[-1]] <= num:
                mono_dec.pop()
            mono_dec.append(idx)
            
            if mono_dec[0] < idx-k+1:
                mono_dec.popleft()
            
            if idx >= k-1:
                res.append(nums[mono_dec[0]])
        return res    
# @lc code=end

