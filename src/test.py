from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys
from src.graph import Graph
from cc import cc
from mst_kruskal import *


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
    sizes = [2 ** i for i in range(0, 13)]  # array numero nodi nel grafo
    probs = [20, 40, 60, 80, 100]  # array di probabilità in %
    cc_data = {p: [] for p in probs}
    mst_data = {p: [] for p in probs}
    for s in sizes:
        for p in probs:
            file_name = "size=" + str(s) + "_p=" + str(p).replace(".", "") + ".dat"
            g = Graph(s, True)
            g.populate_adj(p)

            with open("data/in_" + file_name, "wb") as f:
                pickle.dump(g, f)

            cc = cc_test(g)
            cc_data[p].append((s, cc[1], cc[0]))

            if cc[0] == 1:
                mst = mst_test(g)
                mst_data[p].append((s, mst[1], mst[0]))
            else:
                mst_data[p].append((s, None, None))

            with open("data/out_cc_" + file_name, "wb") as f:
                pickle.dump(cc[0], f)

            if cc[0] == 1:
                with open("data/out_mst_" + file_name, "wb") as f:
                    pickle.dump(mst[0], f)

    with open("data/cc_overall.dat", "wb") as f:
        pickle.dump(cc_data, f)
    with open("data/mst_overall.dat", "wb") as f:
        pickle.dump(mst_data, f)

    # parte di plot

    for p in probs:
        plt.clf()

        # Size-time ccs
        plt.plot([rec[0] for rec in cc_data[p]], [rec[1] for rec in cc_data[p]])
        plt.xlabel("Size")
        plt.ylabel("Time(s)")
        plt.savefig("../img/cc/cc_time_p=" + str(p).replace(".", "") + ".png")

        # Size-Number of ccs
        plt.clf()

        plt.plot([rec[0] for rec in cc_data[p]], [rec[2] for rec in cc_data[p]])
        plt.xlabel("Size")
        plt.ylabel("Componenti connesse")
        plt.savefig("../img/cc/cc_number_p=" + str(p).replace(".", "") + ".png")

        # Size-time Kruskal
        plt.clf()

        plt.plot([rec[0] for rec in mst_data[p] if rec[1] is not None],
                 [rec[1] for rec in mst_data[p] if rec[1] is not None])
        plt.xlabel("Size")
        plt.ylabel("Time(s)")
        plt.savefig("../img/mst/mst_time_p=" + str(p).replace(".", "") + ".png")



def main():
    test()


if __name__ == "__main__":
    main()
