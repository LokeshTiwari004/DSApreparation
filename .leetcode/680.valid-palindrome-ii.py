#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1
        ckpt, flag = None, False
        while lo < hi:
            if s[lo] != s[hi]:
                if flag:
                    return False
                elif ckpt:
                    lo, hi = ckpt
                    hi -= 1
                    flag = True
                else:
                    ckpt = (lo, hi)
                    lo += 1
            else:
                hi -= 1
                lo += 1
        return True
                
# @lc code=end

