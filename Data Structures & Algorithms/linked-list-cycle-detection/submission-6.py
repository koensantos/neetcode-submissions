# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head

        if not curr or curr.next == None or curr.next.next == None:
            return False
        
        slow = curr.next
        fast = curr.next.next

        while fast != None:
            if slow == fast:
                return True
            if fast.next == None or fast.next.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return False