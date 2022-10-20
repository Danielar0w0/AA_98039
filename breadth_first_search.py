from graph_utils import *


# --- Handle graphs

def generate_search_tree(graph, start):
    return nx.bfs_tree(graph, start)


def search(tree, edges):
    global operations_counter

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

        # Update operations counter
        operations_counter += 1

        # Update layer
        i += 1

    # Count number of crossed edges (between A and B)
    maximum_cut = 0
    for a in A:
        for b in B:
            if (a, b) in edges or (b, a) in edges:
                maximum_cut += 1

            # Update operations counter
            operations_counter += 1

    return A, B, maximum_cut


if __name__ == '__main__':

    graphs = load_graphs()
    for graph in graphs:

        operations_counter = 0

        # Get the largest connected component
        vertices = list(largest_connected_component(graph))

        # Use first vertex in the connected component as the root
        tree = generate_search_tree(graph, vertices[0])

        # for layer in tree:
        # print(layer, tree[layer])

        A, B, maximum_cut = search(tree, graph.edges)
        print("---")
        print(graph)
        print("A: ", A)
        print("B: ", B)
        print("Maximum Cut:", maximum_cut)

        print("Number of Operations:", operations_counter)
