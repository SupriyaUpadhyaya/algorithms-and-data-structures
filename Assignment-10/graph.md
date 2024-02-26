What is a graph?
A graph is an abstract data type that stores elements and
their relations with each other
A graph consists of
• a set of nodes (also called vertices)
• a set of edges

Formally a graph is a tuple G = (V, E)
Vertex set v
Edge set E

Relationship between nodes:
• two vertices u and v are adjacent, if they are connected
by a single edge, ie. {u, v} ∈ E
• the set of all vertices that are adjacent to a vertex v are
called v's neighbors

What is a directed and undirected graph? What is this graph?
A directed graph is an abstract data type that stores elements
and their relations with each other
A directed graph consists of
• a set of nodes
• a set of directed edges
• Edges in a directed graph are represented as ordered pairs (or
tuples)
• Undirected graphs are special cases of directed graph
A graph is undirected if holds: �, � ∈ � ↔ �, � ∈ �


How many vertices does this graph have?
9


How many edges does this graph have?
16
Edge set E ={
                {0, 5},{0, 6}, {0, 7}, {0, 8}, {1, 2}, {1, 5}, {2, 3}, {3, 4}, {4, 1}, {5, 4},
                   {6, 5},{6, 6}, {6, 7},{8, 5}, {8, 7},{8, 8}
                }

List all sources! A source is a vertex that has only outgoing edges.
0

List all sinks! A sink is a vertex that has only ingoing edges.
7

A cycle in a directed graph is a path through this graph, where the start node and the end node are the same. The count of visited nodes is the length of this cycle. How many cycles of length  and  are in this graph? Provide them.
length  3
number of cycles = 1
{1, 5, 4}

length  4
number of cycles = 1
{1, 2, 3, 4}

What is the corresponding edge list for this graph?
{ 9, 16, 0, 5, 0, 6, 0, 7, 0, 8, 1, 2, 1, 5, 2, 3, 3, 4, 4, 1, 5, 4,  6, 5, 6, 6 , 6, 7 , 8, 5 ,  8, 7 , 8, 8}

What is the corresponding node list for this graph?
V ={0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
|v|=9

What is the corresponding adjacency matrix for this graph?
    0   1   2   3   4   5   6   7   8   0

    0   0   0   0   0   0   1   1   1   1

    1   0   0   1   0   0   1   0   0   0

    2   0   0   0   1   0   0   0   0   0

    3   0   0   0   0   1   0   0   0   0

    4   0   1   0   0   0   0   0   0   0

    5   0   0   0   0   1   0   0   0   0

    6   0   0   0   0   0   1   1   1   0

    7   0   0   0   0   0   0   0   0   0

    8   0   0   0   0   0   1   0   1   1