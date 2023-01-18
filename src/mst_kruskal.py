from graph import *
from union_find import *


def mst_kruskal(G):  # in questo caso ometto matrice dei pesi, le unisco in G (non definitivo)
    A = []
    uf = UnionFind()
    for v in range(G.size()):
        uf.make_set(v)
    e = G.sort_edges()
    count = 0
    for i in e:
        if uf.find_set(i[1]) is not uf.find_set(i[2]):
            A.append(i)
            uf.union(i[1], i[2])
            count += 1
            if count is G.size()-1:
                break
    return A

