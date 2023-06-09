import snap
from random import seed
from random import random
from collections import Counter
import graph
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor


#--------------------------------------------------------------------------------------------------
#Main function
avg_values2=[]
avg_values3=[]

#Graph import and visualization
#G2 = snap.GenRndGnm(snap.TUNGraph, 40, 70)
G2 = snap.LoadEdgeList(snap.TNGraph, "Network.txt", 0, 1)
print("Grafo con",G2.GetNodes()," e ",G2.GetEdges()," archi caricato!")
#snap.DrawGViz(G2, snap.gvlDot, "output.png", "Grafo non diretto")


def parallelized_function():
    seed(1)
    avg_len2 = 0
    avg_len3 = 0
    print("\n\n")
    print("++++++++++++++++++++++++++++++Starting simulation with k=",k,"+++++++++++++++++++++++++++++++++++++++")

    for i in range(0,10):

        #Network Parameters
        threshold = 4

        #Global Variables
        signed_edges = []
        nodes2 = []
        nodes3 = []

        #Operations
        print("--------------------------------Starting iteration", i,"---------------------------------------- ")
        graph.edge_labeling(G2, signed_edges)
        S2 = graph.algorithm2(signed_edges, k)
        S3 = graph.algorithm3(signed_edges, k)
        print("Initial Seed Set: ",S2)
        nodes2 = graph.cascade_function(S2, threshold, signed_edges)
        nodes3 = graph.cascade_function(S3, threshold, signed_edges)
        #print("Influenced nodes: ",nodes2)
        print("Length of influenced nodes: ",len(nodes2))
        avg_len2 += len(nodes2)
        avg_len3 += len(nodes3)

    # avg_values2.append(avg_len2/10)
    # avg_values3.append(avg_len3/10)
    #Final print
    print("Main completed")
    print("--------------------------------------------Result--------------------------------------------------")
    print('Average number of influenced nodes by alg2: ',avg_len2/10)
    print('Average number of influenced nodes by alg3: ',avg_len3/10)
    print("----------------------------------------------------------------------------------------------------")

    return (avg_len2,avg_len3)

pool = ThreadPoolExecutor()
results = []

for k in range(20,120,20):
    result = pool.submit(parallelized_function)
    results.append(result)

pool.shutdown()

for result in results:
    print("Result alg2: ",result[0])
    avg_values2.append(result[0])
    print("Result alg3: ",result[1])
    avg_values3.append(result[1])

# Dati di esempio
k = [20, 40, 60, 80, 100]  # Valori assegnati a "k"

# Creazione del grafico
plt.plot(k, avg_values2, marker='o', linestyle='-', color='b', label = 'Algoritmo 2')
plt.plot(k, avg_values3, marker='o', linestyle='-', color='r', label = 'Algoritmo 3')

# Titoli degli assi e del grafico
plt.xlabel('k')
plt.ylabel('avg_value')
plt.legend()
plt.grid(True)
plt.title('Grafico k vs avg_values')

# Visualizzazione del grafico
plt.show()