# Randomized Algorithm
## Advanced Algorithms First Project

### Introduction
Design and test a **randomized algorithm** to solve the combinatorial problem that was assigned in the first project.

---

**22** – Find a maximum cut for a given undirected graph G(V, E), with n vertices and m edges. A
maximum cut of G is a partition of the graph's vertices into two complementary sets S and T, such
that the number of edges between the set S and the set T is as large as possible.

---

Devise and/or adapt strategies for:

- Iterating through the randomly generated candidate solutions and keeping the best
feasible solution computed.
- Ensuring that no such solutions are tested more than once.
- Deciding when to stop testing candidate solutions of a certain size and start testing
larger or smaller solutions.
- Deciding when to stop testing altogether: e.g., after a given number of candidate
solutions, or after spending a certain amount of computation time, etc.

### Graphs for the Computational Experiments

In addition to the graph instances already used in the first project, you should **run all your
algorithms on example and benchmark graph instances available on the Web**.

**Pointers for such graph instances will be given on the course page on E-Learning.**

---

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

### Performance Analysis

Afterwards, analyze the performance of the developed strategy. To accomplish that:

a) Perform a formal computational complexity analysis of the randomized algorithm.

b) Devise and carry out a sequence of experiments, **for successively larger problem
instances**, to register and analyze (1) **the number of basic operations** carried out, (2) **the
execution time** and (3) **the number of solutions / configurations** tested.

c) Analyze the accuracy of the obtained solutions by comparing them with the solutions
obtained with the algorithms of the first project.

d) Compare the results of the **experimental** and the **formal analysis**.

e) Determine **the largest graph** that you can process on your computer, without taking too
much time.

f) Estimate the execution time that would be required by much **larger problem instances**.

g) Write a report (8 pages, max.).


