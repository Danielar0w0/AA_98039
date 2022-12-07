from graph_utils import *


def generate_graphs(v=8):
    graph_id = 0

    for i in range(2, v + 1):

        n_vertices = 2 ** i

        for percentage in [12.5, 25, 50, 75]:
            vertices, edges = generate_vertices_edges(n_vertices, percentage)

            print("---")
            print("Number of vertices:", len(vertices))
            print("Number of edges:", len(edges))

            # print("Vertices:", vertices)
            # print("Edges:", edges)

            graph = draw_graph(vertices, edges)
            graph_data = nx.node_link_data(graph)
            # graph_data = nx.adjacency_data(graph)

            with open("graphs/graph_{}.json".format(graph_id), "w") as f:
                f.write(json.dumps(graph_data))

            graph_id += 1

    print("---")


def generate_SW_graphs():

    # Obtain graphs from folder
    folder_path = "SWgraphs"
    graphs_files = [f for f in os.listdir(folder_path) if isfile(join(folder_path, f)) and \
                    f.startswith("SW") and f.endswith(".txt")]

    for file in graphs_files:
        with open(folder_path + "/" + file, "r") as f:

            # Read if graph is directed or not
            directed = int(f.readline().strip()) == 1

            # Read if graph is weighted or not
            weighted = int(f.readline().strip()) == 1

            print(f"File: {file}, Directed: {directed}, Weighted: {weighted}")

            # Ignore graphs that aren't unweighted and undirected
            if weighted or directed:
                print("Graph is weighted and/or directed. Skipping...")
                continue

            # Read number of vertices
            n_vertices = int(f.readline().strip())

            if n_vertices > 20*20:
                print("Graph is too large (not enough coordinates)!")
                continue

            vertices = list(range(n_vertices))

            # Read number of edges
            n_edges = int(f.readline().strip())

            # Read edges
            edges = []
            for i in range(n_edges):
                edge = f.readline().strip().split()
                edges.append((int(edge[0]), int(edge[1])))

            print("Number of vertices:", len(vertices))
            print("Number of edges:", len(edges))

            # print("Vertices:", vertices)
            # print("Edges:", edges)

            # Create graph
            graph = draw_graph(vertices, edges)
            graph_data = nx.node_link_data(graph)

            with open("graphs/{}_graph.json".format(file.split(".")[0]), "w") as f:
                f.write(json.dumps(graph_data))


if __name__ == '__main__':
    # Generate graphs once
    generate_graphs(v)
    generate_SW_graphs()

