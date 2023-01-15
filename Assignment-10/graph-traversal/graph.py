from dataclasses import dataclass
from typing import List, Tuple


@dataclass(unsafe_hash=True, eq=False)
class Vertex:
    def __init__(self, id: int) -> None:
        self.id = id
        self.visited = False
    
    def __repr__(self) -> str:
        return str(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id


class DiGraph:
    def __init__(self, nodes: List[Vertex], edges: List[Tuple[Vertex, Vertex]]) -> None:
        self.nodes = nodes
        self.edges = edges

    def __str__(self) -> str:
        return str(self.nodes) + "\n" + str(self.edges)

    def get_neighbors(self, v: Vertex) -> List[Vertex]:
        """
        Returns all nodes that are directly connected from `i`.
        
        Throws an `AssertionError` if the nodes does not exist.
        """
        assert v in self.nodes
        return sorted([edge[1] for edge in self.edges if v == edge[0]])

    def reset(self) -> None:
        """Sets all the visited attributes to `False`."""
        for n in self.nodes:
            n.visited = False
