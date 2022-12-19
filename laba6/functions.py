from math import factorial, log, log2
from array import *
from collections import Counter

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

def func(arr, ans):
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
        func(arr1, ans)
    if len(arr0) == 1:
        ans.append(arr0[0])
    else:
        func(arr0, ans)

def generator(count):
    prob = 1.0 / count
    gen = []
    for i in range(count):
        gen.append(["a" + str(i), prob, ""])
    return gen

def huffman(freq):
    class NodeTree(object):
        def __init__(self, left=None, right=None):
            self.left = left
            self.right = right

        def children(self):
            return self.left, self.right

        def __str__(self):
            return self.left, self.right


    def huffman_code_tree(node, binString=''):
        '''
        Function to find Huffman Code
        '''
        if type(node) is str:
            return {node: binString}
        (l, r) = node.children()
        d = dict()
        d.update(huffman_code_tree(l, binString + '0'))
        d.update(huffman_code_tree(r, binString + '1'))
        return d


    def make_tree(nodes):
        '''
        Function to make tree
        :param nodes: Nodes
        :return: Root of the tree
        '''
        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))
            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        return nodes[0][0]

    node = make_tree(freq)
    encoding = huffman_code_tree(node)
    for i in encoding:
        print(f'{i} : {encoding[i]}')