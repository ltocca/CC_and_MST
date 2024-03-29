class Node:
    def __init__(self, init_data, r):
        self.data = init_data
        self.r = r  # rappresentante
        self.next = None  # successore

    # getters e setters non sono pythonic (forse sostituire con proprietà)
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def get_r(self):
        return self.r

    def set_r(self, r):
        self.r = r


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def set_head(self, h):
        self.head = h

    def get_head(self):
        return self.head

    def set_tail(self, t):
        self.tail = t

    def get_tail(self):
        return self.tail

    def is_empty(self):
        return self.head is None

    def get_d(self):  # ritorna il nodo rappresentante
        return self.head.get_r()

    def add(self, item):  # inserimento in testa
        if self.is_empty():
            temp = Node(item, item)
            temp.set_next(self.head)
            self.set_tail(temp)
            self.set_head(temp)
        else:
            temp = Node(item, self.get_head().get_d())
            temp.set_next(self.get_head())
            self.set_head(temp)
        self.size +=1

    def search(self, v):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == v:
                found = True
            else:
                current = current.get_next()
        return found

    def merge(self, ll):
        h = self.get_head()
        c = ll.get_head()
        self.tail.set_next(c)
        self.set_tail(ll.get_tail())
        while c is not None:
            c.r = h.r
            c = c.get_next()

    def clear(self):
        self.head = None
        self.tail = None
