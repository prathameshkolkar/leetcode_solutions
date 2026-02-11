# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur=head
        d1=ListNode(0) #odd
        c=d1
        d2=ListNode(0)
        d=d2      
        while cur:
            c.next=cur
            cur=cur.next
            c=c.next
            if cur:
                d.next=cur
                cur=cur.next
                d=d.next
        
        d.next=None
        c.next=d2.next
        return d1.next



            
            

        