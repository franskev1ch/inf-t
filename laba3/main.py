from functions import entropy_source

def pr_3(hx, hy, hx_y): ###Задаача из примеров №3
    i = hx - hx_y
    hy_x = hy - i
    print(hy_x)

def sr_4(ps): ###Задача на самостоятельное решение №2
    print(entropy_source(ps))

if __name__ == "__main__":
    
    problem = int(input())

    if problem == 1:
        pr_3(3400, 6800, 700)
    elif problem == 2:
        sr_4([0.75, 0.25, 0.66, 0.33, 1, 0])