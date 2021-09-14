n = int(input("Digite um inteiro para a base: "))
k = int(input("Digite um inteiro para o expoente: "))

mult = 1

for j in range(k):
    mult = mult*n
    
print(n,"elevado a",k,"é igual a",mult)
