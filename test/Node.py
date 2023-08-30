class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def append(self, val):
        end = Node(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end


x = Node(1)
x.append(2)
x.append(3)

node = x

print(node.data)
while node.next:
    node = node.next
    print(node.data)
