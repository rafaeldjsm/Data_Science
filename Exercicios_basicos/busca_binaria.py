def busca(lista,elem):
    prim = 0
    ult = len(lista)-1

    while prim <= ult:
        meio = (prim+ult)//2
        print(meio)
        if lista[meio] == elem:
            return meio
        
        elif lista[meio] > elem:
            ult = meio - 1
        else:
            prim = meio + 1
            
    return False
