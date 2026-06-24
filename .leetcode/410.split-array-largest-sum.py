#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        state = list(range(k)) + [len(nums)]
        group_weight = nums[:k-1] + [sum(nums[k-1:])]
        def helper():
            maxgps, mingps = [0], [0]
            for idx in range(k):
                if group_weight[idx] > group_weight[maxgps[-1]]:
                    maxgps = [idx]
                elif group_weight[idx] == group_weight[maxgps[-1]]:
                    maxgps.append(idx)
                
                if group_weight[idx] < group_weight[mingps[-1]]:
                    mingps = [idx]
                elif group_weight[idx] == group_weight[mingps[-1]]:
                    mingps.append(idx)
            return mingps, maxgps, group_weight[maxgps[-1]] - group_weight[mingps[-1]]

        def get_moves(info):
            mingps, maxgps, _ = info
            moves = set()
            for maxgp in maxgps:
                if maxgp and state[maxgp] + 1 != state[maxgp+1]:
                    moves.add((maxgp, 1))
                if maxgp < k-1 and state[maxgp+1] -1 != state[maxgp]:
                    moves.add((maxgp+1, -1))
            
            for mingp in mingps:
                if mingp and state[mingp] - 1 != state[mingp - 1]:
                    moves.add((mingp, -1))
                if mingp < k-1 and state[mingp + 1] + 1 != state[mingp + 2]:
                    moves.add((mingp+1, 1))
            return moves
        
        def take_step(info):
            moves = get_moves(info)
            best_move = None
            best_info = info
            while moves:
                move = moves.pop()
                delta = nums[state[move[0]]] if move[1] == 1 else nums[state[move[0]]-1]
                group_weight[move[0]] -= move[1]*delta
                group_weight[move[0]-1] += move[1]*delta
                new_info = helper()
                if new_info[-1] < best_info[-1]:
                    best_move = move
                    best_info = new_info
                group_weight[move[0]] += move[1]*delta
                group_weight[move[0]-1] -= move[1]*delta

            if best_move:
                delta = nums[state[best_move[0]]] if best_move[1] == 1 else nums[state[best_move[0]]-1]
                print(best_move, delta)
                state[best_move[0]] += best_move[1]
                group_weight[best_move[0]] -= best_move[1]*delta
                group_weight[best_move[0]-1] += best_move[1]*delta
                return best_info

        info = helper()
        while True:
            print(state)
            print(group_weight)
            print(info)
            new_info = take_step(info)
            if new_info is None:
                return group_weight[info[1][-1]]
            else:
                info = new_info
# @lc code=end