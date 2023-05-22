# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from node_creater import SLL
sll=SLL()
list=[1,2,3,4,'ssd']
for i in list:
    sll.add_node(i)

    #%%
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ls=[]
        while head !=None:
            ls.append(head.val)
            head=head.next
        # if ls==ls[::-1]:
        #     return True
        # else:
        #     return False
        print(ls)
    #%%
x=Solution
x.isPalindrome(x,sll.head)