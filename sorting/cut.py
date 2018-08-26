#!/usr/bin/python

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
    print(vertex)
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

minimum = sys.maxsize
for i in range(0, 1000):
  v, e = RandomContraction(vertices[:], edges[:])
#  print v, len(e)
  if len(e) < minimum:
    minimum = len(e)

print(minimum)
