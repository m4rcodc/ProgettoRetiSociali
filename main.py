import snap
from random import seed
from random import random
from collections import Counter
import graph
import matplotlib.pyplot as plt


#--------------------------------------------------------------------------------------------------
#Main function
avg_values=[]

#Graph import and visualization
G2 = snap.GenRndGnm(snap.TUNGraph, 40, 70)
snap.DrawGViz(G2, snap.gvlDot, "output.png", "Grafo non diretto")



for i in range(4,8):
    seed(1)
    avg_len=0
    print("\n\n")
    print("++++++++++++++++++++++++++++++Starting simulation with k=",i,"+++++++++++++++++++++++++++++++++++++++")
    k=i

    for i in range(0,10):

        #Network Parameters
        threshold = 2

        #Global Variables
        signed_edges = []
        nodes = []

        #Operations
        print("--------------------------------Starting iteration", i,"---------------------------------------- ")
        graph.edge_labeling(G2, signed_edges)
        #S = graph.algorithm2(signed_edges, k)
        S = graph.algorithm3(signed_edges, k)
        print("Initial Seed Set: ",S)
        nodes = graph.cascade_function(S, threshold, signed_edges)
        print("Influenced nodes: ",nodes)
        print("Length of influenced nodes: ",len(nodes))
        avg_len += len(nodes)

    avg_values.append(avg_len/10)
    #Final print
    print("Main completed")
    print("--------------------------------------------Result--------------------------------------------------")
    print('Average number of influenced nodes: ',avg_len/10)
    print("----------------------------------------------------------------------------------------------------")


# Dati di esempio
k = [4, 5, 6, 7]  # Valori assegnati a "k"

# Creazione del grafico
plt.plot(k, avg_values, marker='o', linestyle='-', color='b')

# Titoli degli assi e del grafico
plt.xlabel('k')
plt.ylabel('avg_value')
plt.title('Grafico k vs avg_values')

# Visualizzazione del grafico
plt.show()