from graph.graph import Graph, Vertex, Edge

graph1 = Graph()

graph2 = Graph()
a = graph2.add_node('A')
b = graph2.add_node('B')
e = graph2.add_node('E')
c = graph2.add_node('C')
d = graph2.add_node('D')
graph2.add_edge(a, b)
graph2.add_edge(b, a)
graph2.add_edge(a, e)
graph2.add_edge(e, a)
graph2.add_edge(a, c)
graph2.add_edge(b, d)
graph2.add_edge(b, e)
graph2.add_edge(e, d)
graph2.add_edge(e, c)

graph3 = Graph()

def test_add_node_to_a_graph():
    graph1.add_node(1)
    actual = graph1.size()
    expected = 1
    assert actual == expected

def test_add_edge_to_a_graph():
    a = graph1.add_node('a')
    b = graph1.add_node('b')
    graph1.add_edge(a, b)
    actual = graph1.get_neighbors(a)[0].vertex
    expected = b
    assert actual == expected

def test_size_of_a_graph():
    actual = graph2.size()
    expected = 5
    assert actual == expected

def test_get_all_nodes_in_graph():
    output = []
    for i in graph2.get_nodes():
        output.append(i.value)
    actual = output
    expected = ['A', 'B', 'E', 'C', 'D']
    assert actual == expected

def test_get_all_neighbors_of_vertex_in_graph():
    array = []
    for i in graph2.get_nodes():
        array.append(i)
    array2 = []
    for i in graph2.get_neighbors(array[0]):
        array2.append(i.vertex.value)
    output = []
    for i in array2:
        if i not in output:
            output.append(i)
    actual = output
    expected = ['B', 'E', 'C']
    assert actual == expected

def test_all_neighbors_in_graph_with_their_weights():
    array1 = []
    for i in graph2.get_nodes():
        array1.append(i)
    array2 = []
    for i in graph2.get_neighbors(array1[0]):
        array2.append([i.vertex.value, i.weight])
    output = []
    for i in array2:
        if i not in output:
            output.append(i)
    actual = output
    expected = [['B', 0], ['E', 0], ['C', 0]]
    assert actual == expected

def test_an_empty_graph_size():
    actual = graph3.size()
    expected = 0
    assert actual == expected

def test_graph_with_only_one_node_and_edge():
    a = graph3.add_node("A")
    graph3.add_edge(a, a, 1)
    neighbors = graph3.get_neighbors(a)[0]
    assert graph3.size() == 1
    assert graph3.get_neighbors(a)[0].vertex.value == "A"
    assert neighbors.weight == 1