from math import log

class HollowHeap:
    class Node:
        rank = 0
        child = None
        nxt = None
        ep = None


        def __init__(self, key, item):
            self.key = key
            self.item = item


        def add_child(self, x):
            x.nxt = self.child
            self.child = x
            return self


        def destroy(self):
            self.child = None
            self.nxt = None
            self.ep = None


    root = None
    num_nodes = 0


    def union(self, h2):
        self.root = self.link(self.root, h2.root)
        self.num_nodes += h2.num_nodes


    def insert(self, key, item):
        node = self.Node(key, item)

        if not self.root:
            self.root = node
        else:
            self.root = self.link(self.root, node)

        self.num_nodes += 1
        return node


    def min(self):
        return self.root


    def decrease_key(self, node, key):
        if node == self.root:
            self.root.key = key
            return

        v = self.Node(key, node.item)
        node.item = None

        if node.rank > 2:
            v.rank = node.rank - 2

        v.child = node
        node.ep = v

        self.num_nodes += 1
        self.root = self.link(self.root, v)



    def delete_min(self):
        return self.delete(self.root)


    def delete(self, node):
        # so we can return the deleted node
        n = self.Node(node.key, node.item)

        node.item = None

        # non root item deleted
        if self.root.item:
            return n

        max_rank = 0
        ranks = [None] * int(1 + log(self.num_nodes)/log(2))

        while self.root:
            w = self.root.child
            v = self.root
            self.root = self.root.nxt
            while w:
                u = w
                w = w.nxt
                if not u.item:
                    if not u.ep:
                        u.nxt = self.root
                        self.root = u
                    else:
                        if u.ep == v:
                            w = None
                        else:
                            u.nxt = None
                        u.ep = None
                else:
                    # ranked links
                    while ranks[u.rank]:
                        u = self.link(u, ranks[u.rank])
                        ranks[u.rank] = None
                        u.rank += 1
                    ranks[u.rank] = u
                    if u.rank > max_rank:
                        max_rank = u.rank

            v.destroy()
            self.num_nodes -= 1

        # unranked links
        for i in range(max_rank + 1):
            if ranks[i]:
                if not self.root:
                    self.root = ranks[i]
                else:
                    self.root = self.link(self.root, ranks[i])

        return n


    def link(self, x, y):
        if x.key < y.key:
            return x.add_child(y)
        else:
            return y.add_child(x)
