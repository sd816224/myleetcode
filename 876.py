# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        init_head=head
        list=[]
        while head!=None:
            list.append(head.val)
            head=head.next
        middle=int(len(list)/2)
        i=0
        head=init_head
        while i < middle:
            i+=1
            head=head.next
        return head

class Solution2(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

#%%
from node_creater import SLL
sll=SLL()
list=[1,2,3,4,'ssd']
for i in list:
    sll.add_node(i)
#%%
x=Solution2
Solution2.middleNode(x,sll.head)
