def ehprimo(n):
    k = 2
    
    while n % k != 0 and k <= int(n**0.5): 
        k+= 1
                      
    return n % k != 0 or n == 2

def n_primos(n):
    cnt = 0
    while n >= 2:
        if ehprimo(n):
            cnt+=1
        n+=-1
    return cnt
