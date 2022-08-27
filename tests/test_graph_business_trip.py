from graph_business_trip.graph_business_trip import Graph, business_trip

graph = Graph()

Pandora = graph.add_node('Pandora')
Arendelle = graph.add_node('Arendelle')
Metroville = graph.add_node('Metroville')
Monstropolis = graph.add_node('Monstropolis')
Narnia = graph.add_node('Narnia')
Naboo = graph.add_node('Naboo')

graph.add_edge(Pandora, Arendelle, 150)
graph.add_edge(Arendelle, Pandora, 150)
graph.add_edge(Pandora, Metroville, 82)
graph.add_edge(Metroville, Pandora, 82)
graph.add_edge(Arendelle, Metroville, 99)
graph.add_edge(Metroville, Arendelle, 99)
graph.add_edge(Arendelle, Monstropolis, 42)
graph.add_edge(Monstropolis, Arendelle, 42)
graph.add_edge(Metroville, Monstropolis, 105)
graph.add_edge(Monstropolis, Metroville, 105)
graph.add_edge(Metroville, Narnia, 37)
graph.add_edge(Narnia, Metroville, 37)
graph.add_edge(Metroville, Naboo, 26)
graph.add_edge(Naboo, Metroville, 26)
graph.add_edge(Monstropolis, Naboo, 73)
graph.add_edge(Naboo, Monstropolis, 73)
graph.add_edge(Naboo, Narnia, 250)
graph.add_edge(Narnia, Naboo, 250)

def test_business_trip_one_edge():
    arr1 = [Pandora, Arendelle]
    actual = business_trip(graph, arr1)
    expected = '$150'
    assert actual == expected

def test_business_trip_two_edge():
    arr1 = [Pandora, Arendelle, Metroville]
    actual = business_trip(graph, arr1)
    expected = '$249'
    assert actual == expected

def test_business_trip_no_edge():
    arr1 = [Pandora, Narnia]
    actual = business_trip(graph, arr1)
    expected = 'Null'
    assert actual == expected

def test_business_trip_three_edges():
    arr1 = [Pandora, Arendelle, Monstropolis, Naboo]
    actual = business_trip(graph, arr1)
    expected = '$265'
    assert actual == expected