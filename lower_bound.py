import math


def lower_bound(v, e, connected=False):

    # Formulas: https://en.wikipedia.org/wiki/Maximum_cut
    # A graph must have at least v+1 edges to be connected
    if connected:
        return (e / 2) + (v - 1)/4

    return (e / 2) + (math.sqrt(2*e + 1/2) - 1/4) / 4


if __name__ == '__main__':

    vertices = [(5, 3), (12, 15), (11, 19), (3, 17), (7, 12), (16, 12), (11, 15), (12, 16), (20, 6), (10, 14)]
    edges = [((16, 12), (5, 3)), ((7, 12), (10, 14)), ((20, 6), (10, 14)), ((20, 6), (12, 16)), ((11, 19), (16, 12))]

    print("Lower bound:", lower_bound(len(vertices), len(edges)))

    # Connected subset
    print("Lower bound (connected):", lower_bound(4, 3, connected=True))
