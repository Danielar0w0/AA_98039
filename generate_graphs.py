import json

import networkx as nx

from graph_utils import *

v = 2


def generate_graphs():

    global v
    graph_id = 0

    for i in range(2, v + 1):

        n_vertices = 2 ** i

        for percentage in [12.5, 25, 50, 75]:
            vertices, edges = generate_vertices_edges(n_vertices, percentage)

            print("---")
            print("Number of vertices:", len(vertices))
            print("Number of edges:", len(edges))

            print("Vertices:", vertices)
            print("Edges:", edges)

            graph = draw_graph(vertices, edges)
            graph_data = nx.node_link_data(graph)
            # graph_data = nx.adjacency_data(graph)

            with open("graphs/graph_{}.json".format(graph_id), "w") as f:
                f.write(json.dumps(graph_data))

            graph_id += 1


def load_graphs():

    global v
    graphs = []

    n_graphs = (v-2+1)*4

    for i in range(n_graphs):
        with open("graphs/graph_{}.json".format(i), "r") as f:
            graph_data = json.loads(f.read())
            print(type(graph_data))

            graphs.append(nx.node_link_graph(graph_data))
            # graphs.append(nx.adjacency_graph(graph_data))

    return graphs


if __name__ == '__main__':

    # Generate graphs once
    generate_graphs()