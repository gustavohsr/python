def computador_escolhe_jogada(n,m):
    #Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste 
    #em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. 
    #Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.   
    #retirando pelo menos 1 e no máximo m peças cada um.
    # n = 6 
    # m = 2

    if n > m:
       i = 1
       while(i < m):
            if (n-1)%(m+1) == 0:
                return i
            else:
                i = i + 1
                n = n - 1
    else:
        return n
    
    return i

def usuario_escolhe_jogada(n,m):
    
    if n <= 0 or m <= 0:
        print ("Valores inválidos!")
        return -1
    else: 
        if (n >= m):
            resp = int(input("Quantas peças você vai retirar? "))
            while (resp > m) or (resp < 1):
                print ("Opss! Jogada invalida! Tente novamente!")
                resp = int(input("Quantas peças você vai retirar? "))
        else:
            resp = int(input("Quantas peças você vai retirar? "))
            while (resp > n) or (resp < 1):
                print ("Opss! Jogada invalida! Tente novamente!")
                resp = int(input("Quantas peças você vai retirar? "))           
        return resp

def partida():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = int(input("Escolha: "))

    if escolha == 1:
        n = int(input("Quantas peças?  "))
        m = int(input("Limite de peças por jogada?  "))

        while (n <= 0) or (m <= 0):
            print("Valores inválidos!")
            n = int(input("Quantas peças?  "))
            m = int(input("Limite de peças por jogada?  "))
        else:
            if n%(m+1) == 0:
                print("VOCÊ começa!")
                while (n != 0):
                    resp_user = usuario_escolhe_jogada(n,m)
                    if resp_user == -1:
                        print("Jogada inválida")
                        resp_user = usuario_escolhe_jogada(n,m)
                    else:
                        print ("Você retirou ", resp_user, "peça(s)")
                        n = n - resp_user
                        print ("Agora restam ",n," peças no tabuleiro!")
                        
                    if n == 0:
                        print ("Você venceu!")
                    else:            
                        resp_comp = computador_escolhe_jogada(n,m)
                        print(" --> Computador tirou ",resp_comp," peças!")
                        n = n - resp_comp
                        print(" --> Agora restam ",n," peças no tabuleiro")
                        if n == 0:
                            print("Fim de jogo! O computador ganhou!")
            else:
                print("Computador começa!")
                while (n != 0):
                    resp_comp = computador_escolhe_jogada(n,m)
                    print(" --> Computador tirou ",resp_comp," peças!")
                    n = n - resp_comp
                    print(" --> Agora restam ",n," peças no tabuleiro")
                    
                    if n == 0:
                        print("Fim de jogo! O computador ganhou!")
                    else:
                        resp_user = usuario_escolhe_jogada(n,m)
                        print ("Você retirou ", resp_user, "peça(s)")
                        n = n - resp_user
                        print ("Agora restam ",n," peças no tabuleiro!")   
                        if n == 0:
                            print ("Você venceu!") 
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        i = 1
        placar_comp = 0
        placar_user = 0
        while (i <= 3):
            print("**** Rodada ",i," ****")
            # ------
            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogada? "))

            while (n <= 0) or (m <= 0):
                print("Valores inválidos!")
                n = int(input("Quantas peças?  "))
                m = int(input("Limite de peças por jogada?  "))
            else:
                if n%(m+1) == 0:
                    print("VOCÊ começa!")
                    while (n != 0):
                        resp_user = usuario_escolhe_jogada(n,m)
                        if resp_user == -1:
                            print("Jogada inválida")
                            resp_user = usuario_escolhe_jogada(n,m)
                        else:
                            print ("Você retirou ", resp_user, "peça(s)")
                            n = n - resp_user
                            print ("Agora restam ",n," peças no tabuleiro!")
                        
                        if n == 0:
                            print ("Você venceu!")
                            placar_user = placar_user + 1
                        else:            
                            resp_comp = computador_escolhe_jogada(n,m)
                            print(" --> Computador tirou ",resp_comp," peças!")
                            n = n - resp_comp
                            print(" --> Agora restam ",n," peças no tabuleiro")
                            if n == 0:
                                print("Fim de jogo! O computador ganhou!")
                                placar_comp = placar_comp + 1    
                else:
                    print("Computador começa!")
                    while (n != 0):
                        resp_comp = computador_escolhe_jogada(n,m)
                        print(" --> Computador tirou ",resp_comp," peças!")
                        n = n - resp_comp
                        print(" --> Agora restam ",n," peças no tabuleiro")
                        if n == 0:
                            print("Fim de jogo! O computador ganhou!")
                            placar_comp = placar_comp + 1
                            
                        else:
                            resp_user = usuario_escolhe_jogada(n,m)
                            print ("Você retirou ", resp_user, "peça(s)")
                            n = n - resp_user
                            print ("Agora restam ",n," peças no tabuleiro!")   
                            if n == 0:
                                print ("Você venceu!") 
                                placar_user = placar_user + 1
            # ------
            i = i + 1
        print ("Final do Campeonato!")
        print ("Placar: Computador ", placar_comp," x ",placar_user, " VOCÊ")
    else:
        print("***** Escolha 1 ou 2 *****")
        partida()
#partida()
#usuario_escolhe_jogada(0,2)
#usuario_escolhe_jogada(-1,3)
resp = computador_escolhe_jogada(3,1)
print(resp)
resp = computador_escolhe_jogada(14,4)
print(resp)
resp = computador_escolhe_jogada(13,4)
print(resp)
resp = computador_escolhe_jogada(6,2)
print(resp)