from functions import shannon, channel_capacity

def pr(p, m, t):
    h = shannon(p)
    vt = 1/(m * t)
    v = vt * h
    print(v)

def sr(xs, t):
    print(channel_capacity(xs, t))

if __name__ == "__main__":
    problem = int(input()) #3
    if problem == 1:
        pr([0.1, 0.2, 0.7], 2, 0.001) #1
    elif problem == 2:
        sr([0.34, 0.46, 0.16, 0.04], 0.2)