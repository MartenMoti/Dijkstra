import unittest
import dijkstra

class TestDijkstra(unittest.TestCase):
    def test_get_lowest_node_cost_index(self):
        a = dijkstra.Node('A')
        b = dijkstra.Node('B')
        c = dijkstra.Node('C')
        d = dijkstra.Node('D')
        a.cost = 3
        b.cost = 7
        c.cost = 1
        d.cost = 8
        nodes = [a, b, c, d]
        result = dijkstra.get_lowest_node_cost_index(nodes)
        expected_result = 2
        self.assertEqual(result, expected_result)

    def test_remove_node_with_index(self):
        a = dijkstra.Node('A')
        b = dijkstra.Node('B')
        c = dijkstra.Node('C')
        d = dijkstra.Node('D')
        a.cost = 3
        b.cost = 7
        c.cost = 1
        d.cost = 8
        nodes = [a, b, c, d]
        index_to_remove = 2
        expected_result = [a, b, d]
        result = dijkstra.remove_node_with_index(nodes, index_to_remove)
        self.assertEqual(result, expected_result)

    def test_sort_nodes_by_cost(self):
        a = dijkstra.Node('A')
        b = dijkstra.Node('B')
        c = dijkstra.Node('C')
        d = dijkstra.Node('D')
        a.cost = 3
        b.cost = 7
        c.cost = 1
        d.cost = 8
        nodes = [a, b, c, d]
        expected_result = [c, a, b, d]
        actual_result = dijkstra.sort_nodes_by_cost(nodes)
        self.assertEqual(expected_result, actual_result)

    def test_dijkstra_normal(self):
        a = dijkstra.Node('A')
        b = dijkstra.Node('B')
        c = dijkstra.Node('C')
        d = dijkstra.Node('D')
        e = dijkstra.Node('E')
        f = dijkstra.Node('F')

        nodes = [a, b, c, d, e, f]

        a.add_connection(dijkstra.Connection(b, 2))
        a.add_connection(dijkstra.Connection(e, 1))
        b.add_connection(dijkstra.Connection(a, 2))
        b.add_connection(dijkstra.Connection(d, 1))
        b.add_connection(dijkstra.Connection(c, 20))
        c.add_connection(dijkstra.Connection(b, 20))
        c.add_connection(dijkstra.Connection(d, 8))
        c.add_connection(dijkstra.Connection(f, 3))
        d.add_connection(dijkstra.Connection(b, 1))
        d.add_connection(dijkstra.Connection(c, 8))
        d.add_connection(dijkstra.Connection(f, 7))
        e.add_connection(dijkstra.Connection(a, 1))
        e.add_connection(dijkstra.Connection(f, 20))
        f.add_connection(dijkstra.Connection(e, 20))
        f.add_connection(dijkstra.Connection(c, 3))
        f.add_connection(dijkstra.Connection(d, 7))

        expected_result = [a, b, d, f]
        actual_result = dijkstra.get_shortest_path(nodes, a, f)
        self.assertEqual(expected_result, actual_result)

    def test_dijkstra_circle(self):
        a = dijkstra.Node('A')
        b = dijkstra.Node('B')
        c = dijkstra.Node('C')
        d = dijkstra.Node('D')
        e = dijkstra.Node('E')
        f = dijkstra.Node('F')
        g = dijkstra.Node('G')

        nodes = [a, b, c, d, e, f, g]

        a.add_connection(dijkstra.Connection(c, 1))
        a.add_connection(dijkstra.Connection(b, 200))
        b.add_connection(dijkstra.Connection(a, 200))
        b.add_connection(dijkstra.Connection(g, 1))
        c.add_connection(dijkstra.Connection(a, 1))
        c.add_connection(dijkstra.Connection(f, 1))
        c.add_connection(dijkstra.Connection(d, 1))      
        d.add_connection(dijkstra.Connection(e, 1))
        d.add_connection(dijkstra.Connection(c, 1))
        e.add_connection(dijkstra.Connection(d, 1))
        e.add_connection(dijkstra.Connection(f, 1))
        f.add_connection(dijkstra.Connection(c, 1))
        f.add_connection(dijkstra.Connection(e, 1))
        g.add_connection(dijkstra.Connection(b, 1))

        expected_result = [a, b, g]
        actual_result = dijkstra.get_shortest_path(nodes, a, g)
        self.assertEqual(expected_result, actual_result)