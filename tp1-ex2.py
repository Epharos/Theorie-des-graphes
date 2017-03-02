#!/usr/bin/python2.7
#coding:utf-8

# Aurélien REY
# Groupe 3
# Théorie des graphes
# TP1 - Exercice 2

def graph(d) :
	def maxIndex(d) :
		current, currentIndex = d[0], 0

		for i in range(len(d)) :
			if d[i] >= current :
				current = d[i]
				currentIndex = i

		return currentIndex

	def maxIndex2(d, mi) :
		temp = list(d)
		del temp[mi]

		index = list()

		for i in range(d[mi]) :
			index.append(maxIndex(temp))
			del temp[maxIndex(temp)]

		return index

	def somme(d, k) :
		r = 0

		for i in range(k) :
			r += d[i]

		return r

	while 0 in d :
		d.remove(0)

	if somme(d, len(d)) % 2 != 0 :
		print "La somme des degrès est impaire, impossible !"
		return

	i = maxIndex(d)
	l = maxIndex2(d, i)

	print i, l

graph([1, 1, 2, 2, 2, 3, 3, 6])