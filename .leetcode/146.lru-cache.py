#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.map = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.map.get(key, -1)
        if value != -1:
            del self.map[key]
            self.map[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            del self.map[key]
            self.map[key] = value
            return
        if len(self.map) == self.capacity:
            self.map.popitem(last=False)
        self.map[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

