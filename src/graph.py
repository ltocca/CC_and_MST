import numpy as np


BLACK = 'BLACK'
GREY = 'GREY'
WHITE = 'WHITE'


class Vertex: # o la chiamo nodo?
    def __init__(self, v):
        self.value = v
        self.colour = WHITE  # al momento della creazione il vertice non è ancora stato scorperto -> bianco
        self.d = None  # tempo di scoperta del vertice
        self.f = None  # tempo completamento visita del vertice
        self.p = None  # predecessore

    def set_colour(self, colour):
        self.colour = colour


class Graph:
    def __init__(self, n_vertices):
        v = []  # vettore contenente i vertici/nodi
        for j in n_vertices:
            v.append(Vertex(j))
        adj = np.zeros(n_vertices)  # inizializzazione matrice di adiacenza
