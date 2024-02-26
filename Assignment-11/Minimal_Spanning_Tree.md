Kruskal's Algorithm

(h, g) - 1
(g, f) - 2
(i, c) - 2
(c, f) - 4
(a, b) - 4
(c, d) - 7
(h, i) - removed
(b, c) - 8
(a, h) - removed
(d, e) - 9
(c, f) - removed
(b, h) - removed
(d, f) - removed

Sum of weights - 47



                                    b -----(8)----- c -----(7)----- d
                                 /               /    \                \
                               (4)             (2)      \               (9)
                              /               /           \                \  
                            a                i             (4)                e       
                                                               \
                                                                 \
                                                                   \
                                    h -----(1)----- g -----(2)----- f