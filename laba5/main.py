import math
from operator import itemgetter

task_2 = [
    ["мы", 0.37, ""],
    ["все", 0.13, ""],
    ["учились", 0.125, ""],
    ["как", 0.11, ""],
    ["понемногу", 0.08, ""],
    ["чему", 0.06, ""],
    ["нибудь", 0.0052, ""],
    ["и", 0.0023, ""],
    ["-", 0.05, ""],
]


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


def print_format(ans, task):
    print(task + "\n")
    for_print = sorted(ans, key=lambda x: x[1], reverse=True)
    for value in for_print:
        print("      '{}'           {}                {}".format(value[0], value[1], value[2]))
    print()


def generator(count):
    prob = 1.0 / count
    gen = []
    for i in range(count):
        gen.append(["a" + str(i), prob, ""])
    return gen


def eff(gen, ans):
    sr_inf = 0
    for i in gen:
        sr_inf += i[1] * math.log2(i[1])
    sr_inf *= -1

    n_sr = 0
    for i in ans:
        n_sr += len(i[2]) * i[1]

    print("Информация на один символ: {}".format(sr_inf/n_sr))


def main():
    ans = []
    func(task_2, ans)
    print_format(ans, "Задание №2")
    print(" {}".format(sum(map(lambda x: len(x[0]), ans)) / len(ans)))
    print("Задание №9")
    for i in range(5, 9):
        ans = []
        gen = generator(i)
        func(gen, ans)
        print_format(ans, "")
        eff(gen, ans)


if __name__ == "__main__":
    main()
