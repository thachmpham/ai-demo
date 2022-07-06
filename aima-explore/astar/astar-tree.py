import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node('Arad', f=350)
G.add_node('Zerind', f=431)
G.add_node('Sibiu', f=372)
G.add_node('Oradea', f=654)
G.add_node('Timisoara', f=435)
G.add_node('Fagara', f=393)
G.add_node('Bucharest', f=450)
G.add_node('Rimnicu', f=406)
G.add_node('Pitesti', f=406)
G.add_node('Craiova', f=518)

G.add_edge('Arad', 'Zerind')
G.add_edge('Arad', 'Sibiu')
G.add_edge('Arad', 'Timisoara')

G.add_edge('Sibiu', 'Fagara')
G.add_edge('Sibiu', 'Rimnicu')
G.add_edge('Sibiu', 'Oradea')


G.add_edge('Fagara', 'Bucharest')

G.add_edge('Rimnicu', 'Pitesti')
G.add_edge('Rimnicu', 'Craiova')

G.add_edge('Pitesti', 'Bucharest')

plt.figure(figsize=(10,10))

pos = nx.planar_layout(G)

nodes = nx.draw_networkx_nodes(G, pos, node_color='w')
# nodes.set_edgecolor('black')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrowsize=20)


plt.show()
