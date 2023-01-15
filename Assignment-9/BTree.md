# A B-Tree is a self-balancing tree of order m in which each node has
# 1. at most 2m entries (and thus at most 2m + 1 children)
# 2. at least m entries (and thus, for internals nodes, m + 1 children)
# 3. except the root node
# 

Insert the numbers 3, 7, 5, 15, 17, 9, 13, 21, 11, 19, 23  into a B-Tree where m=2.

1.insert 3
         3

2. insert 7
      3   7

3. insert 5
            5
        /       \
        3        7

4. insert 15
            5
        /       \
        3       7 15

5. insert 17
         5   15
        /  |  \
        3  7   17

6. insert 9

        5     15
        /   |   \
        3  7 9  17

7. insert 13
            9
        /       \
        5       15
      /   \   /    \
      3    7  13    17

8. insert 21
            9
        /       \
       5       15
      /   \   /    \
     3    7  13  17 21

9. insert 11
             9
        /        \
        5         15
      /   \      /    \
      3    7  11  13  17 21

10. insert 19

              9
         /          \
        5         15    19
      /   \      /    |   \
      3    7  11  13  17   21

11. insert 23

             9
        /          \
        5         15    19
      /   \      /    |   \
      3    7  11  13  17  21 23


Do the same but for the different order 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23  where m=2!

1. insert 3
        3

2. insert 5
    3       5

3. insert 7

         5
     /      \
     3        7

4. insert 9
             5
        /       \
        3       7 9
5. insert 11
     5   9
     /  |  \
    3   7   11

6. insert 13
     5       9
    /    |    \
    3    7   11 13

7. insert 15
         9
     /       \
    5         13
    /   \   /    \
    3    7  11    15

8. insert 17

             9
         /       \
       5         13
    /   \   /    \
   3    7  11   15 17

9. insert 19
             9
        /          \
        5         13    17
     /   \      /     |   \
    3    7    11     15   19

10. insert 21
             9
        /          \
      5         13    17
    /   \      /     |   \
    3    7    11     15 19 21

11. insert 23
             9     17
         /      |    \
       5       13      21
    /   \      /  \    /    \
  3      7    11  15  19   23


Advantages of B tree
B trees are used to reduce the number of disc acceses. Optimize for actual execution time by minimizing number of hard disk accesses!
The B tree can store millions of itemsin it, and through its flat structure it provides easy and efficient traversal through the data.

