def remove_repetidos(lst):
    '''
    Função para eliminar termos repetidos em uma lista e retornar 
    uma nova lista ordenada
    '''
    lista_temp = []
    for j,k in enumerate(lst):
        if k not in lst[j+1:]:
            lista_temp.append(k)
        
    return sorted(lista_temp)
