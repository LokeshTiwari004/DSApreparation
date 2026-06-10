#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        slen, plen = len(s), len(p)
        if plen > slen:
            return []
        
        pdict = dict()
        for chr in p:
            if chr in pdict:
                pdict[chr] += 1
                continue
            pdict[chr] = 1
        
        windict = dict()
        for i in range(plen):
            chr = s[i]
            if chr in windict:
                windict[chr] += 1
                continue
            windict[chr] = 1

        if windict == pdict:
            output.append(0)

        for i in range(plen, slen):
            chr = s[i-plen]
            windict[s[i-plen]] -= 1
            if not windict[chr]:
                del windict[chr]
            
            chr = s[i]
            if chr in windict:
                windict[chr] += 1
            else:
                windict[chr] = 1

            if windict == pdict:
                output.append(i - plen + 1)

        return output
# @lc code=end

