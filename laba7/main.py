
def pr(a:bin, b:bin):
    res = str(bin(a ^ b))
    print(res)
    d = str.count(res, '1')
    print(d)

def sr(a):
    a1 = int(a[0]) ^ int(a[1]) ^ int(a[3]) ^ int(a[4]) ^ int(a[6])
    a2 = int(a[0]) ^ int(a[2]) ^ int(a[3]) ^ int(a[5]) ^ int(a[6])
    a4 = int(a[1]) ^ int(a[2]) ^ int(a[3]) ^ int(a[7])
    a8 = int(a[4]) ^ int(a[5]) ^ int(a[6]) ^ int(a[7])
    s = str(a1) + str(a2) + a[2] + str(a4) + a[4:7] + str(a8) + a[8:12]
    print(s)

if __name__ == "__main__":
    print("Пример №1")
    pr(0b100101100, 0b110110101)
    print("Задание №8")
    sr('10011010')