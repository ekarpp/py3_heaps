from math import log


class FibonacciHeap:
    class Node:
        marked = False
        child = None
        left = None
        right = None
        parent = None
        rank = 0


        def __init__(self, key, value):
            self.key = key
            self.value = value


    root_head = None
    min_node = None
    num_nodes = 0


    def min(self):
        return self.min_node


    def insert(self, key, val):
        node = self.Node(key, val)
        self.add_root(node)
        self.num_nodes += 1
        if not self.min_node or node.key < self.min_node.key:
            self.min_node = node
        return node


    def union(self, heap):
        # nothing to do if other is empty
        if not heap.root_head:
            return

        for root in self.list_nodes(heap.root_head):
            self.add_root(root)

        if not self.min_node or heap.min_node.key < self.min_node.key:
            self.min_node = heap.min_node

        self.num_nodes += heap.num_nodes


    def delete_min(self):
        if not self.min_node:
            return None

        m = self.min_node

        # add children of m to root list
        for child in self.list_nodes(m.child):
            self.add_root(child)
            child.parent = None

        # remove m from root list
        if m.left == m:
            self.min_node = None
            self.root_head = None
        else:
            if self.root_head == m:
                self.root_head = m.left
            m.left.right = m.right
            m.right.left = m.left

        # consolidate
        ranks = [None] * int(1 + log(self.num_nodes)/log(2))
        for root in self.list_nodes(self.root_head):
            node = root
            r = node.rank
            while ranks[r]:
                tmp = ranks[r]
                node = self.link(node, tmp)
                ranks[r] = None
                r += 1
            ranks[r] = node

        # find new minimum
        self.min_node = self.root_head
        for root in self.list_nodes(self.root_head):
            if root.key < self.min_node.key:
                self.min_node = root

        self.num_nodes -= 1
        return m


    def decrease_key(self, node, key):
        if key > node.key:
            return

        node.key = key
        p = node.parent

        if p and node.key < p.key:
            self.cut(node)
            self.cascading_cut(p)

        if key < self.min_node.key:
            self.min_node = node


    def delete(self, node):
        self.decrease_key(node, self.min_node.key - 1)
        return self.delete_min()



    # helper functions

    # returns circular linked list as an array
    def list_nodes(self, head):
        if not head:
            return []

        list = [head]
        node = head.left

        while node != head:
            list.append(node)
            node = node.left

        return list


    def add_root(self, root):
        if not self.root_head:
            root.left = root
            root.right = root
            self.root_head = root
        else:
            l = self.root_head.left
            self.root_head.left = root
            root.right = self.root_head
            root.left = l
            l.right = root


    def link(self, n1, n2):
        if n2.key < n1.key:
            n1, n2 = n2, n1

        # update n2 parent
        n2.parent = n1

        # remove n2 from root list
        if self.root_head == n2:
            self.root_head = n2.left
        n2.left.right = n2.right
        n2.right.left = n2.left

        # add n2 to child list of n1
        if not n1.child:
            n1.child = n2
            n2.left = n2
            n2.right = n2
        else:
            l = n1.child.left
            n1.child.left = n2
            n2.right = n1.child
            n2.left = l
            l.right = n2

        n1.rank += 1
        n2.marked = False

        return n1


    def cut(self, x):
        p = x.parent
        # remove from child list
        if p.child == x:
            if p.rank == 1:
                p.child = None
            else:
                p.child = x.left
        x.left.right = x.right
        x.right.left = x.left
        p.rank -= 1

        self.add_root(x)
        x.parent = None
        x.marked = False


    def cascading_cut(self, y):
        p = y.parent
        if p:
            if not p.marked:
                p.marked = True
            else:
                self.cut(y)
                self.cascading_cut(p)
