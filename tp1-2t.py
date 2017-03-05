#!/usr/bin/python2.7
# coding:utf-8

# Aurélien REY
# Groupe 3
# Théorie des graphes
# TP1 - Exercice 2

def graph(d) :
	def maxIndex(d, c = list()) :
		current, currentIndex = d[0], 0

		for i in range(len(d)) :
			if d[i] >= current and not(i in c) :
				current = d[i]
				currentIndex = i

		return currentIndex

	def maxIndex2(d, mi) :
		counted = list()
		counted.append(mi)

		index = list()

		for i in range(d[mi]) :
			index.append(str(maxIndex(d, counted)))
			counted.append(maxIndex(d, counted))

		return index

	def somme(d, k) :
		r = 0

		for i in range(k) :
			r += d[i]

		return r

	def getValues(g, v) :
		l = list()

		for i in g.keys() :
			if v in g[i] :
				l.append(i)

		return l

	g = {}

	if len(d) % 2 == 0 :
		l = len(d) // 2
	else :
		l = len(d) // 2 + 1

	for i in range(l) :
		if somme(d, len(d)) % 2 != 0 :
			print "La somme des degres est impaire, impossible !"
			return

		a = maxIndex(d)
		g[str(a)] = maxIndex2(d, a)

		for k in maxIndex2(d, a) :
			d[int(k)] -= 1

		d[a] = 0

	for k in range(len(d)) :
		if not(str(k) in g) :
			g[str(k)] = getValues(g, str(k))
		else :
			for v in getValues(g, str(k)) :
				if not(v in g[str(k)]) :
					g[str(k)].append(v)

	for p in g.items() :
		print "{} > {}".format(p[0], p[1])

	return g

g = graph([1, 1, 2, 2, 6, 3, 2, 3])
input()