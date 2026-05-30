/*
 * @lc app=leetcode id=142 lang=cpp
 *
 * [142] Linked List Cycle II
 */

// @lc code=start
#include<unordered_map>
#include<iostream>
using namespace std;

// time: 30 mins
// hint: no
// pattern: hashmap of ptrs
// complexity: O(n) time, O(n) space
// Edge Case: head is null

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head) {
            return head;
        }
        unordered_map<ListNode*, int> ele_pos;
        int pos = 0;
        while (head) {
            auto item = ele_pos.find(head);
            if (item == ele_pos.end()) {
                ele_pos[head] = pos;
                pos++;
            } else {
                return item->first;
            }
            head = head->next;
        }
        return NULL;
    }
};
// @lc code=end

