# köken
# date: 28.02.2021 (dd/mm/yyyy)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
    #Complete this method
        # create a node each time
        node = Node(data)
        # the first case
        if head == None:
            return node
        # other nodes
        else:
            current_Node = head
            while current_Node.next != None:
                current_Node = current_Node.next
            # insert the created new node to the tail of the list
            current_Node.next = node
            return head


mylist= Solution()
# enter an integer, number of nodes
T=int(input())
head=None
# insert nodes
for i in range(T):
    # enter the data
    data=int(input())
    # new node with head and data
    # 1st None, data1 | 2nd head1, data2
    # 3rd head2, data3 | 4th head3, data4
    head=mylist.insert(head,data)
mylist.display(head);
# head3 -> head2 -> head1 -> None
# data4 <- data3 <- data2 <- data1
