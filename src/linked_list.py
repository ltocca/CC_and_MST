class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.r = None  # rappresentante
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

    def set_head(self, h):
        self.head = h

    def get_head(self):
        return self.head

    def set_tail (self, t):
        self.tail = t

    def get_tail(self):
        return self.tail

    def is_empty(self):
        return self.head is None

    def add(self, item):  # inserimento in testa
        temp = Node(item)
        if self.is_empty():
            self.set_head(temp)
            self.set_tail(temp)
            temp.set_r(self)
        else:
            temp.set_next(self.head)
            self.set_head(temp)

    def search(self, v):  # TODO: riscrivere funzione search, non funziona
        if self.is_empty() is not True:
            n = self.head
            while n.get_next() is not None:
                if n.get_data() is v:
                    print("Node found!")
                    return n
                else:
                    n = n.get_next()
            print("Node not found!")
            return None

    def merge(self, ll):
        h = self.get_head()
        c = ll.get_head()
        self.tail.set_next(c)
        self.set_tail(ll.get_tail())
        while c.is_empty() is not True:
            c.r = h
            c = c.get_next()

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def clear(self):
        self.head = None
        self.tail = None


