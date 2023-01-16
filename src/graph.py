import random

import numpy as np

BLACK = 'BLACK'
GREY = 'GREY'
WHITE = 'WHITE'


class Vertex:  # o la chiamo nodo?
    def __init__(self, v):
        self.value = v
        self.colour = WHITE  # al momento della creazione il vertice non è ancora stato scoperto -> bianco
        self.d = None  # tempo di scoperta del vertice
        self.f = None  # tempo completamento visita del vertice
        self.p = None  # predecessore

    def set_colour(self, colour):
        self.colour = colour


class Graph:
    def __init__(self, n_vertices, probability):
        self.v = []  # vettore contenente i vertici/nodi
        self.t = 0
        for j in n_vertices:
            self.v.append(Vertex(j))
        self.adj = np.zeros(n_vertices)  # inizializzazione matrice di adiacenza
        self.edges = []  # inizializzazione vettore di archi

    def add_vertex(self, value):
        if value in self.v:
            return print("Vertex already present")
        self.v.append(Vertex(value))

    def populate_adj(self, prob, weight):
        for i in range(self.adj.size):
            for j in range(self.adj.size):
                v = 0
                if (random.random() + (prob / 100)) > 1 and weight:
                    v = random.random() * 100
                self.adj[i, j] = v
                #self.edges.append([i, j, v])

    def dfs(self, sort = False):
        for u in self.v:
            u.set_colour(WHITE)
            u.p = None
        self.t = 0
        if sort:
            #tmp = self.v
            #tmp.sort(key=lambda tmp: tmp.f, reverse = True)
            self.v.sort (key = lambda v: v.f, reverse = True)
        for u in self.v:
            if u.colour is WHITE:
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.t += 1
        u.d = self.t
        u.set_colour(GREY)
        for v in self.adj[u]:
            if v.colour is WHITE:
                v.p = u
                self.dfs_visit(v)
        u.set_colour(BLACK)
        self.t += 1
        u.f = self.t

    def transpose(self):
        t = self
        t.adj.transpose()
        return t

    def scc(self):
        self.dfs()
        gt = self.transpose()
        gt.dfs(True)

        scc_found = set()
        scc_queue = []
        for v in gt.v:

