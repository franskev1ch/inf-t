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

    l = ["", "", "", "", "", "", ""]
    table2 = table.copy()
    
    table2["а"] = "00"
    table2["в"] = "01"

    i = 0
    for j in table2.keys():
        table2[j] = str(bin(i))
        i += 1
    print(table2.values())
    return

def sr():

    return

if __name__ == "__main__":
    pr()
    print()