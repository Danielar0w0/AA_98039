from graph_utils import *
from itertools import combinations


def exhaustive_search(graph, vertices):

        # Get all possible subsets
        subsets = []
        for i in range(1, len(vertices)+1):
            subsets += list(combinations(vertices, i))

        # Get all possible partitions
        partitions = []
        for subset in subsets:
            partition = [list(subset), list(set(vertices) - set(subset))]
            partitions.append(partition)

        # Get the maximum cut for each partition
        maximum_cut = 0
        A = B = None
        for partition in partitions:
            cut = count_cut(graph, partition)
            if cut > maximum_cut:
                maximum_cut = cut
                A = partition[0]
                B = partition[1]

        return A, B, maximum_cut


def count_cut(graph, partition):

        # Count number of crossed edges (between A and B)
        maximum_cut = 0
        for a in partition[0]:
            for b in partition[1]:
                if (a, b) in graph.edges or (b, a) in graph.edges:
                    maximum_cut += 1

        return maximum_cut


if __name__ == '__main__':

    graphs = load_graphs()
    for graph in graphs:

        # Get the largest connected component
        vertices = list(largest_connected_component(graph))

        A, B, maximum_cut = exhaustive_search(graph, vertices)

        print("---")
        print(graph)
        print("A: ", A)
        print("B: ", B)
        print("Maximum Cut:", maximum_cut)


"""
if __name__ == '__main__':

    graphs = load_graphs()
    for graph in graphs:
    
        # Get the largest connected component
        vertices = list(largest_connected_component(graph))

        edges = []
        for edge in graph.edges:
            if edge[0] not in vertices or edge[1] not in vertices:
                edges.append(edge)
            
        all_A = []
        all_B = []
        for length in range(len(vertices)//2+1):
            all_A += combinations(vertices, length)
            if length != len(vertices)-length:
                all_B += combinations(vertices, len(vertices) - length)
            else:
                all_B += list(combinations(vertices, len(vertices)-length))[::-1]
"""