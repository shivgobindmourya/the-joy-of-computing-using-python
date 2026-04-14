import networkx as nx
import numpy as np

g = nx.read_edgelist(r"C:\Users\techn\Downloads\Python OEC\Week 9\dummy.txt")

n = list(g.nodes())
spl = []

for u in n:
    for v in n:
        if u != v:
            l = nx.shortest_path_length(g,u,v)
            print("Shortest path between :",u," and",v,"is of length",l)
            spl.append(l)


print("Min:", min(spl))
print("Max:", max(spl))
print("Average:", np.mean(spl))