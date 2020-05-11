'''
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

Seems pretty straight forward. I'm not going to make any assumtions about data
type just that it is in a linked list like it says.

'''
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current = head
        last_node = None
        while current is not None:
            if current.val == val:
                if last_node is not None:
                    last_node.next = current.next
                else:
                    head = current.next
            last_node = current
            current = current.next
        return head


def create_ll_from_list(ls):
    head = ListNode()
    current = head
    for i in ls:
        current.val = i
        new_node = ListNode()
        current.next = new_node
        current = new_node
    return head


def verify_ll_equal(ll1, ll2):
    current1, current2 = ll1, ll2
    while current1 is not None or current2 is not None:
        print(current1.val, current2.val)
        if current1.val != current2.val:
            return False
        current1, current2 = current1.next, current2.next
    return True


s = Solution()
print(verify_ll_equal(create_ll_from_list([1,2,3,4,5]), s.removeElements(create_ll_from_list([1,2,6,3,4,5,6]), 6)))
"""
var table for removeElements
vars      | values
current   | node(1), node(2), node(3), node(4), node(5), node(6), node(7), None
last_node | None, node(1), node(2), node(2), node(4),  node(5), node(6), node(6)
head      | Node(1)
val       | 6,
"""

print(verify_ll_equal(create_ll_from_list([1,2,6,3,4,6]), s.removeElements(create_ll_from_list([1,5,2,6,3,4,5,6]), 5)))
"""
var table for removeElements
vars      | values
current   | node(1), node(2), node(3), node(4), node(5), node(6), node(7), node(8), None
last_node | None, node(1), node(1), node(3), node(4), node(5), node(6), node(7), node(7),
head      | Node(1) always
val       | 5 always
"""
