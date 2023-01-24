from linked_list import *


class UnionFind:
    def __init__(self):
        self.collection = []  # collezione s di insiemi
        self.delegates = {}

    def get_dim(self):
        return len(self.collection)

    def make_set(self, x):
        s = LinkedList()
        s.add(x)
        self.collection.append(s)
        self.delegates[x] = x

    def find_set(self, x): # TODO: riscrivere/controllare dopo search in linked_list
        # for i in range(len(self.collection)):
        #     c = self.collection[i].search(x)
        #     if c is not None:
        #         return c.r
        # return None
        return self.delegates[x]

    def find_ll(self, x):
        for i in range(len(self.collection)):
            if self.collection[i].search(x) is not None:
                return self.collection[i]
        return None

    def union(self, x, y):
        #s = LinkedList()
        s_x = self.find_ll(x)
        s_y = self.find_ll(y)
        if s_x.size() < s_y.size():  # euristica unione pesata
            s = s_y.merge(s_x)
        else:
            s = s_x.merge(s_y)
        self.collection.append(s)
        self.collection.remove(s_x)
        self.collection.remove(s_y)


