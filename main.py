import snap
from random import seed
from random import random
from collections import Counter
import graph


#--------------------------------------------------------------------------------------------------
#Main function

#Graph import and visualization
G2 = snap.GenRndGnm(snap.TUNGraph, 40, 70)
snap.DrawGViz(G2, snap.gvlDot, "output.png", "Grafo non diretto")

avg_len=0

for i in range(0,10):

    #Network Parameters
    threshold = 2
    k=4

    #Global Variables
    signed_edges = []
    nodes = []

    print("--------------------------------Starting iteration", i,"---------------------------------------- ")
    #Operations
    graph.edge_labeling(G2, signed_edges)
    S = graph.algorithm2(signed_edges, k)
    #S = graph.algorithm3(signed_edges, k)
    nodes = graph.cascade_function(S, threshold, signed_edges)
    print("Nodi influenzati ", nodes)
    print("Len nodi influenzati ", len(nodes))
    avg_len += len(nodes)

#Final print
print("Main completato")
print("------------------------------------------Risultato-------------------------------------------------")
print('Media Nodi influenzati: ',avg_len/10)
print("----------------------------------------------------------------------------------------------------")
