from graph_utils import *
from utils.algorithm_utils import *
import time


def las_vegas_algorithm(graph, vertices):
    global operations_counter
    global attempts_counter

    maximum_cut = 0
    A = B = None

    # Ensure that no solutions are tested more than once
    checked_partitions = []

    # len(partitions) = 2^n
    while len(checked_partitions) < 2 ** len(vertices):

        # Generate subsets with random size
        size = np.random.randint(0, len(vertices) + 1)

        # Generate subset with random vertices
        subset = []
        while len(subset) != size:
            random_index = np.random.randint(0, len(vertices))
            if vertices[random_index] not in subset:
                subset.append(vertices[random_index])

        # Get random partition
        partition = [list(subset), list(set(vertices) - set(subset))]

        if partition in checked_partitions:
            continue

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

        checked_partitions.append(partition)

    return A, B, maximum_cut


if __name__ == '__main__':

    graphs = load_graphs()
    file = open("results/las_vegas_algorithm.txt", "w")
    file.write(
        f"{'Graph':<12} {'Vertices':<12} {'Edges':<10} {'Maximum Cut':<15} {'Operations':<15} {'Attempts':<12} {'Time':<15}\n")

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
        A, B, maximum_cut = las_vegas_algorithm(graph, vertices)
        end = time.time()

        print_results(graph, A, B, maximum_cut)
        file.write(
            f"{len(graph.nodes):<12} {n_vertices:<12} {len(graph.edges):<10} {maximum_cut:<15} {operations_counter:<15} {attempts_counter:<12} {end - start:<15}\n")

    file.close()
