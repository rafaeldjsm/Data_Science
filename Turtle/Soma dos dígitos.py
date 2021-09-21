n = int(input("Digite um número inteiro: "))

cnt = n
k = 0

while cnt > 0:
    k = k + cnt % 10
    cnt = cnt // 10
    
print(k)