from graph_utils import *
from itertools import combinations


def exhaustive_search(graph, vertices):

    global operations_counter

    # Get all possible subsets
    subsets = []
    for i in range(1, len(vertices) + 1):
        subsets += list(combinations(vertices, i))

        # Update operations counter
        operations_counter += 1

    # Get all possible partitions
    partitions = []
    for subset in subsets:
        partition = [list(subset), list(set(vertices) - set(subset))]
        partitions.append(partition)

        # Update operations counter
        operations_counter += 1

    # Get the maximum cut for each partition
    maximum_cut = 0
    A = B = None
    for partition in partitions:
        cut = count_cut(graph, partition)
        if cut > maximum_cut:
            maximum_cut = cut
            A = partition[0]
            B = partition[1]

    return A, B, maximum_cut


def count_cut(graph, partition):

    global operations_counter

    # Count number of crossed edges (between A and B)
    maximum_cut = 0
    for a in partition[0]:
        for b in partition[1]:
            if (a, b) in graph.edges or (b, a) in graph.edges:
                maximum_cut += 1

            # Update operations counter
            operations_counter += 1

    return maximum_cut


if __name__ == '__main__':

    graphs = load_graphs()
    for graph in graphs:

        operations_counter = 0

        # Get the largest connected component
        vertices = list(largest_connected_component(graph))

        A, B, maximum_cut = exhaustive_search(graph, vertices)

        print("---")
        print(graph)
        print("A: ", A)
        print("B: ", B)
        print("Maximum Cut:", maximum_cut)

        print("Number of Operations:", operations_counter)
