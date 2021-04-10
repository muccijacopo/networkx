import networkx as nx

from heapq import heappush, heappop
from itertools import count


def greedy_path(G, source, target, heuristic=None, weight="weight"):
    """Returns a list of nodes in a shortest path between source and target
        using the Greedy Path algorithm.
    """

    push = heappush
    pop = heappop

    if heuristic is None:
        def heuristic(_, __):
            return 0

    if source not in G or target not in G:
        msg = f"Either source {source} or target {target} is not in G"
        raise nx.NodeNotFound(msg)

    c = count()
    # The queue stores priority, node and parent
    queue = [(heuristic(source, target), next(c), source, None)]
    explored = {}

    while queue:
        h, _, curnode, parent = pop(queue)
        explored[curnode] = parent

        if curnode == target:
            path = [curnode]
            parent = explored[curnode]
            while parent is not None:
                path.append(parent)
                parent = explored[parent]
            path.reverse()
            return path

        for neighbor, props in G[curnode].items():
            push(queue, (heuristic(neighbor, target), next(c), neighbor, curnode))

    raise nx.NetworkXNoPath(f"Node {target} not reachable from {source}")







