from timeit import default_timer as timer
from cc import cc
from mst_kruskal import *


def dfs_test(g):
    start = timer()
    g.dfs()
    end = timer()
    return round(end - start, 6)


def cc_test(g):
    start = timer()
    conn_comp = cc(g)
    end = timer()
    return [conn_comp.get_dim(), round(end - start, 6)]


def mst_test(g):
    start = timer()
    mst = mst_kruskal(g)
    end = timer()
    return [mst, round(end - start, 6)]


def test():
    dfs_results = []
    cc_results = []
    mst_results = []
    dfs_results_weighted = []
    cc_results_weighted = []
    mst_results_weighted = []
    n = 5  # numero iniziale di nodi
    p = 10  # probabilità di archi iniziale

    for i in range(1, 13):
        g = Graph(n, p)
        g.populate_adj(p)
        dfs_results.append(dfs_test(g))
        cc_results.append(cc_test(g))
        mst_results.append(mst_test(g))

        g.clear_adj()
        g.populate_adj(p, True)
        dfs_results_weighted.append(dfs_test(g))
        cc_results_weighted.append(cc_test(g))
        mst_results_weighted.append(mst_test(g))
        p += 5
        n += int(n*i/4)

