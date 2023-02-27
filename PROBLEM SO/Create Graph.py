import networkx as nx
network = nx.Graph()
network.add_nodes_from([1,2,3,4,5,6,7])
print(f"This network has now {network.number_of_nodes()} nodes.")

network.add_edge(1,2)
network.add_edge(1,3)
network.add_edge(1,4)
network.add_edge(1,5)
network.add_edge(2,4)
network.add_edge(3,1)
network.add_edge(3,5)
network.add_edge(3,7)
network.add_edge(5,3)
network.add_edge(5,6)
network.add_edge(6,7)

import matplotlib.pyplot as plt
color_list = ["gold", "red", "violet","pink","orange","grey","brown"]
plt.figure(figsize=(8, 6))
plt.title('Example of Graph Representation', size=10)

nx.draw_networkx(network,node_color=color_list, with_labels=True)

plt.show()