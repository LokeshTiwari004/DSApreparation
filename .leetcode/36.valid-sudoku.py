#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    """
    Time: 25 mins
    O(1) space O(1) time since sudko will always have 81 cells 
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = {digit: set() for digit in range(1, 10)}
        y = {digit: set() for digit in range(1, 10)}
        z = {digit: set() for digit in range(1, 10)}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                val = int(val)

                if i in x[val]:
                    return False
                else:
                    x[val].add(i)

                if j in y[val]:
                    return False
                else:
                    y[val].add(j)
                
                block = (i//3, j//3)
                if block in z[val]:
                    return False
                else:
                    z[val].add(block)
        return True
                    
# @lc code=end

