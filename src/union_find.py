from linked_list import *


class UnionFind:
    def __init__(self):
        self.collection = []  # collezione s di insiemi
        #self.delegates = {}

    def make_set(self, x):
        s = LinkedList()
        s.add(x)
        self.collection.append(s)
        #self.delegates[x] = s

    def find_set(self, x):
        return x.r

    def find_ll(self, x):
        for i in range(len(self.collection)):
            if self.collection[i].search(x) is not None:
                return self.collection[i]
        return None

    def union(self, x, y):
        s = LinkedList()
        s_x = self.find_ll(x)
        s_y = self.find_ll(y)
        if s_x.size() < s_y.size():  # euristica unione pesata
            s = s_y.merge(s_x)
        else:
            s = s_x.merge(s_y)
        self.collection.append(s)
        self.collection.remove(s_x)
        self.collection.remove(s_y)


