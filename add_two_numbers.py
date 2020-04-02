""" You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

# So you just want me to add two numbers together but they happen to be stored as linked lists?

# Would it be okay to modify the input in order to return a linked list or should I create a new list?
# Since linked lists aren't a standard data type should I implement to solve this or create the function assuming a certain implementation?

# I'll assume that I should make a new linked list for the output instead of changing the input.
# I'll use the example implemention on leet code.

"""So I think the way to solve this would be to iterate through each node in the lists
and add each number in each place together until both lists hit their end node and the carry value
is False."""

# Definition for singly-linked list by leet code.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start_node = ListNode(None)
        current = start_node
        carry = False
        while l1 is not None or l2 is not None or carry is True:
            if current.val is not None:
                current.next = ListNode(None)
                current = current.next
            if l1 is None:
                num1 = 0
            else:
                num1 = l1.val
                l1 = l1.next
            if l2 is None:
                num2 = 0
            else:
                num2 = l2.val
                l2 = l2.next
            place = num1 + num2
            if carry is True:
                place += 1
                carry = False
            if place >= 10:
                place -= 10
                carry = True
            current.val = place
        return start_node


"""I think this solution is a little long winded with a lot of conditionals,
 but one upside is that it is beautifuly time efficient because it iterates through
 both lists at once and so it time complexity only grows compared to the longer numbers
 length. This might be a naive solution but it is currently the fastest thing I could
 think to do. I don't have to make any othe data structures and all calculations that
 need to go into the new linked list happen as it is created."""


def test_case():
    """Feel free to modify test cases if you want to test it
    I built this one just to demostrate that it works."""

    print('Input was: ')
    start_node1 = ListNode(5)
    start_node1.next = ListNode(7)
    start_node1.next.next = ListNode(1)
    print([5, 7, 1])

    start_node2 = ListNode(3)
    start_node2.next = ListNode(7)
    start_node2.next.next = ListNode(8)
    print([3, 7, 8])

    print('Expected output is: ')
    print([8, 4, 0, 1])
    print('Because 175 + 873 = 1048')

    print('Output was: ')
    s = Solution()
    added_linked_list = s.addTwoNumbers(start_node1, start_node2)
    current_node = added_linked_list
    output_list = []
    while current_node != None:
        output_list.append(current_node.val)
        current_node = current_node.next
    print(output_list)


if __name__ == '__main__':
    test_case()
