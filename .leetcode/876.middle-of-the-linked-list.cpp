/*
 * @lc app=leetcode id=876 lang=cpp
 *
 * [876] Middle of the Linked List
 */

// @lc code=start
class Solution {
    // time: 30 mins
    // hint: no
    // Pattern: middle of LL
    // complexity: O(n) time, o(1) space
    // Edge Case: Empty LL, LL with single node
public:
    ListNode* middleNode(ListNode* head) {
        int flag=1;
        ListNode* middle = head;
        if (!head) {
            return middle;
        }
        while (1) {
            head = head->next;
            if (head) {
                middle = flag ? middle->next : middle;
                flag =  flag ? 0 : 1;
            }
            else {
                return middle;
            }
        }        
    }
};
// @lc code=end

