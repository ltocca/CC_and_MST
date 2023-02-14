from graph import *
from union_find import *


def mst_kruskal(G):  # in questo caso ometto matrice dei pesi, le unisco in G (non definitivo)
    A = []
    uf = UnionFind()
    for v in G.v:
        uf.make_set(v)
    e = G.sort_edges()
    count = 0
    for i in e:
        if uf.find_set(i[0]) is not uf.find_set(i[1]):
            A.append(i)
            uf.union(i[0], i[1])
            count += 1
    return A

