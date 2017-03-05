#!/usr/bin/python2.7
# coding:utf-8

# Aurélien REY
# Groupe 3
# Théorie des graphes
# TP1 - Exercice 4

import random as rand

def Chaine(G, s, t) :
	d = list()
	current = s

	while current != t :
		d.append(current)
		current = G[current][rand.randint(0, len(G[current]) - 1)]

	d.append(t)

	return d

g = {}
g['A'] = ['B', 'C', 'E']
g['B'] = ['A', 'D', 'F']
g['C'] = ['A', 'G']
g['D'] = ['B']
g['E'] = ['A', 'F']
g['F'] = ['B', 'E']
g['G'] = ['C']

result = Chaine(g, 'E', 'C')

s = ""

for k in result :
	s += "{} > ".format(k)

s = s[:len(s) - 3]

print "La chaine {} est une chaine permettant d'aller du point E au point C".format(s)

input()