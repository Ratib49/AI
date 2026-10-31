# Breadth First Search (BFS) on a tree and on a graph
from collections import deque


def bfs(graph, start):
    visited = [start]
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return order


def bfs_levels(tree, root):
    """Returns nodes level by level, e.g. [['A'], ['B','C'], ...]"""
    levels, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node)
            queue.extend(tree.get(node, []))
        levels.append(level)
    return levels


if __name__ == "__main__":
    # Input tree:
    #            A
    #          /   \
    #         B     C
    #        / \   / \
    #       D   E F   G
    #      /
    #     H
    tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H"],
        "E": [], "F": [], "G": [], "H": [],
    }
    print("Tree BFS from A:", " -> ".join(bfs(tree, "A")))
    for i, lvl in enumerate(bfs_levels(tree, "A")):
        print(f"  Level {i}: {lvl}")

    # Input graph (undirected, has a cycle)
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1, 5],
        4: [1, 2, 5],
        5: [3, 4],
    }
    print("Graph BFS from 0:", " -> ".join(map(str, bfs(graph, 0))))
