from timeit import default_timer as timer
from cc import cc
from mst_kruskal import *
import matplotlib.pyplot as plt


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
    n = 5  # numero iniziale di nodi 5
    p = 10  # probabilità di archi iniziale 10

    for i in range(1, 3):  # dovrebbe essere 13
        g = Graph(n, p)
        g.populate_adj(p)
        dfs_results.append(dfs_test(g))
        cc_results.append(cc_test(g))
        mst_results.append(mst_test(g))

        g = Graph(n, p)
        g.populate_adj(p, True)
        dfs_results_weighted.append(dfs_test(g))
        cc_results_weighted.append(cc_test(g))
        mst_results_weighted.append(mst_test(g))
        p += 5
        # n += int((n * i) / 4)
        n += 5

    x = np.arange(1, len(dfs_results) + 1) * 13
    plot_1 = plt.figure(1)
    plt.plot(x, dfs_results)
    plt.plot(x, dfs_results_weighted)
    plt.xlabel("Dimensione, probabilità")
    plt.ylabel("Tempo in s")
    plt.legend(["Non pesato", "Pesato"])
    plt.title("Confronto esecuzione DFS tra grafo pesato e non pesato")

    plot_2 = plt.figure(2)
    plt.plot(x, cc_results)
    plt.plot(x, cc_results_weighted)
    plt.xlabel("Dimensione, probabilità")
    plt.ylabel("Tempo in s")
    plt.legend(["Non pesato", "Pesato"])
    plt.title("Confronto esecuzione CC tra grafo pesato e non pesato")

    # plot_3 = plt.figure(3)
    # plt.plot(x, mst_results)
    # plt.plot(x, mst_results_weighted)
    # plt.xlabel("Dimensione, probabilità")
    # plt.ylabel("Tempo in s")
    # plt.legend(["Non pesato", "Pesato"])
    # plt.title("Confronto esecuzione MST tra grafo pesato e non pesato")

    plot_1.savefig('dfs.png')
    plot_2.savefig('cc.png')
    # plot_3.savefig('img/mst.png')


def main():
    test()


if __name__ == "__main__":
    main()
