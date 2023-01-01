What is a tree? Use the words: node, parent, child
A tree is an abstract data type that stores elements hierarchically. Tree consists of a set of nodes and a set of edges. Each element in the tree hierarchy is called a node and may consist of one or more fields. If a node N is directly connected to other nodes directly below it in the tree, then is called as parent node and nodes directly below are called as child nodes

What is a leaf node?
A node in the tree hierarchy without any child nodes is called as a leaf node

What is a root node?
A single node a the top of tree hierarchy without any parent node is called as root node

What is the height of a tree?
A path is a sequence of nodes connecting each node to the root of the tree. Depth of a node is equal to the number of edges on the path from node to the root node. Nodes with same depth form a level of a tree. Height of tree is equal to number of levels

What is a path in a tree?
A path in a tree is a sequence of nodes connecting each node to the root of the tree

What are common applications of trees?
Binary search tree
Machine learning algorithm
To evaluate an expression
XML parser

What is a binary tree?
A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right children. 

What is a search tree?
A tree can be considered as a binary search tree if - for any node k in the tree:
- all nodes in k's left subtree are less than k
- all nodes in k's left subtree are less than k

What is a balanced search tree?
A balanced binary tree is also known as height balanced tree. It is defined as binary tree where the difference between the height of the left subtree and right subtree is not more than m, where m is usually equal to 1.

Given the following tree:
Pre-order : 10, 5, 2, 9, 6, 15, 13, 12, 14
In-order :  2, 5, 6, 9, 10, 12, 13, 14, 15
Post-order: 2, 6, 9, 5, 12, 14, 13, 15, 10