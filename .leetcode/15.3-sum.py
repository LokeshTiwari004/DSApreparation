#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        lookup = dict()
        for idx, num in enumerate(nums):
            if num in lookup:
                lookup[num].add(idx)
            else:
                lookup[num] = {idx}
        
        n = len(nums)
        answer = set()
        if len(lookup.get(0, [])) > 2:
            answer.add((0, 0, 0))

        for i in range(n):
            a = nums[i]
            for j in range(i+1, n):
                b = nums[j]
                complement = -a-b
                complement_ids = lookup.get(complement, None)
                if not complement_ids or i in complement_ids or j in complement_ids:
                    continue
                
                if a >= b:
                    if b >= complement:
                        triplet = (a, b, complement)
                    elif complement >= a:
                        triplet = (complement, a, b)
                    else:
                        triplet = (a, complement, b)
                else:
                    if a >= complement:
                        triplet = (b, a, complement)
                    elif complement >=b:
                        triplet = (complement, b, a)
                    else:
                        triplet = (b, complement, a)
                answer.add(triplet)
        return [list(item) for item in answer]
# @lc code=end