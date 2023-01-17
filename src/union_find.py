from linked_list import *

class UnionFind:
    def __init__(self):
        self.collection = []
        self.delegates = {}

    def make_set(self, x):
        s = LinkedList()
        s.add(x)
        self.collection.append(s)
        self.delegates[x] = s

    def find_set(self, x):
        return self.delegates[x.get_r()]

    def find_ll(self, x):
         for i in range(len(self.collection)):
             if self.collection[i].search(x) is not None:
                return self.collection[i]
         return None
