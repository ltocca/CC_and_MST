import random
import numpy as np


class Graph:
    def __init__(self, n_vertices, weight=False):
        self.w = weight
        self.v = np.arange(n_vertices)  # vettore contenente i vertici/nodi
        n = (n_vertices, n_vertices)
        self.adj = np.zeros(n)  # inizializzazione matrice di adiacenza
        self.edges = []  # inizializzazione vettore di archi

    def size(self):
        return self.v.size

    def get_edges(self):
        return self.edges

    def sort_edges(self):
        e = self.edges
        e.sort(key=lambda i: i[2])
        return e

    def populate_adj(self, prob):
        for i in range(self.adj.shape[0]):
            for j in range(i + 1, self.adj.shape[0]):
                v = 0
                p = (random.random() + (prob / 100))
                if p > 1 and self.w:
                    v = int(random.random() * 100)
                elif p > 1:
                    v = 1
                if v != 0:
                    self.adj[i][j] = v
                    self.adj[j][i] = v
                    self.edges.append([self.v[i], self.v[j], v])

    def clear_adj(self):
        s = self.size()
        self.adj = np.zeros(s)
        self.edges.clear()
