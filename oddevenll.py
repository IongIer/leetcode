# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current_odd = head
        current_even = head.next
        second_half_head = current_even
        while current_even and current_even.next:
            current_odd.next, current_even.next = (
                current_odd.next.next,
                current_even.next.next,
            )
            current_odd, current_even = current_odd.next, current_even.next
        current_odd.next = second_half_head
        return head
