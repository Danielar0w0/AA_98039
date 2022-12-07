from graph_utils import *
from utils.algorithm_utils import *
import time


def greedy_search(graph, vertices):

    global operations_counter
    global attempts_counter

    A = vertices
    B = []

    current_cut = count_cut(graph, [A, B])  # Current cut: 0
    improvement = True  # First time

    while improvement:

        improvement = False

        for vertex in vertices:

            if vertex in A:
                # temp_A = A.copy()
                # temp_A.remove(vertex)
                temp_A = [v for v in A if v != vertex]

                # A can't be empty
                if not temp_A:
                    continue

                # If moving vertex from A to B improves the cut
                if count_cut(graph, [temp_A, B]) < count_cut(graph, [A, B + [vertex]]) \
                        and count_cut(graph, [A, B + [vertex]]) > current_cut:
                    A.remove(vertex)
                    B.append(vertex)

                    # Update current cut and set improvement to True
                    current_cut = count_cut(graph, [A, B])
                    improvement = True

            elif vertex in B:
                # temp_B = B.copy()
                # temp_B.remove(vertex)
                temp_B = [v for v in B if v != vertex]

                # B can't be empty
                if not temp_B:
                    continue

                # If moving vertex from B to A improves the cut
                if count_cut(graph, [A, temp_B]) < count_cut(graph, [A + [vertex], B]) \
                        and count_cut(graph, [A + [vertex], B]) > current_cut:
                    A.append(vertex)
                    B.remove(vertex)

                    # Update current cut and set improvement to True
                    current_cut = count_cut(graph, [A, B])
                    improvement = True

            # Update operations counter
            # 2 comparisons per iteration
            operations_counter += 2

            # Update attempts counter
            attempts_counter += 1

    return A, B, count_cut(graph, [A, B])


if __name__ == '__main__':

    graphs = load_graphs()
    file = open("results/greedy_algorithm.txt", "w")
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

        start = time.time()
        A, B, maximum_cut = greedy_search(graph, vertices)
        end = time.time()

        print_results(graph, A, B, maximum_cut)
        file.write(f"{len(graph.nodes):<12} {n_vertices:<12} {len(graph.edges):<10} {maximum_cut:<15} {operations_counter:<15} {attempts_counter:<12} {end - start:<15}\n")

    file.close()
