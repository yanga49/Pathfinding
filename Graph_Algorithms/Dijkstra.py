from Graph import Graph
from ShortestPath import ShortestPath
from Graph_Algorithms.Priority_Queue import PriorityQueue


class Dijkstra(ShortestPath):

    def shortest_path(self, graph: Graph, from_node_id, to_node_id):
        unvisited = PriorityQueue()
        unvisited.insert(from_node_id, float('-inf'))
        results = {}
        edge_to = {}
        dist_to = {}
        line_to = {}
        inserts = 0
        visited = 0
        compares = 0
        for i in graph.all_nodes:
            dist_to[i] = float('inf')
        edge_to[from_node_id] = None
        dist_to[from_node_id] = 0
        line_to[from_node_id] = None
        while not unvisited.is_empty():
            visited += 1
            current = unvisited.pop()[0]
            if current == to_node_id:
                break
            adjacent = graph.get_node(current).get_adjacents()
            for adj in adjacent:
                temp = dist_to[current] + graph.get_node(current).get_weight(adj)
                a = adj.get_node_id()
                compares += 1
                if a not in edge_to or temp < dist_to[a]:
                    dist_to[a] = temp
                    edge_to[a] = current
                    line_to[a] = graph.get_node(current).get_label(adj)
                    unvisited.insert(a, temp + line_change(line_to[current], line_to[a]))
                    inserts += 1
        results['edge_to'] = edge_to
        results['dist_to'] = dist_to
        results['line_to'] = line_to
        results['inserts'] = inserts
        results['visited'] = visited
        results['compares'] = compares
        return results

    def get_name(self):
        return "Dijkstra"

def line_change(prev_line, next_line):
    if prev_line == next_line or prev_line is None:
        return 0
    return 5