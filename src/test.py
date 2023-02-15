from timeit import default_timer as timer
from cc import cc
from mst_kruskal import *
import matplotlib.pyplot as plt


def cc_test(g):
    start = timer()
    conn_comp = cc(g)
    end = timer()
    return [conn_comp.get_dim(), round(end - start, 6)]


def mst_test(g):
    start = timer()
    mst = mst_kruskal(g)
    end = timer()
    return [len(mst), round(end - start, 6)]


def test():
    cc_results = []
    cc_results_time = []
    mst_results = []
    mst_results_time = []
    cc_results_weighted = []
    cc_results_time_weighted = []
    mst_results_weighted = []
    mst_results_time_weighted = []
    n = 5  # numero iniziale di nodi 5
    p = 10  # probabilità di archi iniziale 10

    for i in range(0, 10):  # dovrebbe essere 13
        g = Graph(n)
        g.populate_adj(p)
        comp = cc_test(g)
        cc_results.append(comp[0])
        cc_results_time.append(comp[1])
        mst = mst_test(g)
        mst_results.append(mst[0])
        mst_results_time.append(mst[1])

        g = Graph(n, True)
        g.populate_adj(p)
        comp = cc_test(g)
        cc_results_weighted.append(comp[0])
        cc_results_time_weighted.append(comp[1])
        mst = mst_test(g)
        mst_results_weighted.append(mst[0])
        mst_results_time_weighted.append(mst[1])
        p += 5
        # n += int((n * i) / 4)
        n += 5

    x = np.arange(1, len(mst_results_time) + 1)*10
    plot_1 = plt.figure(1)
    plt.plot(x, cc_results)
    plt.plot(x, mst_results)
    plt.xlabel("Dimensione, probabilità")
    plt.ylabel("Numero di Mst e CC")
    plt.legend(["cc", "mst"])
    plt.title("Confronto esecuzione CC e MST con grafo non pesato")

    plot_2 = plt.figure(2)
    plt.plot(x, cc_results_weighted)
    plt.plot(x, mst_results_weighted)
    plt.xlabel("Dimensione, probabilità")
    plt.ylabel("Numero di MST e Componenti connesse")
    plt.legend(["CC", "MST"])
    plt.title("Confronto esecuzione CC e MST con grafo pesato")

    plot_3 = plt.figure(3)
    plt.plot(x, cc_results_time)
    plt.plot(x, mst_results_weighted)
    plt.xlabel("Dimensione, probabilità")
    plt.ylabel("Tempo in s")
    plt.legend(["Componente connesse", "mst"])
    plt.title("Confronto temporale esecuzione CC e MST")

    plot_1.savefig('img/cc_mst.png')
    plot_2.savefig('img/cc_mst_w.png')
    plot_3.savefig('img/time.png')
    plt.clf()


def main():
    test()


if __name__ == "__main__":
    main()
