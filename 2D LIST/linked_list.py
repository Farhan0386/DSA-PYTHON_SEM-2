class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self,head=None):
        self.head=head

    def insert_at_Begining(self,data):
        new_Node=Node(data,self.head)
        self.head=new_Node
    def insert_at_End(self,data):
        new_Node=Node(data)      