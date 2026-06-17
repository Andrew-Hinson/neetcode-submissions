# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# node1 -> node2 -> node3 
# return new head after reversing

# iterate through nodes, while iterating, swapping pointers, the end is my new head
# two pointer solution
        curr_node, prev_node = head, None
        while curr_node:
# first thing, create temp pointer to next node
            next_node = curr_node.next
            # set curr.next pointing back to prev
            curr_node.next = prev_node
            # set prev = curr
            prev_node = curr_node
            # move cur to next
            curr_node = next_node
#prev node will be pointing at the head because cur_node will be null when it reaches there.
        return prev_node