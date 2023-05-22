# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class SLL:
#     def __init__(self):
#         self.head=None
#
#     def add_node(self,new_val):
#         new_node=ListNode(new_val)
#         if self.head is None:
#             self.head=new_node
#             return
#         laste=self.head
#         while (laste.next):
#             laste=laste.next
#         laste.next=new_node

class ListNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def add_node(self,new_val):
        new_node=ListNode(new_val)
        if self.val is None:
            self.val=new_node
            return
        laste=self.val
        while (laste.next):
            laste=laste.next
        laste.next=new_node

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result=ListNode()
        gain=False
        while l1!=None or l2!=None:
            if l1==None:
                if gain:
                    i=l2.val+1
                    gain = False
                else:
                    i=l2.val

                l2=l2.next

            elif l2==None:
                if gain:
                    i=l1.val+1
                    gain=False
                else:
                    i=l1.val

                l1=l1.next

            else:
                if gain:
                    i=l1.val+l2.val+1
                    gain=False
                else:
                    i = l1.val + l2.val

                l1=l1.next
                l2=l2.next

            if i >=10:
                gain=True
                i=i-10

            result.add_node(i)

        if gain:
            result.add_node(1)

        return result.val

#%%  test

sll1 = ListNode()
sll2 = ListNode()
list1 = [9,9,1]
list2 = [1]
for i in list1:
    sll1.add_node(i)
for i in list2:
    sll2.add_node(i)
# %%
x = Solution
Solution.addTwoNumbers(x, sll1.val,sll2.val)
