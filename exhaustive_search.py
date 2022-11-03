from graph_utils import *
from algorithm_utils import *
from itertools import combinations
import time


def exhaustive_search(graph, vertices):
    global operations_counter
    global attempts_counter

    # Get all possible partitions
    partitions = []

    for i in range(0, (len(vertices) // 2) + 1):
        subsets = list(combinations(vertices, i))

        for subset in subsets:
            partitions.append([list(subset), list(set(vertices) - set(subset))])

            # Update operations counter
            operations_counter += 1

    """
    # Without optimization
    subsets = []
    for i in range(0, len(vertices) + 1):
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
    """

    # Get the maximum cut for each partition
    maximum_cut = 0
    A = B = None
    for partition in partitions:
        cut = count_cut(graph, partition)
        # cut = nx.cut_size(graph, partition[0], partition[1])
        if cut > maximum_cut:
            maximum_cut = cut
            A = partition[0]
            B = partition[1]

        # Update operations counter
        operations_counter += 1

        # Update attempts counter
        attempts_counter += 1

    return A, B, maximum_cut


if __name__ == '__main__':

    graphs = load_graphs()
    file = open("exhaustive_search.txt", "w")
    file.write(f"{'Graph':<12} {'Vertices':<12} {'Edges':<10} {'Maximum Cut':<15} {'Operations':<15} {'Attempts':<12} {'Time':<15}\n")

    for graph in graphs:

        operations_counter = 0
        attempts_counter = 0

        # Get relevant vertices
        vertices = list(remove_vertices_without_edges(graph))
        n_vertices = len(vertices)

        if not vertices:
            print_results(graph, None, None, 0)
            continue

        # Graph is two large (Throws MemoryError)
        if len(vertices) > 16:
            break

        start = time.time()
        A, B, maximum_cut = exhaustive_search(graph, vertices)
        end = time.time()

        print_results(graph, A, B, maximum_cut)
        file.write(f"{len(graph.nodes):<12} {n_vertices:<12} {len(graph.edges):<10} {maximum_cut:<15} {operations_counter:<15} {attempts_counter:<12} {end - start:<15}\n")

    file.close()

