from union_find import *


def cc(G):
    uf = UnionFind()
    for v in G.v:
        uf.make_set(v)
    for i in G.edges:
        if uf.find_set(i[0]) is not uf.find_set(i[1]):
            uf.union(i[0], i[1])
    return uf
