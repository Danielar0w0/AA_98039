from graph_utils import *
from utils.algorithm_utils import *
import time


def randomized_algorithm(graph, vertices):

    global operations_counter
    global attempts_counter

    maximum_cut = 0
    A = B = None

    return maximum_cut, A, B


if __name__ == '__main__':

    graphs = load_graphs()
    file = open("results/randomized_algorithm.txt", "w")
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
        A, B, maximum_cut = randomized_algorithm(graph, vertices)
        end = time.time()

        print_results(graph, A, B, maximum_cut)
        file.write(
            f"{len(graph.nodes):<12} {n_vertices:<12} {len(graph.edges):<10} {maximum_cut:<15} {operations_counter:<15} {attempts_counter:<12} {end - start:<15}\n")

    file.close()
