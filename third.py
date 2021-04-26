class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
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
        def _reverse_recur(temp, prev):
            if not temp:
                return prev
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            return _reverse_recur(temp, prev)
        self.head = _reverse_recur(temp = self.head, prev = None)
    def append_list(self, data):
        new_node = Node(data)
        temp = self.head
        if temp is None:
            new_node = self.head
        while temp.next:
            temp = temp.next
        if temp.next is None:
            temp.next = new_node
    def list_to_linked(self, collection):
        temp = self.head
        if temp.data is None:
            temp.data = collection[0]
            for i in range(2,len(collection),1):
                # if temp.data is None:
                #     new_node = Node(i)
                #     new_node = self.head
                #     temp.next = None
                self.append_list(i)
                temp = temp.next
            if temp.next is None:
                new_node = Node(collection[-1])
                temp.next = new_node
            return self.print_list()
        else:
            for i in collection:
                # if temp.data is None:
                #     new_node = Node(i)
                #     new_node = self.head
                #     temp.next = None
                self.append_list(i)
    # def list_to_ll(self, collection):
    #     temp = self.head
    #     if temp is None:
    #         temp = temp.next
    #         temp = collection[0]
    #         for i in range(1,len(collection)):
    #             self.append_list(i)
    #         return self.print_list()

lists = [1,2,3,4,5,6,7,8]
def list_to_ll(arr):
    for i in arr:
        ll.push(i)
    return ll.print_list()

if __name__ == "__main__":
    Node1 = Node()
    ll = LinkedList(Node1)
    ll.list_to_linked(lists)