#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        if n <= days:
            return max(weights)
        
        state = list(range(days))
        
        weights_per_day = []
        max_wpd = weights[0]
        min_wpd = weights[0]
        for i in range(n):
            weight = weights[i]
            if i < days:
                weights_per_day.append(weight)
                max_wpd = max(max_wpd, weight)
                min_wpd = min(min_wpd, weight)
            else:
                weights_per_day[-1] += weight
                max_wpd = max(max_wpd, weights_per_day[-1])
        
        h = max_wpd - min_wpd
        
        print(weights_per_day, max_wpd, min_wpd, h)
        def best_move():
            move = None
            best_h = h
            for i in range(1, days):
                if state[i] - 1 != state[i-1]:
                    delta = weights[state[i-1]]
                    new_h = max(max_wpd, weights_per_day[i] + delta) - min(min_wpd, weights_per_day[i-1] - delta)
                    if new_h < best_h:
                        best_h = new_h
                        move = (i, -1)

                if i == days - 1 or state[i] + 1 != state[i+1]:
                    delta = weights[state[i]]
                    new_h = max(max_wpd, weights_per_day[i-1] + delta) - min(min_wpd, weights_per_day[i]-delta)
                    print(new_h)
                    if new_h < best_h:
                        best_h = new_h
                        move = (i, 1)
            return move
        
        while True:
            move = best_move()
            print(move)
            if move is None:
                print('broken')
                break
            if move[1] == 1:
                delta = weights[state[i]]
                weights_per_day[i-1] += delta
                weights_per_day[i] -= delta
                max_wpd = max(max_wpd, weights_per_day[i-1])
                min_wpd = min(min_wpd, weights_per_day[i])
            else:
                delta = weights[state[i-1]]
                weights_per_day[i-1] -= delta
                weights_per_day[i] += delta
                min_wpd = min(min_wpd, weights_per_day[i-1])
                max_wpd = max(max_wpd, weights_per_day[i])

            h = max_wpd - min_wpd
            state[move[0]] += move[1]
        return max_wpd
        
# @lc code=end

