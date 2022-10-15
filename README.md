# Exhaustive Search
## Advanced Algorithms First Project

### Introduction
Design and test an **exhaustive search algorithm** to solve the following **graph problem**, as
well as another method using a greedy heuristics.

---

**22** – Find a maximum cut for a given undirected graph G(V, E), with n vertices and m edges. A
maximum cut of G is a partition of the graph's vertices into two complementary sets S and T, such
that the number of edges between the set S and the set T is as large as possible.

---

Afterwards, analyze the computational complexity of the developed algorithms. To accomplish that:

a) Perform a formal computational complexity analysis of the algorithms.

b) Carry out a sequence of experiments, for successively larger problem instances, to register
and analyze (1) the **number of basic operations** carried out, (2) **the execution time** and (3)
the **number of solutions / configurations** tested.

c) Compare the results of the experimental and the formal analysis.

d) Determine the largest graph that you can process on your computer, without taking too much
time.

e) Estimate the execution time that would be required by much larger problem instances.

f) Write a report (8 pages, max.).

### Graphs for the Computational Experiments

The **graph instances** used in the **computational experiments** should represent the following
scenario:

- Graph **vertices** are 2D points on the XOY plane, with integer valued coordinates between
1 and 20.
- Graph **vertices should neither be coincident nor too close**.
- The **number of edges** sharing a vertex is randomly determined.

Generate successively larger **random graphs**, with 4, 5, 6, … vertices, using your **student number
as seed**. **Use 12.5%, 25%, 50% and 75% of the maximum number of edges** for the number of vertices.

**Suggestion**: Store each graph in a file to be used for the computational experiments.
Depending on the problem, it might be helpful to represent each graph by its **adjacency matrix** or
by its **incidence matrix**.

It might also be useful to graphically **visualize** the graph instances and the computed solutions.
