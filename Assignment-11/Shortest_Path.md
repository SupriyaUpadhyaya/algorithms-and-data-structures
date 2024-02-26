Shortest Path: Dijkstra Algorithm

Start from 'a'
Queue : a -> b -> h -> c -> i -> g -> f -> d -> e

predecessors
a   b   c   d   e   f   g   h   i
-   a   b   c   f   c   h   a   h
                    g           c

distance to starting node 'a'
a   b   c   d   e   f   g   h   i
0   4   12  19  21  16  9   8   15
                    11          14

                                    4               12              19
                                    b -----(8)----- c -----(7)----- d
                                 /                             
                               (4)                           
                              /            15 - 14                              
                          0  a             i                               e  21      
                              \         /                               /
                                (8)   (7)                             (10)  
                                  \  /                               /
                                    h -----(1)----- g -----(2)----- f
                                    8               9               16 - 11

Sum of path from a to e
e <-- f <-- g <-- h <-- a = 21