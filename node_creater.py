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


#%%
sll=ListNode()
#%%
list=[1,2,3,4,'ssd']
for i in list:
    sll.add_node(i)

