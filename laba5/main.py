#from ..functions import shannon

def pr():
    table = {
        "а" : "0.3",
        "в" : "0.2",
        "л" : "0.15",
        "и" : "0.1",
        "е" : "0.1",
        "с" : "0.08",
        "к" : "0.07"
    }

    l = [""] * 7
    table2 = table.copy()
    
    s = 0
    b = -1
    for k in table.keys():
        if s >= 0.5:
            break        
        s += float(table[k])
        b += 1
    
    for i in range(len(l)):
        if i <= b:
            l[i] = "0"
        else:
            l[i] = "1"

    co = b + 1
    while co > 1:
        l[0:int(co/2)] = map(("0").__add__ , l[0:int(co/2)])
        l[int(co/2):int(co)] = map(("1").__add__ , l[int(co/2):int(co)])
        print(l)
        co = co / 2
    
    co = len(l) - b - 1
    while co > 1:
        beg = int(len(l) - co)
        mid = beg + int(co/2)
        l[beg:mid] = map(("0").__add__ , l[beg:mid])
        l[mid:len(l)] = map(("1").__add__ , l[mid:len(l)])
        print(l)
        co = co / 2
    print(l)
    return

def sr():

    return

if __name__ == "__main__":
    pr()
    print()