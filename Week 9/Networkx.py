import networkx as nx
import matplotlib.pyplot as plt


g = nx.Graph()


# l = [1,2,3]
# g.add_nodes_from(l)

# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(1, 3)

# print(g.nodes)
# print(g.edges)


# g = nx.complete_graph(20)

# g = nx.gnp_random_graph(20, 0.1)
#g = nx.gnp_random_graph(9, 0.3)    #0.3 → 30% chance of edge between any two nodes

# print(g.nodes())
# print(g.edges())
# print(g.degree(0))


g = nx.barabasi_albert_graph(15,2)

nx.write_gexf(g, "./analysis1.gexf")


nx.draw(g)
plt.show()
