import numpy as np


nMec = 98039


"""
def obtain_start(vertices, edges):

    # Obtain the start vertex of a graph.
    # Return the start vertex of the graph.

    global nMec
    np.random.seed(nMec)

    start = None
    while not start:
        vertex = vertices[np.random.randint(0, len(vertices))]
        if [edge for edge in edges if vertex in edge]:
            start = vertex

    return start
"""


def generate_search_tree(vertices, edges):

    # Generate the search tree of a graph.
    # Return the search tree of the graph.

    global nMec
    np.random.seed(nMec)

    queue = [vertices[np.random.randint(0, len(vertices))]]
    # queue = [obtain_start(vertices, edges)]
    # queue = [vertices[0]]

    visited = set()

    tree = {}
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited or (vertex[1], vertex[0]) not in visited:

            visited.add(vertex)

            next_vertices = [edge[1] for edge in edges if edge[0] == vertex]
            next_vertices += [edge[0] for edge in edges if edge[1] == vertex]

            next_vertices = set(next_vertices) - visited

            if next_vertices:
                tree[vertex] = next_vertices
                queue.extend(next_vertices)

    return tree, visited


def search(tree, edges):

    first_layer = list(tree.keys())[0]
    A = [first_layer]
    B = []

    i = 0
    for layer in tree:
        # print(layer, tree[layer])
        if i % 2 != 0:
            vertices = [vertex for vertex in tree[layer]]
            A += vertices
        else:
            vertices = [vertex for vertex in tree[layer]]
            B += vertices
        i += 1

    # Count number of crossed edges (between A and B)
    maximum_cut = 0
    for a in A:
        for b in B:
            if (a, b) in edges or (b, a) in edges:
                maximum_cut += 1

    return A, B, maximum_cut


if __name__ == '__main__':

    vertices = [(5, 3), (12, 15), (11, 19), (3, 17), (7, 12), (16, 12), (11, 15), (12, 16), (20, 6), (10, 14)]
    edges = [((16, 12), (5, 3)), ((7, 12), (10, 14)), ((20, 6), (10, 14)), ((20, 6), (12, 16)), ((11, 19), (16, 12))]

    all_visited = set()
    trees = []

    while all_visited != set(vertices):

        current_vertices = list(set(vertices) - all_visited)
        tree, visited = generate_search_tree(current_vertices, edges)

        trees.append(tree)
        all_visited.update(visited)

    # tree, visited = generate_search_tree(vertices, edges)
    # not_visited = set(vertices) - visited

    print("Vertices:", vertices)
    print("Edges:", edges)
    print("Trees:")

    final_tree = {}
    for tree in trees:
        if not final_tree or len(tree) > len(final_tree):
            final_tree = tree
        print("-", tree)

    print("Largest sub-tree:", final_tree)

    # print("Tree:\n", tree)
    # print("Visited:", visited)
    # print("Not visited:", not_visited)

    A, B, maximum_cut = search(final_tree, edges)
    print("A: ", A)
    print("B: ", B)
    print("Maximum Cut:", maximum_cut)
