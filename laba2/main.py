from functions import acc, comb, bayes, shannon, hartley
from math import factorial, log, log2
from array import *

def pr1(m, n, c):
    res = 0.0
    for i in range(0, c+1):
        p = (comb(i, m) * comb(m - i, n - m)) / comb(m, n)
        res += p
    print(res)

def pr2(a, c, mssg):
    m1 = "11111"
    m2 = "00000"
    b = 1 - a
    pb1 = 1
    pb2 = 1
    for i in range(0,5):
        if mssg[i] == m1[i]:
            pb1 *= c
        else:
            pb1 *= 1 - c

    for i in range(0,5):
        if mssg[i] == m2[i]:
            pb2 *= c
        else: 
            pb2 *= 1 - c

    r = bayes(a, b, pb1, pb2)
    p1 = r[0]
    p2 = r[1]
    
    print(f'Вероятность первого события: {p1}')
    print(f'Вероятность второго события: {p2}')

def pr3(ps):
    m = [["X", "Pi"], ["0",""], ["1",""]]
    s = str(ps)
    s = s + "(q+1-p)"
    m[1][1] = s
    s = str(1 - ps)
    s = s + "(p+1-q)"
    m[2][1] = s
    print(m)

def pr4(ps, n):
    m = [["X", "Pi"], ["1",""], ["2",""], ["3",""], ["4",""]]
    for i in range(n):
        m[i+1][1] = pow(ps, i) * (1 - ps)
    m[n][1] = pow(ps, i) * (1 - ps) + pow(ps, n)
    print(m)

def pr5(x, y):
    res = (y - 3)/2 - (x - 3)/2
    print(res)

def pr2_1(a):
    h = shannon(a)
    print(h)
    res = 1 - (h/log2(len(a)))
    print(res)

def sr2(a):
    h = shannon(a)
    print(h)

if __name__ == "__main__":
    
    problem = int(input())

    if problem == 1:
        m = 3 #3
        n = 6 #6
        c = 2 #2
        pr1(m, n, c)
    elif problem == 2:
        a = 0.7 #0.7
        c = 0.6 #0.6
        mssg = "10110"  #10110
        pr2(a, c, mssg)
    elif problem == 3:
        ps = 0.5 #0.5
        pr3(ps)
    elif problem == 4:
        ps = 0.6 #0.6
        n = 4 #4
        pr4(ps, n)
    elif problem == 5:
        x = 3.5 #3.5
        y = 4.5 #4.5
        pr5(x, y)
    elif problem == 6:
        a = [0.2, 0.3, 0.4, 0.1]
        pr2_1(a)
    elif problem == 7:
        a = [0.25, 0.25, 0.34, 0.16]
        sr2(a)