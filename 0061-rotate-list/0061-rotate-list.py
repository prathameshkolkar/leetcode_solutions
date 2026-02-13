# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l=0 
        cur=head
        while cur:
            l=l+1
            cur=cur.next

        for i in range(k%l):
            cur=head
            while cur.next and cur.next.next:
                cur=cur.next
                
            temp=cur.next
            temp.next=head
            cur.next=None
            head=temp
        return head




        