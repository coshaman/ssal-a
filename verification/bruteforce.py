from itertools import combinations


def is_chordal(adjacency):
    active = (1 << len(adjacency)) - 1
    while active:
        removed = False
        for v in range(len(adjacency)):
            if not active >> v & 1:
                continue
            neighbors = adjacency[v] & active & ~(1 << v)
            okay = True
            remaining = neighbors
            while remaining:
                u_bit = remaining & -remaining
                u = u_bit.bit_length() - 1
                if adjacency[u] & neighbors != neighbors & ~(1 << u):
                    okay = False
                    break
                remaining ^= u_bit
            if okay:
                active ^= 1 << v
                removed = True
                break
        if not removed:
            return False
    return True


def count_graphs(n):
    edges = list(combinations(range(n), 2))
    count = 0
    for mask in range(1 << len(edges)):
        adjacency = [0] * n
        for i, (u, v) in enumerate(edges):
            if mask >> i & 1:
                adjacency[u] |= 1 << v
                adjacency[v] |= 1 << u
        count += is_chordal(adjacency)
    return count
