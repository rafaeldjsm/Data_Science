def main():

    
    print("Bem-vindo ao jogo do NIM! Escolha:")
    tip = tip = int(input(
        "1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))

    while tip not in [1,2]:
        print("Opção Inválida, insira um novo valor")   
        tip = int(input(
            "1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))

    if tip == 2:
        print("\nVoce escolheu um campeonato!")
        num_part = 3
    else:
        print("\n","Voce escolheu uma partida isolada!")
        num_part = 1
 
    campeonato(num_part)
        
#########################################################
def campeonato(num_part):
    pt_cpt = pt_jgt = 0
    for k in range(num_part):
        print("\n**** Rodada %d ****"%(k+1))
        pt_cp,pt_jg = partida()
        pt_cpt = pt_cpt + pt_cp
        pt_jgt = pt_jgt + pt_jg

    print("Placar: Você %d X %d Computador"%(pt_jgt,pt_cpt))

    
#########################################################

def usuario_escolhe_jogada(n,m):

   
    pj = int(input("\nQuantas peças você vai tirar? "))

    if pj <= m and pj > 0 and pj <= n:
        n2 = n - pj
        
        if pj == 1:
            print("\nVocê tirou uma peça.")
        else:
            print("\nVoce tirou %d peças."%pj)
            
        if n2 == 0:
            print("Fim do jogo! Você ganhou!")
            
        return pj
    
    elif pj > n and pj > m:
        print("\nOops! Jogada inválida! Tente de novo.")
        return usuario_escolhe_jogada(n,m)
    
    else:
        print("\nOops! Jogada inválida! Tente de novo.")
        return usuario_escolhe_jogada(n,m)
    

#########################################################
def computador_escolhe_jogada(n,m):


    nm1 = n //(m+1)
    rst = n %(m+1)
    
    if nm1 > 0 and rst != 0:
        cj = n - nm1*(m+1)
        
    elif rst == 0:
        cj = m
        
    else:
        cj = n

    n2 = n - cj    
    if cj == 1:            
        print("\nO computador tirou uma peça.")
    else:
        print("\nO computador tirou %d peças."%cj)
        
    if n2 == 0:
        print("Fim do jogo! O computador ganhou!")    
    
    return cj
#########################################################
def msgpecas(n):
    if n > 0:
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam %d peças no tabuleiro."%n)  

#########################################################

def partida():
    
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if m <= n:

        pt_jg = 0
        pt_cp = 0
        cnt_cp = cnt_jg = 0
        
        if n % (m+1) == 0:
            print("\nVoce começa!")
            n = n- usuario_escolhe_jogada(n,m)
            cnt_jg = cnt_jg +1
            msgpecas(n)
            if n == 0:
                pt_jg +=1

        else:
            print("\nComputador começa!")
            n = n- computador_escolhe_jogada(n,m)
            cnt_cp = cnt_cp +1
            msgpecas(n)
            if n == 0:
                pt_cp +=1
                
        
        if cnt_cp > cnt_jg:
            while n > 1:
                n = n-usuario_escolhe_jogada(n,m)
                msgpecas(n)
                if n == 0:
                    pt_jg +=1
                else:    
                    n = n-computador_escolhe_jogada(n,m)
                    msgpecas(n)
                    if n == 0:
                        pt_cp +=1
        else:
            while n >= 1:
                n = n-computador_escolhe_jogada(n,m)
                msgpecas(n)
                if n == 0:
                    pt_cp +=1
                else:
                    n = n-usuario_escolhe_jogada(n,m)
                    msgpecas(n)                
                    if n == 0:
                        pt_cp +=1

        return pt_cp,pt_jg
    else:
        partida()
           
        
main()
