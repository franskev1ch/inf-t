from functions import huffman


def pr(a):
    huffman(a)
    return

def sr(a):
    huffman(a)
    return

if __name__ == "__main__":
    print("Пример №2")
    a = [('A', 0.25), ('B', 0.22), ('C', 0.13), ('D', 0.11), ('E', 0.1), ('F', 0.09), ('G', 0.07), ('H', 0.03)]
    pr(a)
    print("Задача № 3")
    a = [('x1', 0.45), ('x2', 0.3), ('x3', 0.15), ('x4', 0.1)]
    sr(a)