from graph_utils import *


def generate_graphs(v=7):
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


if __name__ == '__main__':
    # Generate graphs once
    generate_graphs(v)
