from linked_list import *


class UnionFind:
    def __init__(self):
        self.collection = []  # collezione s di insiemi
        self.delegates = {}

    def get_dim(self):
        return len(self.collection)

    # def remove(self, c):
    #     self.delegates.pop(c.head.get_data())
    #     self.collection.remove(c)

    def make_set(self, x):
        s = LinkedList()
        s.add(x)
        self.collection.append(s)
        self.delegates[x.value] = x

    def find_set(self, x):
        # for i in range(len(self.collection)):
        #     c = self.collection[i].search(x)
        #     if c is not None:
        #         return c.r
        # return None
        return self.delegates[x.value]

    def find_ll(self, x):
        delegate = self.find_set(x)
        count = 0
        current = self.collection[count]
        while current.get_d() != delegate:
            count += 1
            if count < len(self.collection):
                current = self.collection[count]  # T#ODO: eccezione out of bounds
        return self.collection[count]

    def union(self, x, y):
        s_x = self.find_ll(x)
        s_y = self.find_ll(y)
        if s_x.size() < s_y.size():  # euristica unione pesata
            s_y.merge(s_x)
            self.collection.remove(s_x)

        else:
            s_x.merge(s_y)
            self.collection.remove(s_y)
