# Lets you traverse elements of a collection without exposing its
# underlying representation.

class LL:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = self.Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = self.Node(val)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next

ll = LL()
for v in [1,2,3]: ll.append(v)

for val in ll:
    print(val)
