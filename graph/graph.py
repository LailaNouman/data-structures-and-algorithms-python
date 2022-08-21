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
        self.__adj_list[start_vertex].append(edge1)
        edge2 = Edge(start_vertex)
        self.__adj_list[end_vertex].append(edge2)

    def get_nodes(self):
        return self.__adj_list.keys()

    def get_neighbors(self, vertex):
        return self.__adj_list.get(vertex, [])

    def size(self):
        return len(self.__adj_list)

class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex

if __name__ == "__main__":
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

    output = []
    for i in graph2.get_nodes():
        output.append(i.value)

    print(output)

    array = []
    for i in graph2.get_nodes():
        array.append(i)
    array2 = []
    for i in graph2.get_neighbors(array[0]):
        array2.append(i.vertex.value)

    print(array2)