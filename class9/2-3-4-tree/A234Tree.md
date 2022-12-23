1.1
====================================================================
A 2/3/4-Tree is an ordered Tree T with the following properties:
• each internal node has at least two children
• These nodes are called �-nodes, where � is the number of children
• each node contains � − 1 data items of the form (key, value)
• the keys form a search tree

2 - node
    a
   / \
 <a   >a

3 - node
      a | b
    /   |   \
  <a  >a <b  >b

4 - node
         a  |  b  |  c
      /     |     |     \
    <a   >a <b  >b <c   >c


2.1
====================================================================
3, 7, 5, 15, 17, 9, 13, 21, 11, 19

     5
   /   \
  3     7 | 15 | 17

           5  |  15
         /    |    \
       3    7|9|13  17|21


       5   |   9   |   15
    /      |       |       \
   3       7     11|13      17|19|21


2.2
====================================================================
3, 5, 7, 9, 11, 13, 15, 17, 19, 21

    5
  /   \
 3     7|9|11

        5   |   9
      /     |     \
    3       7      11|13|15

            5   |   9   |   13
        /       |       |        \
      3         7       11        15|17|19


                    9
                /       \
            5                13 |  17
        /      \          /     |      \
       3         7       11    15      19 | 21

2.3
====================================================================
The 2-3-4 tree depends on the order of items inserted. For case 1 and 2 the tree is different for same set of items inserted in different order. The height of the both the trees is also different

3
====================================================================
In top down approch tree will never "step into" a full-node while descending tree to insert a new item. Nodes are proactivively split while going down the tree instead of waiting for the "full-node" status. There is no need to propagate values back up the tree. Insertions is done in single pass.

For 2.1 and 2.2 bottom-up approch is used.