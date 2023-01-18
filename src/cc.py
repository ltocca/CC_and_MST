from union_find import *

def cc(G):
    uf = UnionFind()
    for v in range(G.size()):
        uf.make_set(v)
    for i in range(G.size):
        for j in range (G.size):
            if uf.find_set(i) is not uf.find_set(j):
                uf.union(i, j)
    return uf
