import collections

Nodes = []  # изначальный граф
S1 = []
S2 = []
path = ""

def get_node(value, graph):
    for node in graph:
        if node.value == value:
            return node
    return Node(value, graph)


class Node:
    def __init__(self, value, graph, node_to=None, node_from=None, s1=False, s2=False):
        self.s1 = s1
        self.s2 = s2
        self.value = value
        self.graph = graph
        if node_to is None:
            self.nodes_to = []
        else:
            self.nodes_to = [node_to]
        if node_from is None:
            self.nodes_from = []
        else:
            self.nodes_from = [node_from]
        graph.append(self)
        if s1:
            S1.append(self)
        if s2:
            S2.append(self)

    def add_node_to(self, node):
        if node not in self.nodes_to:
            self.nodes_to.append(node)

    def add_node_from(self, node):
        if node not in self.nodes_from:
            self.nodes_from.append(node)


def turn_edges(graph):
    for node in graph:
        term = node.nodes_to
        node.nodes_to = node.nodes_from
        node.nodes_from = term
    return graph


def create_new_graph_for_A(graph, n):
    new_graph = []
    a = Node(n + 1, new_graph)  # вершина-множество S1

    for v in graph:
        if v.s1:
            for u in v.nodes_to:
                if not u.s1:
                    u_new = get_node(u.value, new_graph)
                    a.add_node_to(u_new)
                    u_new.add_node_from(a)
        else:
            v_new = get_node(v.value, new_graph)
            for u in v.nodes_to:
                if u.s1:
                    v_new.add_node_to(a)
                    a.add_node_from(v_new)
                else:
                    u_new = get_node(u.value, new_graph)
                    v_new.add_node_to(u_new)
                    u_new.add_node_from(v_new)
    return new_graph


def create_new_graph_for_B(graph, n):
    new_graph = []
    b = Node(n + 2, new_graph)  # вершина-множество S2

    for v in graph:
        if v.s2:
            for u in v.nodes_to:
                if not u.s2:
                    u_new = get_node(u.value, new_graph)
                    b.add_node_to(u_new)
                    u_new.add_node_from(b)
        else:
            v_new = get_node(v.value, new_graph)
            for u in v.nodes_to:
                if u.s2:
                    v_new.add_node_to(b)
                    b.add_node_from(v_new)
                else:
                    u_new = get_node(u.value, new_graph)
                    v_new.add_node_to(u_new)
                    u_new.add_node_from(v_new)
    return new_graph


def bfs(root, graph):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    dist = {vertex.value: -1 for vertex in graph}
    dist[root.value] = 0
    while queue:
        vertex = queue.popleft()
        for neighbour in vertex.nodes_to:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                dist[neighbour.value] = dist[vertex.value] + 1
    return dist


if __name__ == '__main__':
    with open(path + "input1.txt", "r") as f:
        n, e = map(int, f.readline().split(' '))
        for i in range(e):
            a, b = map(int, f.readline().split(' '))
            u = get_node(a, Nodes)
            v = get_node(b, Nodes)
            u.add_node_to(v)
            v.add_node_from(u)
        n_s1 = int(f.readline())

        s_1 = map(int, f.readline().split(' '))
        for i in s_1:
            v = get_node(i, Nodes)
            v.s1 = True
            S1.append(v)
        n_s2 = int(f.readline())
        s_2 = map(int, f.readline().split(' '))
        for i in s_2:
            v = get_node(i, Nodes)
            v.s2 = True
            S2.append(v)
    turn_edges(Nodes)

    new_graph_for_S1 = create_new_graph_for_A(Nodes, n)
    new_graph_for_S2 = create_new_graph_for_B(Nodes, n)
    A = get_node(n + 1, new_graph_for_S1)
    B = get_node(n + 2, new_graph_for_S2)
    d1 = bfs(A, new_graph_for_S1)  # расстояние до S1
    d2 = bfs(B, new_graph_for_S2)  # расстояние до S2
    turn_edges(Nodes)
    for node in S1:
        d1.update({node.value: 0})
    for node in S2:
        d2.update({node.value: 0})
    del d1[A.value]
    del d2[B.value]
    finish_dict = {}
    for node in Nodes:
        if d1[node.value] != -1 and d2[node.value] != -1:
            finish_dict[node.value] = d1[node.value] + d2[node.value]
    sorted_nodes = sorted(finish_dict, key=finish_dict.get)
    for node in sorted_nodes:
        print(node)
