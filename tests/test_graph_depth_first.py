from graph_depth_first.graph_depth_first import Graph

graph = Graph()
a = graph.add_node('A')
b = graph.add_node('B')
c = graph.add_node('C')
d = graph.add_node('D')
e = graph.add_node('E')
f = graph.add_node('F')
g = graph.add_node('G')
h = graph.add_node('H')

graph.add_edge(a, d)
graph.add_edge(a, b)
graph.add_edge(b, a)
graph.add_edge(b, d)
graph.add_edge(b, c)
graph.add_edge(c, b)
graph.add_edge(c, g)
graph.add_edge(g, c)
graph.add_edge(d, a)
graph.add_edge(d, b)
graph.add_edge(d, f)
graph.add_edge(d, h)
graph.add_edge(d, e)
graph.add_edge(e, d)
graph.add_edge(h, d)
graph.add_edge(h, f)
graph.add_edge(f, d)
graph.add_edge(f, h)

def test_depth_first_on_a_graph():
    actual = graph.depth_first(a)
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert actual == expected

graph1 = Graph()

def test_depth_first_on_a_graph2():
    actual = graph1.depth_first()
    expected = []
    assert actual == expected

