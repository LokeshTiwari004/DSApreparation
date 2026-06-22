#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        recent, count = fruits[0], 0
        last = None
        seq_len = 0
        max_fruits = 0
        for f in fruits:
            if f == recent:
                count += 1
            else:
                if last != f:
                    max_fruits = max(max_fruits, seq_len)
                    seq_len = count
                
                recent, last, count = f, recent, 1
            seq_len += 1

        max_fruits = max(max_fruits, seq_len)
        return max_fruits
# @lc code=end

