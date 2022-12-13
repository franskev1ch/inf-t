from math import factorial, log, log2
from array import *

def acc(k, n):
    res = factorial(n)/factorial(n-k)

def comb(k, n):
    res = factorial(n)/(factorial(k) * factorial(n-k))
    return res

def bayes(a, b, pb1, pb2):
    res = [0, 0]
    res[0] = (a * pb1) / (a * pb1 + b * pb2)
    res[1] = (b * pb2) / (a * pb1 + b * pb2)
    return res

def shannon(a):
    h = 0.0
    for p in a:
        h += p * (log2(p))
    return -h

def hartley(m, n):
    big_n = pow(m, n)
    h = log2(big_n)
    return h

def entropy_source(ps):
    h = 0
    for p in ps:
        if p != 0:
            h += p * log2(p)
    h = -h
    return h

def entropy_cond(ps, matrix):
    h = 0
    i = 0
    for n in matrix:
        ht = entropy_source(n)
        h += ps[i] * ht
        i += 1
    return h
