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

def channel_capacity(xs, t):
    vt = 1 / t
    m = len(xs)
    c = (1 /( t * 0.001)) * log2(m)
    return c

def info_per_symbol(gen, b):
    sr_inf = 0
    for i in gen:
        sr_inf += i[1] * log2(i[1])
    sr_inf *= -1

    n_sr = 0
    for i in b:
        n_sr += len(i[2]) * i[1]

    return sr_inf/n_sr

def table(arr, ans):
    half = sum(map(lambda x: x[1], arr))
    sum1 = 0
    index = 1
    for i, j in enumerate(arr):
        sum1 += j[1]
        if sum1 * 2 >= half:
            index = i + (abs(2 * sum1 - half) < abs(2 * (sum1 - j[1]) - half))
            break

    arr0, arr1 = [], []
    for i in arr[:index]:
        i[2] += '0'
        arr0.append(i)
    for i in arr[index:]:
        i[2] += '1'
        arr1.append(i)
    if len(arr1) == 1:
        ans.append(arr1[0])
    else:
        table(arr1, ans)
    if len(arr0) == 1:
        ans.append(arr0[0])
    else:
        table(arr0, ans)