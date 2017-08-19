class Connection:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

def get_shortest_path(nodes, start_node, end_node):
    for node in nodes:
        node.cost = 10e99
    start_node.cost = 0

    nodes = sort_nodes_by_cost(nodes)

    while nodes[0] != end_node:
        for connection in nodes[0].connections:
            new_cost = nodes[0].cost + connection.cost
            if connection.node.cost > new_cost:
                connection.node.cost = new_cost
                connection.node.previous_node = nodes[0]

        nodes = remove_node_with_index(nodes, 0)
        nodes = sort_nodes_by_cost(nodes)

    path = []
    current_node = end_node
    while True:
        path.append(current_node)
        current_node = current_node.previous_node
        if current_node == start_node:
            path.append(current_node)
            break
    # Reverse array
    path = path[::-1]

    return path

def sort_nodes_by_cost(nodes):
    sorted_nodes = []
    while nodes != []:
        lowest_cost_node_index = get_lowest_node_cost_index(nodes)
        sorted_nodes.append(nodes[lowest_cost_node_index])
        nodes = remove_node_with_index(nodes, lowest_cost_node_index)
    return sorted_nodes

def get_lowest_node_cost_index(nodes):
    curLowest = 10e99
    index = 0
    for i in range(len(nodes)):
        if nodes[i].cost < curLowest:
            curLowest = nodes[i].cost
            index = i
    return index

def remove_node_with_index(nodes, index):
    result = []
    for i in range(len(nodes)):
        if index != i:
            result.append(nodes[i])
    return result

def Main():
    # a = Node('A')
    # b = Node('B')
    # c = Node('C')
    # d = Node('D')
    # e = Node('E')
    # f = Node('F')
    # g = Node('G')
    
    # nodes = [a, b, c, d, e, f, g]


    # a.add_connection(Connection(b, 1))
    # b.add_connection(Connection(a, 1))
    # b.add_connection(Connection(c, 2))
    # b.add_connection(Connection(d, 3))
    # c.add_connection(Connection(b, 2))
    # c.add_connection(Connection(f, 7))
    # d.add_connection(Connection(b, 3))
    # d.add_connection(Connection(e, 1))
    # e.add_connection(Connection(d, 1))
    # e.add_connection(Connection(f, 3))
    # f.add_connection(Connection(c, 7))
    # f.add_connection(Connection(e, 3))
    # f.add_connection(Connection(g, 1))   
    # g.add_connection(Connection(f, 1))


    # get_shortest_path(nodes, a, g)

    # a = Node('A')
    # b = Node('B')
    # c = Node('C')
    # d = Node('D')
    # e = Node('E')
    # f = Node('F')
    # g = Node('G')

    # nodes = [a, b, c, d, e, f, g]

    # a.add_connection(Connection(b, 1))
    # a.add_connection(Connection(f, 1))

    # b.add_connection(Connection(a, 1))
    # b.add_connection(Connection(c, 3))
    # b.add_connection(Connection(d, 5))

    # c.add_connection(Connection(b, 3))
    # c.add_connection(Connection(d, 3))

    # d.add_connection(Connection(b, 5))
    # d.add_connection(Connection(c, 3))
    # d.add_connection(Connection(e, 1))

    # e.add_connection(Connection(d, 1))
    # e.add_connection(Connection(g, 1))

    # f.add_connection(Connection(a, 1))
    # f.add_connection(Connection(g, 20))

    # g.add_connection(Connection(f, 20))
    # g.add_connection(Connection(e, 1))

    # get_shortest_path(nodes, a, g)

    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')

    nodes = [a, b, c, d, e, f, g]

    a.add_connection(Connection(b, 4))
    a.add_connection(Connection(c, 1))
    b.add_connection(Connection(a, 4))
    b.add_connection(Connection(d, 2))
    b.add_connection(Connection(g, 13))
    c.add_connection(Connection(a, 1))
    c.add_connection(Connection(d, 4))
    c.add_connection(Connection(e, 2))
    d.add_connection(Connection(b, 2))
    d.add_connection(Connection(c, 4))
    d.add_connection(Connection(e, 1))
    d.add_connection(Connection(f, 3))    
    e.add_connection(Connection(d, 1))
    e.add_connection(Connection(c, 2))
    e.add_connection(Connection(f, 7))   
    f.add_connection(Connection(d, 3))
    f.add_connection(Connection(e, 7))
    f.add_connection(Connection(g, 2))
    g.add_connection(Connection(b, 13))
    g.add_connection(Connection(f, 2))

    get_shortest_path(nodes, a, g)

if __name__ == '__main__':
    Main()
