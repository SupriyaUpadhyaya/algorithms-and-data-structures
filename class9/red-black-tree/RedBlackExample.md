A red-black tree is a binary search tree with nodes colored in either red or black that satisfies the following properties:
1. The root node is black
2. Every external node is black
    • None references count as external nodes!
3. Children of a red node are black
4. For every external node the black depth is equal
    • black depth: number of proper ancestors that are black

Properties
A red-black tree can be transformed into a 2-3-4 tree by mergingevery red node into its parent
• the entry from the red node w is stored at its parent
• the children of the red node w become ordered children of the parent

        6b
    /       \
3r              7r
    \
        4r
Red black violation in above step

        6b
    /       \
3b              7b
    \
        4r

                  6b
                /   \
            3b          7b
        /       \
    2r              4r
/
1r


                                    3b
                                /       \
                            2b              6b
                        /               /       \              
                    1r                 4r         7r



AVL:

                    3
                /       \
            2               6
        /               /       \
        1               4       7


2-3-4 tree
            3
        /       \
    1  |  2    4|6|7


                        

                