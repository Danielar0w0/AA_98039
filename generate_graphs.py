import numpy as np
import math

# Graph vertices are 2D points on the XOY plane, with integer valued coordinates between 1 and 20.
# Graph vertices should neither be coincident nor too close.
# The number of edges sharing a vertex is randomly determined.

# Generate successively larger random graphs, with 4, 5, 6, … vertices, using your student number as seed.
# Use 12.5%, 25%, 50% and 75% of the maximum number of edges for the number of vertices.


def generate_graph(seed, v, p):

    # Generate a random graph with n vertices and n * (p/100) edges.
    # Return the list of vertices and the list of edges.

    # v - Number of vertices
    # p - Percentage of the maximum number of edges

    np.random.seed(seed)
    e = math.floor(v * p / 100)

    vertices = []
    while len(vertices) < v:
        x = np.random.randint(1, 20)
        y = np.random.randint(1, 20)
        if (x, y) not in vertices:
            vertices.append((x, y))

    edges = []
    while len(edges) < e:
        v1 = np.random.randint(0, v)
        v2 = np.random.randint(0, v)

        if v1 != v2 and (vertices[v1], vertices[v2]) not in edges and (vertices[v2], vertices[v1]) not in edges:
            edge = (vertices[v1], vertices[v2])
            edges.append(edge)

    return vertices, edges


def adjacency_matrix(vertices, edges):

    # Generate the adjacency matrix of a graph.
    # Return the adjacency matrix of the graph.

    n = len(vertices)
    matrix = np.zeros((n, n), dtype=int)

    for edge in edges:
        v1 = vertices.index(edge[0])
        v2 = vertices.index(edge[1])
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1

    return matrix


def incidence_matrix(vertices, edges):

    # Generate the incidence matrix of a graph.
    # Return the incidence matrix of the graph.

    n = len(vertices)
    m = len(edges)
    matrix = np.zeros((n, m), dtype=int)

    for i in range(m):
        edge = edges[i]
        v1 = vertices.index(edge[0])
        v2 = vertices.index(edge[1])
        matrix[v1][i] = 1
        matrix[v2][i] = 1

    return matrix


def print_matrix(matrix):

    # Print a matrix in a readable format.
    for line in matrix:
        print('  '.join(map(str, line)))


if __name__ == '__main__':
    # Generate graphs for the 4 cases and save them to files.
    nMec = 98039
    n_vertices = 2
    percentage = 50

    vertices, edges = generate_graph(nMec, n_vertices, percentage)

    print("Vertices:", vertices)
    print("Edges:", edges)

    matrix = adjacency_matrix(vertices, edges)
    print("Adjacency matrix")
    print_matrix(matrix)

    matrix = incidence_matrix(vertices, edges)
    print("Incidence matrix:")
    print_matrix(matrix)

