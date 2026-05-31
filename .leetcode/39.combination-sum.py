#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def count(self, candidates, target):
        for candidate in candidates:
            if candidate > target:
                yield [candidate, 0]
            elif candidate == target:
                yield [candidate, 1]
            else:
                for rest in self.count(candidates, target - candidate):
                    yield [candidate] + rest

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        ds = []
        for combo in self.count(candidates, target):
            if combo[-1]:
                d = dict()
                for i in combo[:-1]:
                    if i in d:
                        d[i] += 1
                    else:
                        d[i] = 1
                ds.append(d)
                answer.append(combo[:-1])
        to_pop = set()
        for i, d in enumerate(ds):
            for j, q in enumerate(ds[i+1:]):
                if d==q and i != j:
                    to_pop.add(j)

        for i in sorted(list(to_pop), reverse=True):
            answer.pop(i)
        return answer
# @lc code=end

