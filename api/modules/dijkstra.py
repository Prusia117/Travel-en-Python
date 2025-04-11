from modules.graph import Graph
from modules.queue import Queue
from modules.data import nodes, distancias_reales

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.queue = Queue()

    def dijkstra_execute(self, start_node, end_node):
        distances = {}
        previous_nodes = {}

        for node in self.graph.nodes:

            distances[node] = float('inf')
            previous_nodes[node] = None
            self.queue.enqueue((node, distances[node]))

        distances[start_node] = 0
        self.queue.decrease_key(start_node, 0)

        while not self.queue.is_empty():

            current_node = self.queue.extract_min()

            for neighbor in self.graph.neighbors(current_node):
                weight = self.graph.get_edge_weight(current_node, neighbor)
                alt = distances[current_node] + weight

                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous_nodes[neighbor] = current_node
                    self.queue.decrease_key(neighbor, alt)

            if current_node == end_node:
                break

        sequence = []
        target = end_node

        while target is not None:

            sequence.append(target)
            target = previous_nodes[target]
        sequence.reverse()
        
        #** Este bloque es para cambiar el nombre de los paises a su nombre oficial **#
        for i in range(len(sequence)):
            match sequence[i]:
                case "Laos":
                    sequence[i] = "Lao PDR"
                case "North Korea":
                    sequence[i] = "Dem. Rep. Korea"
                case "South Korea":
                    sequence[i] = "Republic of Korea"
                case "Gambia":
                    sequence[i] = "The Gambia"
                case "Réunion":
                    sequence[i] = "Reunion"
                case "North Macedonia":
                    sequence[i] = "Macedonia"
                
        
        return distances[end_node], sequence



def dijkstra(first_country, second_country):
    
    if first_country == second_country:
        return 'El país de origen y el país de destino son iguales.'
    
    if first_country not in nodes or second_country not in nodes:
        return 'Uno de los países no está en la lista.'
    
    graph = Graph()

    for node in nodes:
        graph.create_node(node)

    for (pais1, pais2), distancia in distancias_reales.items():
        graph.add_edges(pais1, pais2, distancia)


    dijkstra = Dijkstra(graph)
    
    dijkstra_result = dijkstra.dijkstra_execute(first_country, second_country)
    print(dijkstra_result)
    return dijkstra_result
