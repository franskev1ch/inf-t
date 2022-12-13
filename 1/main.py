a = float(input())
c = float(input())
mssg = input()
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

p1 = (a * pb1) / (a * pb1 + b * pb2)
p2 = (b * pb2) / (a * pb1 + b * pb2)

print(f'Вероятность первого события: {p1}')
print(f'Вероятность второго события: {p2}')