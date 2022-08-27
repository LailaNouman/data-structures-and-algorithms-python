class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex

class Graph:

    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        edge2 = Edge(start_vertex)
        self.__adj_list[start_vertex].append(edge1)
        self.__adj_list[end_vertex].append(edge2)

    def get_nodes(self):
        return self.__adj_list.keys()

    def size(self):
        return len(self.__adj_list)

    def get_neighbors(self, ver):
        return self.__adj_list.get(ver, [])

def business_trip(graph, arr_cities):
    cost = 0
    if len(arr_cities) == 0:
        return None
    for city in range(len(arr_cities) - 1):
        for neighbor in graph.get_neighbors(arr_cities[city]):
            if neighbor.vertex == arr_cities[city + 1]:
                cost += neighbor.weight
    if cost == 0:
        return 'Null'
    else:
        return f"${cost}"

if __name__ == "__main__":
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

    arr_cities = [Pandora, Arendelle, Monstropolis, Naboo]
    print(business_trip(graph, arr_cities))

