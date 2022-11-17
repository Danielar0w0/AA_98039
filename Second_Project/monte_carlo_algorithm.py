from graph_utils import *
from utils.algorithm_utils import *
from itertools import combinations
import time

"""
    # First Implementation:
    # Generate subsets with random size
    size = np.random.randint(0, len(vertices) + 1)

    for subset in combinations(vertices, size):
        if np.random.randint(0, 2):
            break
"""

"""
    # Second Implementation:
    # Generate subsets with random size
    size = np.random.randint(0, len(vertices) + 1)

    # Get random subset
    n_subsets = math.comb(len(vertices), size)
    random_index = np.random.randint(0, n_subsets, dtype=np.int64)

    subset_idx = 0
    for subset in combinations(vertices, size):
        if subset_idx == random_index:
            break

        subset_idx += 1
"""


def monte_carlo_algorithm(graph, vertices, operations_limit=None, time_limit=None):

    global start
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

            # Update operations counter
            operations_counter += 1

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
        # operations_counter += 1

        # Update attempts counter
        attempts_counter += 1

        checked_partitions.append(partition)

        # Best possible solution
        if maximum_cut == len(graph.edges):
            break

        # Time has exceeded
        if time_limit and time.time() - start > time_limit:
            break

        # Number of operations has exceeded
        if operations_limit and operations_counter > operations_limit:
            break

    return A, B, maximum_cut


def generate_partitions(vertices):
    # Get all possible subsets
    subsets = []
    for i in range(0, len(vertices) + 1):
        subsets += list(combinations(vertices, i))

    # Get all possible partitions
    partitions = []
    for subset in subsets:
        partition = [list(subset), list(set(vertices) - set(subset))]
        partitions.append(partition)

    return partitions


if __name__ == '__main__':

    graphs = load_graphs()

    parameters = [(100000, None), (1000000, None), (None, 60), (100000, 60), (1000000, 60)]

    for i, param in enumerate(parameters):

        file = open("results/monte_carlo_algorithm" + str(i) + ".txt", "w")
        file.write(f"Time Limit: {param[1] or 0}s, Operations Limit: {param[0] or 0}\n")
        file.write(
            f"{'Graph':<12} {'Vertices':<12} {'Edges':<10} {'Maximum Cut':<15} {'Operations':<15} {'Attempts':<12} {'Time':<15}\n")

        for graph in graphs:

            operations_counter = 0
            attempts_counter = 0

            # Get relevant vertices
            vertices = list(remove_vertices_without_edges(graph))
            n_vertices = len(vertices)

            if not vertices:
                # print_results(graph, None, None, 0)
                continue

            start = time.time()
            A, B, maximum_cut = monte_carlo_algorithm(graph, vertices, param[0], param[1])
            end = time.time()

            # print_results(graph, A, B, maximum_cut)
            file.write(
                f"{len(graph.nodes):<12} {n_vertices:<12} {len(graph.edges):<10} {maximum_cut:<15} {operations_counter:<15} {attempts_counter:<12} {end - start:<15}\n")

        print("Done with", i)
        file.close()
