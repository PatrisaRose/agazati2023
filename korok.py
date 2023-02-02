korokLista = []
def bekeres():
    i = 0
    #korok = ""
    while i < 5:
        kor = int(input("Kérlek adj meg egy életkort 0 és 120 között: "))
        if i == 4:
            korokLista.append(kor)
            #korok += kor
        else:
            korokLista.append(kor)
            #korok += kor + " : "
        i += 1
    #korokLista.append(korok)
    print(f"\t{korokLista}")

def elso_idos():
    i = 0
    elso = []
    while i < len(korokLista):
        if korokLista[i] > 70:
            elso.append(i)
            quit()
        else:
            i += 1

    return elso[0]

def konzolra_ir():
    print(f"Első idős ember korának helye a listában: {elso_idos()}")

def falj_ir():
    open("oreg.txt", "w", encoding="utf-8")

