#!/usr/bin/python2.7
# coding:utf-8

# Aurélien REY
# Groupe 3
# Théorie des graphes
# TP1 - Exercice 3

def ParcoursProfondeur(G, s, i = 0, d = list(), H = {}) :
	d.append(s)
	H[s] = i

	for n in G[s] :
		if not(n in d) :
			ParcoursProfondeur(G, n, i + 1, d, H)

	return H

g = {}
g['A'] = ['B', 'C', 'E']
g['B'] = ['A', 'D', 'F']
g['C'] = ['A', 'G']
g['D'] = ['B']
g['E'] = ['A', 'F']
g['F'] = ['B', 'E']
g['G'] = ['C']

# g = {}
# g['A'] = ['B', 'E']
# g['B'] = ['A', 'D', 'F']
# g['C'] = ['G']
# g['D'] = ['B']
# g['E'] = ['A', 'F']
# g['F'] = ['B', 'E']
# g['G'] = ['C']

result = ParcoursProfondeur(g, 'E')

if len(g) == len(result) :
	print "Le parcours passe par tous les sommets !"
else :
	print "Le parcours ne passe pas par tous les points ({}/{} points parcourus)".format(len(result), len(g))

for p in result.items() :
		print "{} > {}".format(p[0], p[1])

input()