import snap
from random import seed
from random import random
from collections import Counter

#G5 = snap.LoadEdgeList(snap.TUNGraph, "test.txt", 0, 1)
G2 = snap.GenRndGnm(snap.TUNGraph, 10, 20)

#G2 = snap.GenRndGnm(snap.TUndirNet, 4, 6)

#Compute function for proprability distribution
def getMaxDegree(value_src,value_dst):
   src_node_id = value_src  # ID del nodo sorgente
   dst_node_id = value_dst  # ID del nodo destinazione

   src_node = G2.GetNI(src_node_id)  #Prendiamo il nodo sorgente con id = src_node_id
   dst_node = G2.GetNI(dst_node_id)  #Prendiamo il nodo destinazione con id = dst_node_id

   src_node_deg = src_node.GetOutDeg()  #Prendiamo il grado del nodo sorgente
   dst_node_deg = dst_node.GetOutDeg()  #Prendiamo il grado del nodo destinazione

   degree =  1/max(src_node_deg, dst_node_deg)

   #print(degree)

   return degree #Restituiamo il quoziente tra 1 ed il max di src_deg e dst_deg

#Print graph
snap.DrawGViz(G2, snap.gvlDot, "output.png", "Grafo non diretto")


#--------------------------------------------------------------------------------------------------

#Labeling degli edge
signed_edges = []
seed(1)

for EI in G2.Edges():
    value = random()
    #if value <= 0.10:
    if value <= getMaxDegree(EI.GetSrcNId(),EI.GetDstNId()):
        signed_edges.append((EI.GetSrcNId(),EI.GetDstNId(),'-'))

    else:
        signed_edges.append((EI.GetSrcNId(),EI.GetDstNId(),'+'))

#for EI in signed_edges:
        #print('Signed edge',EI[0], EI[1], EI[2])


#--------------------------------------------------------------------------------------------------


#Assegnazione della threshold
threshold = 2
nodes = []

for node in G2.Nodes():
     nodes.append((node.GetId(), threshold))

#for node in nodes:
     #print('Threshold',node[0], node[1])


#--------------------------------------------------------------------------------------------------

#Applicazione algoritmo 2
 
 
def algorithm2(signed_edges):
 
    S = []
    k = 4

    #Find max positive node degree outsiede of seed set S
    def find_max_positive_degree(edge_list):
            
            S = []
            k = 4

            positives = []
            #maximum = 0
            for edge in edge_list:
                if edge[2] == '+':
                    positives.append(edge[0])
                    positives.append(edge[1])
                #maximum = max(Counter(positives), maximum)
            counter = Counter(positives)
                #maximum = max(counter.values())
            maximum = counter.most_common(1)[0][0]


            print(Counter(positives))
            return maximum
        #print(find_max_positive_degree(signed_edges))

    while len(S) < k:
            u = find_max_positive_degree(signed_edges)
            print('Max-degrees positive node', u)
            #togliere da signed_edges u
            signed_edges = [tupla for tupla in signed_edges if tupla[0] != u]
                            
            S.append(u)
            signed_edges = [tupla for tupla in signed_edges if tupla[1] != u]

            for EI in signed_edges:
                print('Signed edge',EI[0], EI[1], EI[2])

    print("Trovato seed set ", S," con lunghezza ",len(S))

    return S

#print("Trovato seed set ", S2," con lunghezza ",len(S2))


#--------------------------------------------------------------------------------------------------

#Applicazione algoritmo 3

