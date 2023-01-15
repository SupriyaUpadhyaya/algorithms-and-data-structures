from typing import List

from graph import DiGraph, Vertex


def depth_first_search(g: DiGraph, node: Vertex) -> List[Vertex]:
    g.reset()
    path = []
    path.append(node)
    node.visited = True
    i = len(path) - 1
    while i >= -1:
        if find(g, path[i]).id == path[i].id:
            i -= 1
        else:
            node = find(g, path[i])
            path.append(node)
            node.visited = True
            i = len(path) - 1
    return path


def find(g: DiGraph, node: Vertex) -> Vertex:
    if len(g.get_neighbors(node)) == 0:
        return node
    else:
        for i in g.get_neighbors(node):
            if i.visited is False:
                return i
    return node
        

def breath_first_search(g: DiGraph, node: Vertex) -> List[Vertex]:
    g.reset()
    path = [node]
    node.visited = True
    i = 0
    while i < len(path):
        for j in g.get_neighbors(path[i]):
            if j.visited is False:
                path.append(j)
                j.visited = True
        i += 1
    return path


if __name__ == "__main__":
    v_1 = Vertex(1)
    v_2 = Vertex(2)
    v_3 = Vertex(3)
    v_4 = Vertex(4)
    v_5 = Vertex(5)
    v_6 = Vertex(6)
    v_7 = Vertex(7)
    v_8 = Vertex(8)

    nodes = [v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8]
    edges = [
        (v_1, v_3), (v_1, v_6), (v_1, v_8),
        (v_2, v_8),
        (v_3, v_1), (v_3, v_7),
        (v_4, v_5), (v_4, v_5),
        (v_5, v_4), (v_5, v_6), (v_5, v_7), (v_5, v_8),
        (v_6, v_1), (v_6, v_4), (v_6, v_5),
        (v_7, v_3), (v_7, v_5),
        (v_8, v_1), (v_8, v_2), (v_8, v_5)
    ]

    g = DiGraph(nodes=nodes, edges=edges)
    print(depth_first_search(g, v_1))
    assert depth_first_search(g, v_1) == [v_1, v_3, v_7, v_5, v_4, v_6, v_8, v_2]

    print(breath_first_search(g, v_1))
    assert breath_first_search(g, v_1) == [v_1, v_3, v_6, v_8, v_7, v_4, v_5, v_2]

    v_0 = Vertex(0)
    v_1 = Vertex(1)
    v_2 = Vertex(2)
    v_3 = Vertex(3)
    v_4 = Vertex(4)
    v_5 = Vertex(5)
    v_6 = Vertex(6)

    nodes1 = [v_0, v_1, v_2, v_3, v_4, v_5]
    edges1 = [
        (v_0, v_1), (v_0, v_2), (v_0, v_4),
        (v_1, v_2), (v_1, v_3), (v_1, v_5),
        (v_2, v_0), (v_2, v_5),
        (v_3, v_1), (v_3, v_4), (v_3, v_5),
        (v_4, v_0), (v_4, v_1),
        (v_5, v_1), (v_5, v_3), (v_5, v_4)
    ]

    g1 = DiGraph(nodes=nodes1, edges=edges1)
    print(depth_first_search(g1, v_1))

    nodes2 = [v_0, v_1, v_2, v_3, v_4, v_5, v_6]
    edges2 = [
        (v_0, v_1), (v_0, v_4),
        (v_2, v_2), (v_2, v_4), (v_2, v_6),
        (v_3, v_0), (v_3, v_2),
        (v_4, v_2), (v_4, v_3), (v_4, v_4), (v_4, v_6),
        (v_5, v_2),
        (v_6, v_3), (v_6, v_5)
    ]

    g2 = DiGraph(nodes=nodes2, edges=edges2)
    print(depth_first_search(g2, v_0))