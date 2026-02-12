# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # c=head
        # a=[]
        # while c!=None:
        #     a.append(c.val)
        #     c=c.next
        # if a==a[::-1]:
        #     return True
        # return False
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        pre=None
        cur=slow
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        com=pre
        while com:
            if head.val!=com.val:
                return False
            head=head.next
            com=com.next
        return True
        
        


                    