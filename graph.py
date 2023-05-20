#possibile algoritmo: prendere i nodi con un grado medio
import snap
from random import seed
from random import random
from collections import Counter
import copy

#Probability distribution

#G5 = snap.LoadEdgeList(snap.TUNGraph, "test.txt", 0, 1)


#G2 = snap.GenRndGnm(snap.TUndirNet, 4, 6)

#Compute function for proprability distribution
def getMaxDegree(G2,value_src,value_dst):
   src_node_id = value_src  # ID del nodo sorgente
   dst_node_id = value_dst  # ID del nodo destinazione

   src_node = G2.GetNI(src_node_id)  #Prendiamo il nodo sorgente con id = src_node_id
   dst_node = G2.GetNI(dst_node_id)  #Prendiamo il nodo destinazione con id = dst_node_id

   src_node_deg = src_node.GetOutDeg()  #Prendiamo il grado del nodo sorgente
   dst_node_deg = dst_node.GetOutDeg()  #Prendiamo il grado del nodo destinazione

   degree =  1/max(src_node_deg, dst_node_deg)

   #print(degree)

   return degree #Restituiamo il quoziente tra 1 ed il max di src_deg e dst_deg




#--------------------------------------------------------------------------------------------------------------------------

#Labeling degli edge
def edge_labeling(G2, signed_edges):

    for EI in G2.Edges():
        value = random()
        #if value <= 0.10:
        if value <= getMaxDegree(G2,EI.GetSrcNId(),EI.GetDstNId()):
            signed_edges.append((EI.GetSrcNId(),EI.GetDstNId(),'-'))

        else:
            signed_edges.append((EI.GetSrcNId(),EI.GetDstNId(),'+'))


#--------------------------------------------------------------------------------------------------------------------------

#Applicazione algoritmo 2
 
 
def algorithm2(signed_edges,k):
 
    S = []

    #Find max positive node degree outsiede of seed set S
    def find_max_positive_degree(edge_list):
            
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


            #print(Counter(positives))
            return maximum
        #print(find_max_positive_degree(signed_edges))

    while len(S) < k:
            u = find_max_positive_degree(signed_edges)
            #print('Max-degrees positive node', u)
            #togliere da signed_edges u
            signed_edges = [tupla for tupla in signed_edges if tupla[0] != u]
                            
            S.append(u)
            signed_edges = [tupla for tupla in signed_edges if tupla[1] != u]

            #for EI in signed_edges:
            #    print('Signed edge',EI[0], EI[1], EI[2])

    #print("Trovato seed set ", S," con lunghezza ",len(S))

    return S

#print("Trovato seed set ", S2," con lunghezza ",len(S2))


#--------------------------------------------------------------------------------------------------------------------------

#Applicazione algoritmo 3

def algorithm3(signed_edges,k):

    S = []

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
    
        #print('Counter positive:',counter_positive)
        #print('Counter negative:',counter_negative)

        counter_condition = counter_positive - counter_negative

        #print(counter_condition)

        #La condizione deve essere verificata solo per gli elementi che sono presenti all'interno di questo array
        nodes_verify_condition = dict((k, v) for k, v in counter_condition.items() if v >= 0)

        #print("I nodi che verificano la condizione d+ >= d- sono: ", nodes_verify_condition)

        maximum = 0
        maximum_key = ''

        for v in nodes_verify_condition.items():
            
            if v[1]/2 > maximum:
                maximum = v[1]/2
                maximum_key = v[0]

        return maximum_key


    while len(S) < k:
            u = find_max_difference(signed_edges)
            #print('Max-difference node', u)
            #togliere da signed_edges u
            signed_edges = [tupla for tupla in signed_edges if tupla[0] != u]
                            
            S.append(u)

            signed_edges = [tupla for tupla in signed_edges if tupla[1] != u]

            #for EI in signed_edges:
                #print('Signed edge',EI[0], EI[1], EI[2])

    #print("Trovato seed set ", S," con lunghezza ",len(S))

    return S


        #nodes_verify_condition= counter_condition.elements()

        #for value in nodes_verify_condition:
        #    print(value)

    find_max_difference(signed_edges)

