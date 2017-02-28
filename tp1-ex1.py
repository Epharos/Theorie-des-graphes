#!/usr/bin/python2.7
#coding:utf-8

# Aurélien REY
# Groupe 3
# Théorie des graphes
# TP1 - Exercice 1

from math import *

def erdosGallaiTheorem(d) :
	r = somme(d, len(d))

	if r % 2 != 0 :
		print "stop 1"
		return False

	for k in range(1, len(d) + 1) :
		n = 0

		for i in range(k + 1, len(d) + 1) :
			n += min(d[i - 1], k)

		if not(somme(d, k) <= k * (k - 1) + n) :
			print "stop 2 à k =", k
			return False

	return True

def somme(d, k) :
	r = 0

	for i in range(k) :
		r += d[i]

	return r

print erdosGallaiTheorem([1, 1, 1, 3])