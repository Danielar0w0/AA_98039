def count_cut(graph, partition):

    # Count number of crossed edges (between A and B)
    maximum_cut = 0
    for a in partition[0]:
        for b in partition[1]:
            if (a, b) in graph.edges or (b, a) in graph.edges:
                maximum_cut += 1

    return maximum_cut


def print_results(graph, A, B, maximum_cut):

    print("---")
    print("Number of vertices:", len(graph))
    print("Number of edges:", len(graph.edges))

    # print("Vertices:", list(graph))
    # print("Edges:", list(graph.edges))

    print("A: ", A)
    print("B: ", B)
    print("Maximum cut:", maximum_cut)