def algorithm3(signed_edges):

    S = []
    K = 4


    def find_max_difference(edge_list):
        positives = []
        negatives = []

        for edge in edge_list:
            if edge[2] == '+':
              positives.append(edge[0])
              positives.append(edge[1])
            else:
              negatives.append(edge[0])
              negatives.append(edge[1])
     
        counter_positive = Counter(positives)
        counter_negative = Counter(negatives)
    
        print('Counter positive:',counter_positive)
        print('Counter negative:',counter_negative)

        counter_condition = counter_positive - counter_negative

        print(counter_condition)

        #La condizione deve essere verificata solo per gli elementi che sono presenti all'interno di questo array
        nodes_verify_condition = dict((k, v) for k, v in counter_condition.items() if v >= 0)

        print("I nodi che verificano la condizione d+ >= d- sono: ", nodes_verify_condition)

        maximum = 0
        maximum_key = ''

        for v in nodes_verify_condition.items():
            
            if v[1]/2 > maximum:
                maximum = v[1]/2
                maximum_key = v[0]

        return maximum_key


    while len(S) < K:
            u = find_max_difference(signed_edges)
            print('Max-difference node', u)
            #togliere da signed_edges u
            signed_edges = [tupla for tupla in signed_edges if tupla[0] != u]
                            
            S.append(u)

            signed_edges = [tupla for tupla in signed_edges if tupla[1] != u]

            for EI in signed_edges:
                print('Signed edge',EI[0], EI[1], EI[2])

    print("Trovato seed set ", S," con lunghezza ",len(S))

    return S


        #nodes_verify_condition= counter_condition.elements()

        #for value in nodes_verify_condition:
        #    print(value)

    find_max_difference(signed_edges)

#--------------------------------------------------------------------------------------------------

#Funzione di Cascading

#Function to retrieve positive and negative neighbors for every nodes

def node_neighbors(seed_set,edge_list):

    #Per ogni nodo nel S vediamo se corrisponde alla sorgente o destinazione di ogni arco presente in Signed Edges
    print("")
    node_info = []
    for node in seed_set:
        for edge in edge_list:
            if node == edge[0] | node == edge[1]:
                node_info.append((node, edge))
    
    return node_info

def find_neighbors_in_seedset(seed_set):
    #Dobbiamo prendere tutti i nodi fuori il seedset, ovvero in signed_edges - seedset
    #Dobbiamo cercare tutti gli archi che hanno come sorgente (o destinazione) node, 
    # e come destinazione(o sorgente) un nodo presente in seed_set
    # differenza tra signed_edge e seed set, poi andiamo a prendere il risultato e prendere tutti gli archi all'interno di signed_edge che hanno come
    #sorgente (o come destinazione) un nodo in risultato.
    print("Signed edges: ",signed_edges)
    print("Seed set", seed_set)
    nodes = set()
    #signed_edge = [0,1,2,3,4,5,6,7,8,9]
    seed_set = [3,8,6,9]
    filtered_edges = []
    
    for edge in signed_edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    
    node_list = list(nodes)
    print(node_list)

    outside_seed_set = list(set(node_list) - set(seed_set))
    print(outside_seed_set)

    for edge in signed_edges:
        source_node = edge[0]
        target_node = edge[1]

        if (source_node in outside_seed_set and target_node in outside_seed_set) or (source_node not in outside_seed_set and target_node not in outside_seed_set):
            continue
        filtered_edges.append(edge)
        
    print('Edge filtrati',filtered_edges)

    '''
    for edge in signed_edges:
        for node in seed_set:
            if not (edge[1] == node) and (edge[0] not in influence_node):
                influence_node.append(edge[0])
    print("Influence node: ",influence_node)
    for set_node in seed_set:
        for edge in node_info[1]:
            if edge[0] == node_info[0]:
                if edge[1] == set_node:
            if edge[1] == node_info[0]:
                if edge[0] == set_node:

    '''

#--------------------------------------------------------------------------------------------------

#Main applicazione

#algorithm3(signed_edges)

S = algorithm2(signed_edges)


#node_neighbors(S, signed_edges)
find_neighbors_in_seedset(S)

'''
max_out_degree = 0
node_max_id = 0

for NI in G2.Nodes():
    out_degree = NI.GetOutDeg()
    if out_degree > max_out_degree:
        max_out_degree = out_degree
        node_max_id = NI.GetId()

print("Max out-degree:", max_out_degree)
print("Max node out-degree:", node_max_id)
'''