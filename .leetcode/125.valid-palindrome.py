#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
# Time: 10 mins
# Pattern: 2 pointer
# O(n) time O(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s)-1
        while lo < hi:
            lc = s[lo]
            if not lc.isalnum():
                lo += 1
                continue

            hc = s[hi]
            if not hc.isalnum():
                hi -= 1
                continue

            if lc.lower() != hc.lower():
                return False
            lo += 1
            hi -= 1
        return True
# @lc code=end
