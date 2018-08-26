#The file contains the adjacency list representation of a simple undirected graph. 
#There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, 
#and the particular row (other entries except the first column) tells all the vertices 
#that the vertex is adjacent to. So for example, the $$6^{th}$$ row looks like : "6	155	56	52	120	......". 
#This just means that the vertex with label 6 is adjacent 
#to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc


#Your task is to code up and run the randomized contraction algorithm for the min cut problem 
#and use it on the above graph to compute the min cut.  
#(HINT: Note that you'll have to figure out an implementation of edge contractions.  
#Initially, you might want to do this naively, creating a new graph from the old every time 
#there's an edge contraction.  But you should also think about more efficient implementations.)   
#(WARNING: As per the video lectures, please make sure to run the algorithm many times 
#with different random seeds, and remember the smallest cut that you ever find.)  
#Write your numeric answer in the space provided.  So e.g., if your answer is 5, just type 5 in the space provided

import csv as csv
import random as random
import copy as copy



def minCut(G,E):

	Q = copy.deepcopy(G);
	
	s = random.sample(E,1);
	u = s[0][0]
	v = s[0][1]
	# rebinding list
	_E = [(i, j) for i, j in E if i!=u and j!=v]
	
	keys = Q.keys();
	# kind of like union find
	# list of each vertex and its cluster leader
	C = {}

	while len(keys) >2:
		#print "keys"+str(keys)
		# merge u and v
		# merge always to u
		#print "merging "+str(u)+" "+str(v)
		uEdges = Q[u]
		vEdges = Q[v]
		edges = vEdges + uEdges
		del Q[v]
		#assign leaders
		C[u] =u
		C[v] =u
		# now see if anyone had "v" as a leader, change to u
		for k in C.keys():
			if C[k] == v:
				C[k] = u
		
		# go through the edges of u
		# and find the ones that are on the same cluster 
		# i.e. u is the leader
		# and remove them
		_edges = copy.deepcopy(edges);
		for e in edges:
			if C.get(e)!=None and C[e] == u:
				#print "removing edge"+str(e)
				_edges.remove(e)
		edges = _edges
		Q[u] = edges
		
		#print Q	
		#print "union find"
		#print C

		#now select new u, v 
		# if we have more than 2 vertexes in our keys
		keys = Q.keys()
		if len(keys) ==2:
			#we are done
			#print Q
			break
		_vertex = v
		while _vertex==v:
			s = random.sample(_E,1);
			#print "u"+str(u)
			_u = s[0][0]
			_v = s[0][1]
			# when picking cases
			# never contracted before, if contracted get their leaders from C 
		#	print "_u and _v"+str(_u)+" "+str(_v)
			if C.get(_v)==None:
				v = _v
			if C.get(_u)==None:
				u = _u
			if C.get(_v) != C.get(_u):
				if C.get(_u)!=None:
					u =C[_u]
				if C.get(_v)!=None:
					v = C[_v]

			# the case C.get(_v) == C.get(_u) 
			# is the one in which both vertexes have already been merged
			# remove them from edge list try again
			# rebinding list
			_E = [(i, j) for i, j in E if i!=_u and j!=_v]

	minCutNumberOfVertexes = len(Q[keys[0]]) 
	#print ">>>local min"+str(minCutNumberOfVertexes);
	return minCutNumberOfVertexes 

f = open('./kargar.txt');
reader = csv.reader(f,delimiter='\t', quoting=csv.QUOTE_NONE)
#f = open('./testCase3.txt');
#reader = csv.reader(f,delimiter=' ', quoting=csv.QUOTE_NONE)

G = {}
V = 0
E =[]; #tuples of edges to pick an edge at random
for row in i#!/usr/bin/python

# Programming question week 3, http://w...content-available-to-author-only...s.org/ June 2012.

# The input file contains the adjacency list representation of a simple
# undirected graph.  There are 200 vertices labeled 1 to 200. The first column
# in the file represents the vertex label, and the particular row (other
# entries except the first column) tells all the vertices that the vertex is
# adjacent to. So for example, the 6th row looks like : "6 155    56	52
# 120 ......".  This just means that the vertex with label 6 is adjacent to
# (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

# Your task is to code up and run the randomized contraction algorithm for the
# min cut problem and use it on the above graph to compute the min cut. (HINT:
# Note that you'll have to figure out an implementation of edge contractions.
# Initially, you might want to do this naively, creating a new graph from the
# old every time there's an edge contraction. But you should also think about
# more efficient implementations.) (WARNING: As per the video lectures, please
# make sure to run the algorithm many times with different random seeds, and
# remember the smallest cut that you ever find.) Write your numeric answer in
# the space provided. So e.g., if your answer is 5, just type 5 in the space
# provided.

import sys
import random

def ParseGraph(filename):
  """Parse a graph into adjacency list format per programming Q.3

     Args:
     - filename: the on-disk graph representation
     Returns:
     (vertices, edges) where
       vertices = [vertex_1, vertex_2, ...]
       edges = [(vertex_1, vertex_2), ...]
  """
  vertices = []
  edges = set([])

  for l in open(filename):
    fields = [int(f) for f in l.split()]
    vertex = fields.pop(0)
    incident = [tuple(sorted([vertex, f])) for f in fields]
    vertices.append(vertex)
    edges.update(incident)

  return vertices, list(edges)

def RandomContraction(vertices, edges):
  while len(vertices) > 2:
    edge = random.choice(edges)
    a, b = edge
    vertices.remove(b)
    new_edges = []
    for e in edges:
      if e == edge:
        continue
      if b in e:
        if e[0] == b:
          other = e[1]
        if e[1] == b:
          other = e[0]
        e = tuple(sorted([a, other]))
      new_edges.append(e)
    edges = new_edges
      
  return vertices, edges

vertices, edges = ParseGraph(sys.argv[1])

minimum = sys.maxint
for i in range(0, 1000):
  v, e = RandomContraction(vertices[:], edges[:])
  print v, len(e)
  if len(e) < minimum:
    minimum = len(e)

print "min cut: %d" % minimumf:
	V = V+1
	v = int(row[0])
	tails = [] # not set as later this structure will hold repeated edges to one vertex
	l = len(row)
	for i in range(1,l):
		w = row[i]
		if w.isdigit():
			w = int(w)
			tails.append(w)
			t = (v,w);
			E.append(t);
	G[v] = tails

#print E

# now we need to start contracting graph
keys = G.keys();

#print G

minCutNumberOfVertexes = 1000;

counter = 10;

#print "Minimum found in "+str(counter)+" attempts "

while counter>0: 
	# pick a random starting vertex
	seed = random.sample(keys,1);
	seed = seed[0]
	#print "seed is "+strseed);
	minCutNumber = minCut(G,E)
	#print "The number of vertexes..."
	#print minCutNumber
	minCutNumberOfVertexes = min(minCutNumberOfVertexes,minCutNumber)
	counter = counter-1

#print "Final min:"
print(minCutNumberOfVertexes)


