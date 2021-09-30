def é_hipotenusa(n):
    k = cnt = 1
    while k <= n and (n**2 - k**2)**0.5 != int((n**2 - k**2)**0.5):
        k+=1

    return k != n

def soma_hipotenusas(n):
    k = s = 0
    while k <= n:
        if é_hipotenusa(k):
            s+=k
        k+=1
    return s
