from graph_utils import *
from algorithm_utils import *
import networkx as nx
import time


# --- Handle graphs

def generate_search_tree(graph, start):
    return nx.bfs_tree(graph, start)


def search(graph, tree):

    global operations_counter
    global attempts_counter

    first_layer = list(tree)[0]

    A = [first_layer]
    B = []

    i = 0
    for layer in tree:

        if i % 2 != 0:
            vertices = [vertex for vertex in tree[layer]]
            A += vertices
        else:
            vertices = [vertex for vertex in tree[layer]]
            B += vertices

        # Update layer
        i += 1

    # Count number of crossed edges (between A and B)
    # maximum_cut = nx.cut_size(graph, A, B)
    maximum_cut = count_cut(graph, [A, B])

    # Update operations counter
    operations_counter += 1

    # Update attempts counter
    attempts_counter += 1

    return A, B, maximum_cut


if __name__ == '__main__':

    graphs = load_graphs()
    file = open("breadth_first_search.txt", "w")
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
        # Use first vertex in the connected component as the root
        tree = generate_search_tree(graph, vertices[0])

        A, B, maximum_cut = search(graph, tree)
        end = time.time()

        print_results(graph, A, B, maximum_cut)
        file.write(
            f"{len(graph.nodes):<12} {n_vertices:<12} {len(graph.edges):<10} {maximum_cut:<15} {operations_counter:<15} {attempts_counter:<12} {end - start:<15}\n")

    file.close()
