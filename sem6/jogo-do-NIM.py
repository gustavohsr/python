def computador_escolhe_jogada(n,m):
        n = n - m
        
        if (m == 0):
            print("Computador tirou uma peça!")
            print("Fim de jogo! O computador ganhou!")
            n = 0
        elif (n == 0):
             print("Computador tirou ",m," peça!")    
             print("Fim de jogo! O computador ganhou!")
        else:
            print("Agora restam ",n," peças no tabuleiro")       
    
        return n

def usuario_escolhe_jogada(n,m):
        if (n != 0):
            resp = int(input("1 - Quantas peças você vai retirar? "))
            while (resp >= n):
                print ("Opss! Jogada invalida! Tente novamente!")
                resp = int(input("Quantas peças você vai retirar? "))
            
            print ("Você retirou ", resp, "peças")
            n = n - resp
            print ("Agora restam ",n," peças no tabuleiro")
    
        return n

def partida():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = int(input("Escolha: "))

    if escolha == 1:
        n = int(input("Quantas peças? Informe o valor de n: "))
        m = int(input("Limite de peças por jogada? Informe o valor de m: "))

        if ((m+1)*2) >= n:
            print("Você começa!")
            resp_user = usuario_escolhe_jogada(n,m)
            resp_comp = computador_escolhe_jogada(resp_user,resp_user-1)
            while (resp_user > 1) or (resp_comp > 0):
                resp_user = usuario_escolhe_jogada(resp_comp,resp_comp-1)
                resp_comp = computador_escolhe_jogada(resp_user,resp_user-1)
        else:
            print("Computador começa!")
            resp_comp = computador_escolhe_jogada(n,m)
            resp_user = usuario_escolhe_jogada(resp_comp,resp_comp-1)
            while (resp_user > 1) or (resp_comp > 0):
                resp_comp = computador_escolhe_jogada(resp_user,resp_user-1)
                resp_user = usuario_escolhe_jogada(resp_comp,resp_comp-1)
        print("Final")
    
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        i = 1
        while (i <= 3):
            print("**** Rodada ",i," ****")
            # ------
            n = int(input("Quantas peças? Informe o valor de n: "))
            m = int(input("Limite de peças por jogada? Informe o valor de m: "))

        if ((m+1)*2) >= n:
            print("Você começa!")
            resp_user = usuario_escolhe_jogada(n,m)
            resp_comp = computador_escolhe_jogada(resp_user,resp_user-1)
            while (resp_user > 1) or (resp_comp > 0):
                resp_user = usuario_escolhe_jogada(resp_comp,resp_comp-1)
                resp_comp = computador_escolhe_jogada(resp_user,resp_user-1)
        else:
            print("Computador começa!")
            resp_comp = computador_escolhe_jogada(n,m)
            resp_user = usuario_escolhe_jogada(resp_comp,resp_comp-1)
            while (resp_user > 1) or (resp_comp > 0):
                resp_comp = computador_escolhe_jogada(resp_user,resp_user-1)
                resp_user = usuario_escolhe_jogada(resp_comp,resp_comp-1)
            # ------
        i = i + 1
        print ("Final do Campeonato!")
    else:
        print("Escolha 1 ou 2")


partida()