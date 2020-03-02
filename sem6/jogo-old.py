def computador_escolhe_jogada(n,m):
     #Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste 
     #em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. 
     #Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.   
    #n = 2
    #m = 1
    # n = n - 1 #  retirando pelo menos 1 e no máximo m peças cada um.

    if n > m:
       i = 1
       n = n - i
       if n == 0:
                print(" --> Computador tirou uma peça!")    
                print("Fim de jogo! O computador ganhou!")
                return n
       else:
           while(i <= m):
                if n%(m+1) == 0:
                    print(" --> Computador tirou ",i," peças!")
                    print(" --> Agora restam ",n," peças no tabuleiro")
                    i = m
                    return n
                else:
                    n = n - i
                    if n == 0:
                        i = m
                        print(" --> Computador tirou uma ",i," peça!")    
                        print("Fim de jogo! O computador ganhou!")
                    else:
                        i = i + 1
                return n
    else:
        print(" --> Computador tirou uma ",n," peça!")    
        print("Fim de jogo! O computador ganhou!")
        return 0

    #n = n - m
    #if n%(m+1) == 0:
    #tabuleiro = n
    #eh_multiplo = True

    #while (not eh_multiplo):
    #    if n%(m+1) != 0:
    #        n = n - 1
    #    else:
    #        eh_multiplo = False
            #multiplo = n

    #   if n == 0:
    #        eh_multiplo = False
    #        n = tabuleiro - m
            #n = n - m
        
    #if (m == 1):
    #    print(" --> Computador tirou uma peça!")
    #    print(" --> Fim de jogo! O computador ganhou!")
    #    n = 0
    #if (n == 0):
    #    print(" --> Computador tirou ",m," peça!")    
    #    print("Fim de jogo! O computador ganhou!")
    #else:
    #    print(" --> Computador tirou ",m," peças!")
    #    print(" --> Agora restam ",n," peças no tabuleiro")       
    #return n

def usuario_escolhe_jogada(n,m):
        if (n >= m):
            resp = int(input("Quantas peças você vai retirar? "))
            while (resp > m):
                print ("Opss! Jogada invalida! Tente novamente!")
                resp = int(input("Quantas peças você vai retirar? "))
            
            print ("Você retirou ", resp, "peça(s)")
            n = n - resp
            print ("Agora restam ",n," peças no tabuleiro!")
        elif (n < m):
            resp = int(input("Quantas peças você vai retirar? "))
            while (resp > n):
                print ("Opss! Jogada invalida! Tente novamente!")
                resp = int(input("Quantas peças você vai retirar? "))
            print ("Você retirou ", resp, "peça(s)")
            n = n - resp
            print ("Agora restam ",n," peças no tabuleiro!")
        
        if n == 0:
            print ("Você venceu!")
        
        return n

def partida():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = int(input("Escolha: "))

    if escolha == 1:
        n = int(input("Quantas peças?  "))
        m = int(input("Limite de peças por jogada?  "))

        while n <= m:
            print("Valores inválidos!")
            n = int(input("Quantas peças?  "))
            m = int(input("Limite de peças por jogada?  "))
        else:
            if n%(m+1) == 0:
                print("VOCÊ começa!")
                resp_user = usuario_escolhe_jogada(n,m)
                resp_comp = computador_escolhe_jogada(resp_user,m)

                if resp_comp != 0:
                    while (resp_user > 1) or (resp_comp > 1):
                        resp_user = usuario_escolhe_jogada(resp_comp,m)
                        if resp_user > 0:
                            resp_comp = computador_escolhe_jogada(resp_user,m)
            else:
                print("Computador começa!")
                resp_comp = computador_escolhe_jogada(n,m)
                resp_user = usuario_escolhe_jogada(resp_comp,m)
                
                if resp_user != 0:
                    while (resp_user > 1) or (resp_comp > 1):
                        resp_comp = computador_escolhe_jogada(resp_user,m)
                        if resp_comp > 0:
                            resp_user = usuario_escolhe_jogada(resp_comp,m)
    
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

            if n%(m+1) == 0:
                print("Você começa!")
                resp_user = usuario_escolhe_jogada(n,m)
                resp_comp = computador_escolhe_jogada(resp_user,m)

                if resp_comp == 0:
                    placar_comp = placar_comp + 1
                else:    
                    while (resp_user > 1) or (resp_comp > 1):
                        resp_user = usuario_escolhe_jogada(resp_comp,m)
                    
                        if resp_user == 0:
                            placar_user = placar_user + 1
                        else:
                            resp_comp = computador_escolhe_jogada(resp_user,m)
                    
                        if resp_comp == 0:
                            placar_comp = placar_comp + 1
            else:
                print("Computador começa!")
                resp_comp = computador_escolhe_jogada(n,m)
                resp_user = usuario_escolhe_jogada(resp_comp,m)

                if resp_user == 0:
                    placar_user = placar_user + 1
                else:
                    while (resp_user > 1) or (resp_comp > 1):
                        resp_comp = computador_escolhe_jogada(resp_user,m)

                        if resp_comp == 0:
                            placar_comp = placar_comp + 1
                        else:
                            resp_user = usuario_escolhe_jogada(resp_comp,m)
                        
                        if resp_user == 0:
                            placar_user = placar_user + 1
            # ------
            i = i + 1
        print ("Final do Campeonato!")
        print ("Placar: Computador ", placar_comp," x ",placar_user, " VOCÊ")
    else:
        print("***** Escolha 1 ou 2 *****")
        partida()
partida()