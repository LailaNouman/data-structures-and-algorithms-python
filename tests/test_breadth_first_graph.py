from graph_breadth_first.graph_breadth_first import Graph

graph = Graph()
Pandora = graph.add_node('Pandora')
Arendelle = graph.add_node('Arendelle')
Metroville = graph.add_node('Metroville')
Monstroplolis = graph.add_node('Monstroplolis')
Narnia = graph.add_node('Narnia')
Naboo = graph.add_node('Naboo')

def test_breadth_first_graph_without_edges():
    actual = graph.breadth_first(Pandora)
    expected = ['Pandora']
    assert actual == expected

graph2 = Graph()
Pandora1 = graph2.add_node('Pandora')
Arendelle1 = graph2.add_node('Arendelle')
Metroville1 = graph2.add_node('Metroville')
Monstroplolis1 = graph2.add_node('Monstroplolis')
Narnia1 = graph2.add_node('Narnia')
Naboo1 = graph2.add_node('Naboo')
graph2.add_edge(Pandora1, Arendelle1)
graph2.add_edge(Arendelle1, Metroville1)
graph2.add_edge(Arendelle1, Monstroplolis1)
graph2.add_edge(Metroville1, Arendelle1)
graph2.add_edge(Metroville1, Monstroplolis1)
graph2.add_edge(Metroville1, Narnia1)
graph2.add_edge(Metroville1, Naboo1)
graph2.add_edge(Monstroplolis1, Arendelle1)
graph2.add_edge(Monstroplolis1, Metroville1)
graph2.add_edge(Monstroplolis1, Naboo1)
graph2.add_edge(Naboo1, Narnia1)
graph2.add_edge(Naboo1, Metroville1)
graph2.add_edge(Naboo1, Monstroplolis1)
graph2.add_edge(Narnia1, Naboo1)
graph2.add_edge(Narnia1, Metroville1)

def test_breadth_first_graph_with_edges():
    actual = graph2.breadth_first(Pandora1)
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    assert actual == expected

