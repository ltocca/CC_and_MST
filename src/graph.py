import random

import numpy as np

BLACK = 'BLACK'
GREY = 'GREY'
WHITE = 'WHITE'


class Vertex:  # o la chiamo nodo?
    def __init__(self, v):
        self.value = v
        self.colour = WHITE  # al momento della creazione il vertice non è ancora stato scorperto -> bianco
        self.d = None  # tempo di scoperta del vertice
        self.f = None  # tempo completamento visita del vertice
        self.p = None  # predecessore

    def set_colour(self, colour):
        self.colour = colour


class Graph:
    def __init__(self, n_vertices, probability):
        self.v = []  # vettore contenente i vertici/nodi
        for j in n_vertices:
            self.v.append(Vertex(j))
        self.adj = np.zeros(n_vertices)  # inizializzazione matrice di adiacenza

    def add_vertex(self, value):
        if value in self.v:
            return print("Vertex already present")
        self.v.append(Vertex(value))

    def populate_adj(self, prob, weight):
        for i in range(self.adj.size):
            for j in range(self.adj.size):
                v = 1
                if (random.random() + (prob/100)) > 1 and weight:
                    v = random.random() * 100
                self.adj[i, j] = v

    # def dfs(self, ):