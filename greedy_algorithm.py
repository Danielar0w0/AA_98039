from graph_utils import *


operations_counter = 0

def greedy_search(graph, vertices):

    global operations_counter

    A = vertices
    B = []

    current_cut = count_cut(graph, [A, B])  # Current cut: 0
    improvement = True  # First time

    while improvement:

        improvement = False

        for vertex in vertices:

            if vertex in A:
                # temp_A = A.copy()
                # temp_A.remove(vertex)
                temp_A = [v for v in A if v != vertex]

                # A can't be empty
                if not temp_A:
                    continue

                # If moving vertex from A to B improves the cut
                if count_cut(graph, [temp_A, B]) < count_cut(graph, [A, B+[vertex]]) \
                        and count_cut(graph, [A, B+[vertex]]) > current_cut:
                    A.remove(vertex)
                    B.append(vertex)

                    # Update current cut and set improvement to True
                    current_cut = count_cut(graph, [A, B])
                    improvement = True

            elif vertex in B:
                # temp_B = B.copy()
                # temp_B.remove(vertex)
                temp_B = [v for v in B if v != vertex]

                # B can't be empty
                if not temp_B:
                    continue

                # If moving vertex from B to A improves the cut
                if count_cut(graph, [A, temp_B]) < count_cut(graph, [A+[vertex], B]) \
                        and count_cut(graph, [A+[vertex], B]) > current_cut:
                    B.remove(vertex)
                    A.append(vertex)

                    # Update current cut and set improvement to True
                    current_cut = count_cut(graph, [A, B])
                    improvement = True

            # Update operations counter
            operations_counter += 1

    return A, B, count_cut(graph, [A, B])


def count_cut(graph, partition):

    global operations_counter

    # Count number of crossed edges (between A and B)
    maximum_cut = 0
    for a in partition[0]:
        for b in partition[1]:
            if (a, b) in graph.edges or (b, a) in graph.edges:
                maximum_cut += 1

            # Update operations counter
            operations_counter += 1

    return maximum_cut


if __name__ == '__main__':

    graphs = load_graphs()
    for graph in graphs:

        operations_counter = 0

        # Get the largest connected component
        vertices = list(largest_connected_component(graph))

        A, B, maximum_cut = greedy_search(graph, vertices)

        print("---")
        print(graph)
        print("A: ", A)
        print("B: ", B)
        print("Maximum Cut:", maximum_cut)

        print("Number of Operations:", operations_counter)
