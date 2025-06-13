class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList2:

    def __init__(self):
        """
        Head is dummy head
        tail point the tail of MyLinkedList2
        size is the number of elements
        """
        self.head = Node(None)
        self.tail = self.head
        self.size = 0

    # Create
    def add(self, index: int=0, val=None) -> None:
        """
        Add node into ${index} of MyLinkedList2
        """
        # check the index
        self.check_possible_index(index)
        new_node = Node(val)

        # the first element
        if index == 0:
            new_node.next = self.head.next
            self.head.next = new_node
            # if the list is empty, then tail point to new_node
            # add element into empyt MyLinkedList2
            if self.size == 0:
                self.tail = new_node
            self.size += 1
            return
        prev = self.head
        for _ in range(index):
            # self.head is dummy head node, therefor
            # index will be the current index after loop
            # if index is 3. range(3) is [0,2]/[0,3)
            # H -> 1 -> 2 ->3 ->4 -> None
            #      0    1   2   3
            # size is 4
            # start is prev point H
            # when index is 0: prev = H.next/prev=1
            # index is 1: prev=2
            # therefore prev is index 3's previous element
            prev = prev.next
        # H->1->2->3->4->None
        #       P  P.n
        # H->1->2->new_node->3->4->None
        new_node.next = prev.next
        prev.next = new_node
        # last element
        if index == self.size:
            self.tail = new_node
        # increase size
        self.size += 1
        return

    def add_head(self, val) -> None:
        self.add(0, val)

    def add_tail(self, val) -> None:
        self.add(self.size, val)

    # Delete
    def remove(self, index: int) -> None:
        # check index
        self.check_available_index(index)
        if index == 0:
            self.head.next = self.head.next.next
        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        if index == self.size - 1:
            self.tail = prev
        self.size -= 1

    def remove_head(self) -> None:
        self.remove(0)

    def remove_tail(self) -> None:
        self.remove(self.size-1)

    # Update
    def update(self, index: int, val) -> None:
        self.check_available_index(index)
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        curr.val = val

    # Query/Get
    def get(self, index: int):
        self.check_available_index(index)
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def get_head(self):
        return self.get(0)

    def get_tail(self):
        return self.get(self.size-1)

    # Check
    def is_available_index(self, index: int) -> bool:
        "Check is the index in [0, slef.size)"
        return 0 <= index < self.size

    def is_possible_index(self, index: int) -> bool:
        "Check is the index is a possible index for adding value"
        return 0 <= index <= self.size

    def check_available_index(self, index: int) -> None:
        if not self.is_available_index(index):
            raise ValueError("The index is out of range")

    def check_possible_index(self, index: int) -> None:
        if not self.is_possible_index(index):
            raise ValueError("The index is too big" +
                             ", please make sure your index is in [0,size+1)")