#--------------------------------------------------------------------------------------------------------------------------

#Funzione di Cascading

#Function to retrieve positive and negative neighbors for every nodes
'''
def node_neighbors(seed_set,edge_list):

    #Per ogni nodo nel S vediamo se corrisponde alla sorgente o destinazione di ogni arco presente in Signed Edges
    print("")
    node_info = []
    for node in seed_set:
        for edge in edge_list:
            if node == edge[0] | node == edge[1]:
                node_info.append((node, edge))
    
    return node_info
'''

#--------------------------------------------------------------------------------------------------------------------------

#Function that apply this formula |N+(u) Intersect Inf[S,r-1] - |N-(u) Intersect Inf[S,r-1]

def find_neighbors_in_seedset(signed_edges,seed_set):
    #Dobbiamo prendere tutti i nodi fuori il seedset, ovvero in signed_edges - seedset
    #Dobbiamo cercare tutti gli archi che hanno come sorgente (o destinazione) node, 
    # e come destinazione(o sorgente) un nodo presente in seed_set
    # differenza tra signed_edge e seed set, poi andiamo a prendere il risultato e prendere tutti gli archi all'interno di signed_edge che hanno come
    #sorgente (o come destinazione) un nodo in risultato.
    #print("Signed edges: ",signed_edges)
    #print("Seed set", seed_set)
    nodes = set()
    filtered_edges = []

    for edge in signed_edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    
    #node_list = list(nodes)
    #print(node_list)

    outside_seed_set = list(set(nodes) - set(seed_set))
    #print('Outside seet set:',outside_seed_set)

    for edge in signed_edges:
        source_node = edge[0]
        target_node = edge[1]

        if (source_node in outside_seed_set and target_node in outside_seed_set) or (source_node not in outside_seed_set and target_node not in outside_seed_set):
            continue
        filtered_edges.append(edge)
        
    #print('Edge filtrati',filtered_edges)
    
    node_filtered = set()

    #for edge in filtered_edges:
    #    node_filtered.add(edge[0])
    #    node_filtered.add(edge[1])
    
    #set_node_filtered = 
    

    counter_difference = Counter()



    for item in filtered_edges:
        nodo_sorgente = item[0]
        nodo_destinazione = item[1]
        segno = item[2]
        if segno == '+':
             counter_difference[nodo_sorgente] += 1
             counter_difference[nodo_destinazione] += 1
        elif segno == '-':
             counter_difference[nodo_sorgente] -= 1
             counter_difference[nodo_destinazione] -= 1
    
    #print('Counter outside seed set', Counter(outside_seed_set))

    #S1 = [1,2,3,5,8]
    #S2 = [0:5, 1:4, 2:4, 3:2, 4:2, 5:2, 6:1, 7:1]
    #dobbiamo togliere da S2 tutte le chiavi NON presenti in S1
    
    for node in seed_set:
        del counter_difference[node]

    #print("Counter",counter_difference)
    return counter_difference


#--------------------------------------------------------------------------------------------------------------------------

#Cascade function

def cascade_function(seed_set, threshold, signed_edges):
    influenced_nodes = []
    previous_influenced_nodes = []
    step = 1
  
    influenced_nodes = copy.deepcopy(seed_set)
    
    while len(influenced_nodes) != len(previous_influenced_nodes):
        previous_influenced_nodes = copy.deepcopy(influenced_nodes)
        #print("------------------------------------------------------Inizio step ",step,"------------------------------------------------------- ")
        difference_nodes = find_neighbors_in_seedset(signed_edges, influenced_nodes)
        for node,value in difference_nodes.items():
            if value>=threshold:
                influenced_nodes.append(node)
        step+=1

    return influenced_nodes
    #print('Nodi influenzati',influenced_nodes)

