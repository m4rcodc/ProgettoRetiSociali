import snap
import graph
import matplotlib.pyplot as plt


#--------------------------------------------------------------------------------------------------
#Main function
avg_values2=[]
avg_values3=[]
avg_values4=[]

#Graph import and visualization
#G2 = snap.GenRndGnm(snap.TUNGraph, 200, 300)
G2 = snap.LoadEdgeList(snap.TUNGraph, "test.txt", 0, 1)
print("Grafo con",G2.GetNodes()," e ",G2.GetEdges()," archi caricato!")
#snap.DrawGViz(G2, snap.gvlDot, "output.png", "Grafo non diretto")

rnge = 1

for k in range(5,35,5):
    avg_len2 = 0
    avg_len3 = 0
    avg_len4 = 0
    
    print("\n\n")
    print("++++++++++++++++++++++++++++++Starting simulation with k=",k,"+++++++++++++++++++++++++++++++++++++++")

    for i in range(0,rnge):
        #seed(1)

        #Network Parameters
        threshold = 2

        #Global Variables
        signed_edges = []
        nodes2 = []
        nodes3 = []
        nodes4 = []

        #Operations
        print("--------------------------------Starting iteration", i,"---------------------------------------- ")
        signed_edges = graph.edge_labeling(G2)
        S2 = graph.algorithm2(signed_edges, k)
        S3 = graph.algorithm3(signed_edges, k, threshold)
        S4 = graph.algorithmIdeato(signed_edges, k)
        print("Initial Seed Set alg2: ",S2)
        print("Initial Seed Set alg3: ",S3)
        print("Initial Seed Set alg4: ",S4)
        nodes2 = graph.cascade_function(S2, threshold, signed_edges)
        nodes3 = graph.cascade_function(S3, threshold, signed_edges)
        nodes4 = graph.cascade_function(S4, threshold, signed_edges)
        #print("Influenced nodes: ",nodes2)
        print("Length of influenced nodes alg2: ",len(nodes2))
        print("Length of influenced nodes alg3: ",len(nodes3))
        print("Length of influenced nodes alg4: ",len(nodes4))
        avg_len2 += len(nodes2)
        avg_len3 += len(nodes3)
        avg_len4 += len(nodes4)

    avg_values2.append(avg_len2/rnge)
    avg_values3.append(avg_len3/rnge)
    avg_values4.append(avg_len4/rnge)
    #Final print
    print("Main completed")
    print("--------------------------------------------Result--------------------------------------------------")
    print('Average number of influenced nodes by alg2: ',avg_len2/rnge)
    print('Average number of influenced nodes by alg3: ',avg_len3/rnge)
    print('Average number of influenced nodes by alg4: ',avg_len4/rnge)
    print("----------------------------------------------------------------------------------------------------")




# Dati di esempio
k = [5,10,15,20,25,30]  # Valori assegnati a "k"

# Creazione del grafico
plt.plot(k, avg_values2, marker='o', linestyle='-', color='b', label = 'Algoritmo 2')
plt.plot(k, avg_values3, marker='o', linestyle='-', color='r', label = 'Algoritmo 3')
plt.plot(k, avg_values4, marker='o', linestyle='-', color='g', label = 'AlgoritmoIdeato')

# Titoli degli assi e del grafico
plt.xlabel('k')
plt.ylabel('avg_value')
plt.legend()
plt.grid(True)
plt.title('Grafico k vs avg_values')

# Visualizzazione del grafico
plt.show()
