from Graph_builder import Graph_builder
from Graph import Graph
from Csv_reader import Csv_reader
from Metric_Extractor import Metric_Extractor
from Itinerary import Itinerary
from Graph_Algorithms.Dijkstra import Dijkstra
from Graph_Algorithms.A_star import A_star
from Graph_Algorithms.Priority_Queue import PriorityQueue
from ShortestPath import ShortestPath
from Test import Test
from KPIs.CpuTime import CpuTime
from KPIs.ExecutionTime import ExecutionTime
import matplotlib.pyplot as plt
import time

csv_reader = Csv_reader()

london_sub_graph = Graph_builder(csv_reader, Graph())
london_sub_graph.create_station_nodes('_dataset/london.stations.csv')
london_sub_graph.create_connections('_dataset/london.connections.csv')
#london_sub_graph.graph.print_all_connections()
london_sub_metrics = Metric_Extractor(london_sub_graph.graph)
#print('Average Node Degree: '+str(london_sub_metrics.get_avg_degree()))
#print('Total Edge Count: '+str(london_sub_metrics.get_edge_count()))
#print('Total Node Count: '+str(london_sub_metrics.get_node_count()))
#london_sub_metrics.plot_node_dist()

# creating an itinerary from station 36 to station 289
itinerary = Itinerary(london_sub_graph.graph, 37, 123, A_star())
print(itinerary.find_shortest_path())
test = Test(london_sub_graph.graph, A_star(), ExecutionTime(), 37, 123)
print("execution time = ", test)
