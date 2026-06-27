#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq
class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, heapq.heappop_max(self.small))
        if self.large and self.small[0] > self.large[0]:
            heapq.heappush(self.large, heapq.heappop_max(self.small))
        if len(self.large) - len(self.small) == 2:
            heapq.heappush_max(self.small, heapq.heappop(self.large))

    def findMedian(self) -> float:
        match (len(self.small) - len(self.large)):
            case 0:
                return (self.small[0] + self.large[0]) / 2
            case 1:
                return self.small[0]
            case -1:
                return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

