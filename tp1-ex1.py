#!/usr/bin/python2.7
#coding:utf-8

# Aurélien REY
# Groupe 3
# Théorie des graphes
# TP1 - Exercice 1

from math import *

def erdosGallaiTheorem(d) :
	def somme(d, k) :
		r = 0

		for i in range(k) :
			r += d[i]

		return r

	while 0 in d :
		d.remove(0)

	if max(d) >= len(d) :
		return False

	r = somme(d, len(d))

	if r % 2 != 0 :
		return False

	for k in range(1, len(d) + 1) :
		n = 0

		for i in range(k + 1, len(d) + 1) :
			n += min(d[i - 1], k)

		if not(somme(d, k) <= k * (k - 1) + n) :
			return False

	return True

print erdosGallaiTheorem([0, 0, 1, 2, 3])