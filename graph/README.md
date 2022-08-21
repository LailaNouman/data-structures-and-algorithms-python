# Graphs
A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links, the interconnected 
objects are represented by points termed as vertices, and the links that connect the vertices are called edges.

## Challenge
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

#### add node
- Arguments: value
- Returns: The added node
- Add a node to the graph
#### add edge
- Arguments: 2 nodes to be connected by the edge, weight (optional)
- Returns: nothing
- Adds a new edge between two nodes in the graph
- If specified, assign a weight to the edge
- Both nodes should already be in the Graph
#### get nodes
- Arguments: none
- Returns all of the nodes in the graph as a collection (set, list, or similar)
#### get neighbors
- Arguments: node
- Returns a collection of edges connected to the given node
- Include the weight of the connection in the returned collection
#### size
- Arguments: none
- Returns the total number of nodes in the graph

## Approach & Efficiency
##### For all of them
- Time complexity: Big O(1)
- Space complexity: Big O(1)

## API
- add_node(): Adds a node to the graph.
- add_edge(): Adds an edge to connect two nodes in a graph.
- get_nodes(): Returns all nodes in the graph.
- get_neighbors(): Returns all the connected nodes for the given node.
- size(): Returns the number of the nodes in the graph.