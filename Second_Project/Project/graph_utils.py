import networkx as nx
from networkx import Graph
import matplotlib.pyplot as plt
import numpy as np
import math
import json
import os
from os.path import isfile, join

# Graph vertices are 2D points on the XOY plane, with integer valued coordinates between 1 and 20.
# Graph vertices should neither be coincident nor too close.
# The number of edges sharing a vertex is randomly determined.

# Generate successively larger random graphs, with 4, 5, 6, … vertices, using your student number as seed.
# Use 12.5%, 25%, 50% and 75% of the maximum number of edges for the number of vertices.

nMec = 98039
v = 8


# --- Handle vertices and edges

def generate_vertices_edges(v, p):
    """
    Generate a random graph with n vertices and n * (p/100) edges.
    Return the list of vertices and the list of edges.

    v - Number of vertices
    p - Percentage of the maximum number of edges
    """

    global nMec
    np.random.seed(nMec)
    # e = math.floor(v * p / 100)
    e = math.floor((v * (v - 1) / 2) * (p / 100))

    vertices = []
    while len(vertices) < v:
        x = np.random.randint(1, 21)
        y = np.random.randint(1, 21)
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


def is_connected(vertices, edges):
    """
    Check if a graph is connected.
    Return True if the graph is connected, False otherwise.
    """

    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    graph.add_edges_from(edges)

    return nx.is_connected(graph)


def adjacency_matrix(vertices, edges):
    """
    Generate the adjacency matrix of a graph.
    Return the adjacency matrix of the graph.
    """

    n = len(vertices)
    matrix = np.zeros((n, n), dtype=int)

    for edge in edges:
        v1 = vertices.index(edge[0])
        v2 = vertices.index(edge[1])
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1

    return matrix


def incidence_matrix(vertices, edges):
    """
    Generate the incidence matrix of a graph.
    Return the incidence matrix of the graph.
    """

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


def store_vertices_and_edges(vertices, edges):
    """Store a graph in a file."""

    with open('graph.txt', 'w') as file:
        file.write('Vertices: ' + str(vertices))
        file.write('Edges: ' + str(edges))


# --- Handle graphs

def draw_graph(vertices, edges):
    """
    Generate a networkx graph and display it.
    """

    graph = nx.Graph()

    # graph.add_nodes_from(vertices)
    # graph.add_edges_from(edges)

    vertices_ids = [i for i in range(len(vertices))]
    edges_ids = [(i, j) for i in vertices_ids for j in vertices_ids if (vertices[i], vertices[j]) in edges]

    graph.add_nodes_from(vertices_ids)
    graph.add_edges_from(edges_ids)

    # Plot the graph
    # positions = {i: vertices[i] for i in vertices_ids}
    # nx.draw(graph, node_color='orange', edge_color='red', with_labels=True, pos=positions)
    # plt.show()

    return graph


def is_connected(graph: Graph):
    """
    Check if a graph is connected.
    Return True if the graph is connected, False otherwise.
    """

    return nx.is_connected(graph)


def is_bipartite(graph: Graph):
    """
    Check if a graph is bipartite.
    Return True if the graph is bipartite, False otherwise.
    """

    return nx.is_bipartite(graph)


def number_of_connected_components(graph: Graph):
    """Return the number of connected components of a graph."""

    return nx.number_connected_components(graph)


def connected_components(graph: Graph):
    """Return the connected components of a graph."""

    return list(nx.connected_components(graph))


def largest_connected_component(graph: Graph):
    """Return the largest connected component of a graph."""
    for c in nx.connected_components(graph):
        print(c)

    return max(nx.connected_components(graph), key=len)


def remove_vertices_without_edges(graph: Graph):
    """Remove vertices without edges."""
    return graph.subgraph([v for v in graph if graph.degree(v) > 0])


def adjacency_data(graph: Graph):
    """Generate the adjacency matrix of a graph."""

    return nx.adjacency_data(graph)


def obtain_graph(adjacency_data):
    """Obtain a graph from adjacency data."""
    return nx.adjacency_graph(adjacency_data)


def print_matrix(matrix):
    """Print a matrix in a readable format."""
    for line in matrix:
        print('  '.join(map(str, line)))


def load_graphs():
    global v
    graphs = []

    n_graphs = (v - 2 + 1) * 4

    for i in range(n_graphs):
        with open("graphs/graph_{}.json".format(i), "r") as f:
            graph_data = json.loads(f.read())

            graphs.append(nx.node_link_graph(graph_data))
            # graphs.append(nx.adjacency_graph(graph_data))

    return graphs


def load_SW_graphs():

    folder_path = "graphs"
    graphs_files = [f for f in os.listdir(folder_path) if isfile(join(folder_path, f)) and \
                    f.startswith("SW") and f.endswith(".json")]

    graphs = []
    for file in graphs_files:
        with open(folder_path + "/" + file, "r") as f:
            graph_data = json.loads(f.read())

            graphs.append(nx.node_link_graph(graph_data))

    return graphs


if __name__ == '__main__':
    n_vertices = 10
    percentage = 50

    vertices, edges = generate_vertices_edges(n_vertices, percentage)

    print("Vertices:", vertices)
    print("Edges:", edges)

    """
    # Vertices and edges handling
    matrix = adjacency_matrix(vertices, edges)
    print("Adjacency matrix")
    print_matrix(matrix)

    matrix = incidence_matrix(vertices, edges)
    print("Incidence matrix:")
    print_matrix(matrix)
    """

    graph = draw_graph(vertices, edges)
    print("Graph is connected:", is_connected(graph))

    print("Number of connected components:", number_of_connected_components(graph))
    print("Connected components:", connected_components(graph))
    print("Largest connected component:", largest_connected_component(graph))

    graph_data = adjacency_data(graph)
    print("Adjacency data")
    print(graph_data)

    graph = obtain_graph(graph_data)
    print("Obtained graph:", graph)
