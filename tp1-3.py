#!/usr/bin/python2.7
# coding:utf-8

# Aurélien REY
# Groupe 3
# Théorie des graphes
# TP1 - Exercice 3

def ParcoursProfondeur(G, s, d = list()) :
	d.append(s)

	for n in G[s] :
		if not(n in d) :
			ParcoursProfondeur(G, n, d)

	H = {}

	for i, v in enumerate(d) :
		H[v] = i

	return H

g = {}
g['A'] = ['B', 'C', 'E']
g['B'] = ['A', 'D', 'F']
g['C'] = ['A', 'G']
g['D'] = ['B']
g['E'] = ['A', 'F']
g['F'] = ['B', 'E']
g['G'] = ['C']

result = ParcoursProfondeur(g, 'E')

if len(g) == len(result) :
	print "Le parcours passe par tous les sommets !"
else :
	print "Le parcours ne passe pas par tous les points ({}/{} points parcourus)".format(len(result), len(g))

for p in result.items() :
		print "{} > {}".format(p[0], p[1])