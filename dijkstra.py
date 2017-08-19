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
