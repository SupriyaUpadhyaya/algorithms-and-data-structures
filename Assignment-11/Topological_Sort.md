Topological sorting can be applied on only directed asyclic graphs. The algorithm starts with any vertex that is a sink.

There is no sink in given graph

Given graph has below paths that form cycle/loops 
1. cuts - covers - crushes - poisons - smashes
2. disaproves - smashes - cuts
3. vaporizes - crushes - poisons
4. crushes - cuts - covers
5. decapitates - poisons - smashes
6. eats - covers - crushes

Removing atleast two outgoing edges of any node say X and removing one of the outgoing node of X will break all loops and leave a sink which can be used as starting vertex. 

Example - Consider Paper Vertex:
1. Remove two outgoing edges - Disaproves and Covers
2. Two incoming edges are from Lizard and Scissors 
    - Consider Scissors and remove outgoing edge that does not connect to paper - decapitates
    - Consider Lizard and remove outgoing edge that does not connect to paper - poisons

All the cycles mentioned above are brokens:
1. cut - {removed} - crushes - {removed} - smashes
2. {removed} - smashes - cuts
3. vaporizes - crushes - {removed}
4. crushes - cuts - {removed}
5. {removed} - {removed} - smashes
6. eats - {removed} - crushes

one sinks are created:
1. Paper