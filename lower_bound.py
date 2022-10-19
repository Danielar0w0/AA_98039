import math
from graph_utils import *


"""
def lower_bound(v, e, connected=False):

    # Formulas: https://en.wikipedia.org/wiki/Maximum_cut
    # A graph must have at least v+1 edges to be connected
    if connected:
        return (e / 2) + (v - 1)/4

    return (e / 2) + (math.sqrt(2*e + 1/2) - 1/4) / 4
"""


def lower_bound(graph):

    # Formulas: https://en.wikipedia.org/wiki/Maximum_cut
    # A graph must have at least v+1 edges to be connected

    e = len(graph.edges)
    return (e / 2) + (math.sqrt(2 * e + 1 / 2) - 1 / 4) / 4


if __name__ == '__main__':

    graphs = load_graphs()
    for graph in graphs:
        print("---")
        print(graph)
        print("Lower Bound:", lower_bound(graph))
