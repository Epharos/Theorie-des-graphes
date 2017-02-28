#!/usr/bin/python2.7
#coding:utf-8

def graph(name) :
	file = open(name, 'r')
	lines = file.readlines()
	graph = {}

	for l in lines :
		l2 = l.split(" ")

		if not(l2[0] in graph) :
			graph[l2[0]] = list()

		graph[l2[0]].append(l2[1][:len(l2[1]) - 1])

		if not(l2[1] in graph) :
			graph[l2[1][:len(l2[1]) - 1]] = list()

		graph[l2[1][:len(l2[1]) - 1]].append(l2[0])

	return graph

def dgraph(name) :
	file = open(name, 'r')
	lines = file.readlines()
	graph = {}

	for l in lines :
		l2 = l.split(" ")

		if not(l2[0] in graph) :
			graph[l2[0]] = list()

		graph[l2[0]].append(l2[1][:len(l2[1]) - 1])

	return graph

def nombre_sommets(G) :
	return len(G)

def nombre_aretes(G) :
	r = 0

	for l in G.values() :
		r += len(l)

	return r

def deg(v, G) :
	if not(v in G) :
		return 0

	return len(G[v])

def present(v, w, G) :
	if not(v in G) :
		return 0

	if not(w in G[v]) :
		return 0

	return 1

def insert(i, j, G) :
	if not(i in G) :
		G[i] = list()
		G[i].append(j)
		return 1

	if not(j in G[i]) :
		G[i].append(j)
		return 1

	return 0

def supp(i, j, G) :
	if i in G :
		if j in G[i] :
			G[i].remove(j)
			return 1

	return 0

# s = "jean"
# v = "elodie"
# G = dgraph("test.txt")

# print v, "est dans la liste d'amis de", s, "? >", present(s, v, G)
# print insert('jean', 'elodie', G)
# print v, "est dans la liste d'amis de", s, "? >", present(s, v, G)
# print insert('jean', 'elodie', G)
# print s, "est dans la liste d'amis de", v, "? >", present(v, s, G)
# print supp('elodie', 'jean', G)
# print s, "est dans la liste d'amis de", v, "? >", present(v, s, G)
# print supp('elodie', 'jean', G)