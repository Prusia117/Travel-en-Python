from modules.node import Node
#** El grafo es una estructura de datos que representa un conjunto de nodos y aristas. Para mas informacion ver el vídeo https://www.youtube.com/watch?v=vnNFiNVy9KM ó https://www.youtube.com/watch?v=lp-1rvtRYQg **#
class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def create_node(self, value):
        if value not in self.nodes:
            new_node = Node(value)
            self.nodes[value] = new_node

    def add_edges(self, first_node, second_node, road_weight):

        if first_node not in self.nodes:
            self.create_node(first_node)

        if second_node not in self.nodes:
            self.create_node(second_node)

        self.edges[(first_node, second_node)] = road_weight

    def neighbors(self, node):
        neighbors = []
        for (first_node, second_node) in self.edges:
            if first_node == node:
                neighbors.append(second_node)
        return neighbors

    def get_edge_weight(self, first_node, second_node):
        return self.edges.get((first_node, second_node), float('inf'))  



