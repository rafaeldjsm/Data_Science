def soma_elementos (lst):
    '''
    Função que recebe como parâmetro uma lista com números inteiros e 
    devolve um número inteiro correspondente à soma dos elementos da lista recebida.
    '''
    sum = 0 
    for k in lst:
        sum = sum + k
    return sum
