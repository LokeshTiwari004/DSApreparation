#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        hashset = set(nums)
        res = []
        for idx, num in enumerate(nums):
            if n-idx-1 and  num == nums[idx + 1]:
                continue
            if num:
                if idx and nums[idx-1] == num and -2 * num in hashset:
                    res.append([num, num, -2*num])
                
                for pt2 in range(idx+1, n):
                    if n-pt2-1 and nums[pt2] == nums[pt2+1]:
                        continue
                    num2 = nums[pt2]
                    num3 = -num-num2
                    if num3 > num2 and num3 in hashset:
                        res.append([num, num2, num3])

            elif num == 0 and idx>1 and nums[idx-2] == 0:
                res.append([0, 0, 0])
        return res
# @lc code=end