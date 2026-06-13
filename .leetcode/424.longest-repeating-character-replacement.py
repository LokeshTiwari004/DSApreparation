#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
# Time: 30 mins
# Hint: No
# Pattern Sliding window
# edge case: k >= len(s), char_freq + k >= len(s)
# complexity: O(n*charset) Time, O(charset + extra) space
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seq_len = len(s)

        if seq_len <= k:
            return seq_len
        
        freq_table = dict()
        for char in s:
            if char in freq_table:
                freq_table[char] +=1
            else:
                freq_table[char] = 1

            if freq_table[char] + k == seq_len:
                return seq_len

        max_subsequence_length = k
        for char in freq_table:
            quota = k
            cursor = 0
            win_len = 0
            while quota:
                if s[cursor] != char:
                    quota -= 1
                cursor += 1
                win_len += 1
            
            max_subsequence_length = max(max_subsequence_length, win_len)

            while cursor < seq_len:
                if s[cursor] == char:
                    cursor += 1
                    win_len += 1
                elif s[cursor-win_len] != char:
                    cursor += 1
                else:
                    win_len -= 1
                
                max_subsequence_length = max(max_subsequence_length, win_len)
        return max_subsequence_length

            
# @lc code=end

