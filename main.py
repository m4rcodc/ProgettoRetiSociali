import snap
import graph
import matplotlib.pyplot as plt
import time


#--------------------------------------------------------------------------------------------------
#Main function
#avg_values2=[]
avg_valuesSSCD=[]
avg_values3=[]
avg_values4=[]
avg_valuesTSS=[]
ti = time.time()

#Graph import and visualization
#G2 = snap.GenRndGnm(snap.TUNGraph, 400, 900)
G2 = snap.LoadEdgeList(snap.TUNGraph, "ego-Facebook.txt", 0, 1)
print("Graph with ",G2.GetNodes()," and ",G2.GetEdges()," edges loaded!")
snap.DrawGViz(G2, snap.gvlDot, "outputgraph.png", "Undirected Graph")

iterations = 10
threshold = 2
k_values = []

for k in range(10,60,10):
    avg_lenSSCD = 0
    avg_len3 = 0
    avg_len4 = 0
    avg_lenTSS = 0
    k_values.append(k)
    
    print("\n\n")
    print("++++++++++++++++++++++++++++++Starting simulation with k=",k,"+++++++++++++++++++++++++++++++++++++++")

    for i in range(0,iterations):

        #Global Variables
        signed_edges = []

        #Operations
        print("--------------------------------Starting iteration", i + 1,"---------------------------------------- ")
        signed_edges = graph.edge_labeling(G2)
        #S2 = graph.algorithm2(signed_edges, k)
        #S4 = graph.algorithmIdeato(signed_edges, k)
        S3 = graph.algorithm3(signed_edges, k, threshold)
        STSS = graph.algorithmTSS(G2, signed_edges, k, threshold)
        SSSCD = graph.SS_CD(G2, signed_edges, k)
        #print("Initial Seed Set alg2: ",S2)
        #print("Initial Seed Set algIdeato: ",S4)
        print("Initial Seed Set algSSCD: ",SSSCD)
        print("Initial Seed Set alg3: ",S3)
        print("Initial Seed Set algTSS: ",STSS)
        #nodes2 = graph.cascade_function(S2, threshold, signed_edges)
        nodesSSCD = graph.cascade_function(SSSCD, threshold, signed_edges)
        nodes3 = graph.cascade_function(S3, threshold, signed_edges)
        nodesTSS = graph.cascade_function(STSS, threshold, signed_edges)
        #nodes4 = graph.cascade_function(S4, threshold, signed_edges)
        #print("Influenced nodes: ",nodes2)
        #print("Length of influenced nodes alg2: ",len(nodes2))
        print("Length of influenced nodes algSSCD: ",len(nodesSSCD))
        print("Length of influenced nodes alg3: ",len(nodes3))
        print("Length of influenced nodes algTSS: ",len(nodesTSS))
        #print("Length of influenced nodes algIdeato: ",len(nodes4))
        #avg_len2 += len(nodes2)
        avg_lenSSCD += len(nodesSSCD)
        avg_len3 += len(nodes3)
        avg_lenTSS += len(nodesTSS)
        #avg_len4 += len(nodes4)

    #avg_values2.append(avg_len2/iterations)
    avg_valuesSSCD.append(avg_lenSSCD/iterations)
    avg_values3.append(avg_len3/iterations)
    avg_valuesTSS.append(avg_lenTSS/iterations)
    te = time.time()
    #avg_values4.append(avg_len4/iterations)
    #Final print
    print("Main completed")
    print("--------------------------------------------Result--------------------------------------------------")
    #print('Average number of influenced nodes by alg2: ',avg_len2/iterations)
    print('Average number of influenced nodes by algSSCD: ',avg_lenSSCD/iterations)
    print('Average number of influenced nodes by alg3: ',avg_len3/iterations)
    print('Average number of influenced nodes by algTSS: ',avg_lenTSS/iterations)
    #print('Average number of influenced nodes by algIdeato: ',avg_len4/iterations)
    print("The algorithm took ", te-ti," seconds to complete!")
    print("----------------------------------------------------------------------------------------------------")




# Dati di esempio

# Creazione del grafico
#plt.plot(k_values, avg_values2, marker='o', linestyle='-', color='b', label = 'Algoritmo 2')
plt.plot(k_values, avg_valuesSSCD, marker='o', linestyle='-', color='g', label = 'SSCD Algorithm')
plt.plot(k_values, avg_values3, marker='o', linestyle='-', color='r', label = '3rd Algorithm')
plt.plot(k_values, avg_valuesTSS, marker='o', linestyle='-', color='b', label = 'TSS Algorithm')
#plt.plot(k_values, avg_values4, marker='o', linestyle='-', color='y', label = 'AlgoritmoIdeato')


# Titoli degli assi e del grafico
plt.xlabel('k')
plt.ylabel('avg_influenced_nodes')
plt.legend()
plt.grid(True)
#plt.title('Threshold = '+str(threshold)+'; Probability = constant(0.01)')
plt.title('Threshold = '+str(threshold)+'; Probability = proportional')


# Visualizzazione del grafico
plt.show()
