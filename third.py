class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        # temp = temp.next
        # temp = new_node
        # temp.next = temp
        # new_node = self.head
        # new_node.next = temp
    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.data, end="-->")
            temp = temp.next
        if temp.next is None:
            print(temp.data)
    def reverse_iter(self):
        prev = None
        temp = self.head
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        self.head = prev
    def reverse_recur(self):
        
    def reverserecur(self):
        temp = reverserecur(self.head)
if __name__ == "__main__":
    Node1 = Node(5)
    ll = LinkedList(Node1)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.push(0)
    ll.print_list()
    ll.reverse()
    ll.print_list()