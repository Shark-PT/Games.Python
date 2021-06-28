import random


inventario = []


def intro():
    
    print(" Bem Vindo á MASMORRA DA MORTE")
    print("\nComo the chamas?")
    nome = input(">")
    print("Bem vindo, ", nome)
    print("\nNa tua frente tens uns portões ferruguentos que aparentam ter centenas de anos desde que foram abertos")
    print("que misterios, lendas, monstros e tesouros se escondem lá dentro")
    print("Tens coragem de abrir? (sim/não)")
    resposta = input(">")
    
    
    if "s" in resposta.lower():
        entrada_principal()
    else:
        game_over("Nunca saberás que riquezas se escondem dentro desta masmorra!!")
        
    
def entrada_principal():
    
        print("\nAbriste com esforço os portões ferrugentos.")
        print("Observas com horror, os restos de aventureiros tombados pelo chão")
        print("Queres revistar os corpos para ve se tem alguma coisa util?(sim/não)")
    
        resposta = input(">")
    
        if "s" in resposta.lower():
            print("\nencontras uma adaga antiga e decides guarda-la")
            inventario.append("adaga")
            print("Continuas a vasculhar a entrada e vês dois caminhos")
            print("Vais para a direita ou esquerda?(direita/esquerda)")
            cruzamento = input(">")
        
        else:
            print("\nContinuas a vasculhar a entrada e vês dois caminhos")
            print("Vais para a direita ou esquerda?(direita/esquerda)")
            cruzamento = input(">")
            
        
        if "d" in cruzamento:
            sala_ogre()
            
        elif "e" in cruzamento:
            print("CONTINUA")
            
            
                
            
def sala_ogre():
    print("\nEntraste numa sala escura e fedorenta.") 
    print("Olhas com atenção e vês um ogre num canto a dormir.")
    print("1)Queres lutar com o Ogre ")     
    print("2)Queres passar pelo Ogre sem o acordar?")
    resposta = input(">")
    
    if resposta == "1":
        monstro("Ogre","sala3", 60, 75, 90)
    
    elif resposta == "2":
        sorte(60)
        valor = sorte(60)
        if valor > 60:
            print("\nTu conseguiste passar pelo ogre a dormir")
            ir_para("sala3")
            
        elif valor > 25 and sorte < 60:
            print("\nEle acordou e vais ter que lutar com ele")
            monstro("Ogre", "sala3", 60, 75, 90)
            
        else:
            game_over("\nO Ogre acordou e atacou-te pelas costas. Nunca tiveste hipotese")
    else:
        print("Opção errada, escolha uma das opções disponiveis")
    
        
def sala3():
    print("\nConseguiste ultrapassar o Ogre e passaste para uma sala nova.")
    print("Olhas para o chão e vês moedas de ouro espalhadas")
    print("Achas estranho, mas vais querer apanha-las?(sim/não)")
    resposta = input(">")
    
    if "s" in resposta.lower():
        print("\nApanhaste as moedas do chão e ficaste com 5 moedas de ouro.")
        print("inspecionas melhor a sala e vês que tem dois caminhos.")
        print("Vais querer ir para a esquerda ou direita? (Esquerda/direita)")
        inventario.append("Moedas de Ouro")
        caminho = input(">")
        
        
    else:
        print("\nIgnoras as moedas e olhas em frente e vês que tem dois caminhos.")
        print("Vais querer ir para a esquerda ou direita? (Esquerda/direita")
        caminho = input(">")
        
    if "d" in caminho:
        sala4()
        
    else:
        sala5()
            
 
def sala3():
    print("\nConseguiste ultrapassar o Ogre e passaste para uma sala nova.")
    print("Olhas para o chão e vês moedas de ouro espalhadas")
    print("Achas estranho, mas vais querer apanha-las?(sim/não)")
    resposta = input(">")
    
    if "s" in resposta.lower():
        print("\nApanhaste as moedas do chão e ficaste com 5 moedas de ouro.")
        print("Olhas em frente e vês que tem dois caminhos.")
        print("Vais querer ir para a esquerda ou direita? (Esquerda/direita")
        inventario.append("Moedas de Ouro")
        caminho = input(">")
        
        
    else:
        print("\nIgnoras as moedas e olhas em frente e vês que tem dois caminhos.")
        print("Vais querer ir para a esquerda ou direita? (Esquerda/direita")
        caminho = input(">")
        
    if "d" in caminho.lower():
        sala4()
        
    else:
        sala5()
        
        
def sala4():
    print("\nEntras numa sala iluminada com tochas e pensas o que haverá nesta sala")
    print("olhas para o chão e vês que algumas pedras são mais escuras e que há uma porta no fim.")
    print("tentas atravessar a sala pisando as pedras escuras ou claras?")
    pedras = input("\n>")
    
    if "esc" in pedras.lower:
        sorte(50)
        valor = sorte(50)
        if valor > 30:
            print("\nConseguiste passar a sala e passas a porta")
            sala6()
            
        else:
            game_over("\nO Chão cedeu e tu cais num abismo sem fundo.")
            
    
def sala5():
    print("\nOlhas para a sala e sentes-la perfumada")
    print("Achas isso muito estranho e fora do contexto, mas ignoras.")
    print("De cada lado da sala tens duas portas. Para qual vais?")
    print("Esquerda/Direita?)")
    portas = input(">")
    if "d" in portas.lower():
        print("\nentras numa sala nova")
        sala8()
            
            
    else:
        sala7()


def sala6():
    print("continua")
    
def sala7():
    print("Continua")
    
def sala8():
    print("\nEntraste no que parece ser um mini coliseu subterraneo")
    print("Tens um Urso a mostrar-te os dentes e vais ter que lutar contra ele")
    monstro("Urso","sala9", "10", "50", "80")
    
def sala9():
    print("contnua")    
    
def monstro(monstro, local, prob1, prob2, prob3):
    print("***--- Estás numa luta contra um " + monstro)
    print(". Tu vais?: ---***")
    print("***--- A: Ver o inventario ")
    print("***--- B: Dar-lhe um soco? Sucesso:  {xpto}  %".format(xpto = prob1))
    print("***--- C: Dar-lhe um pontapé? Sucesso:  {foo}  %".format(foo = prob2))
    print("***--- D: Usar uma arma do inventario? Sucesso:   {boo} %".format(boo = prob3))
    decision= input("O que vais escolher: A,B,C ou D?")
        
    minPoint=1
    maxPoint=100
    """
    p1 = int(prob1)
    p2 = int(prob2)
    p3 = int(prob3)
    """    
    ChB = (random.randint(minPoint, maxPoint))*prob1
    ChC = (random.randint(minPoint, maxPoint))*prob2
    ChD = (random.randint(minPoint, maxPoint))*prob3
    
    if "a" in decision.lower():
                for x in inventario:
                    print(x) 
    
    if decision.upper() == "B" and ChB > 25:
        print("\nTu decidiste dar-lhe um soco")
        print("Ele aterrou no chão")
        ir_para(local)
        
            
    elif decision.upper() == "C" and ChC > 25:
        print("\nTu decidiste dar-lhe um pontapé")
        print("Ele aterrou no chão")
        ir_para(local)
        
            
    elif decision.upper() == "D" and ChD > 25 and "adaga" in inventario:
        print("\nTu usaste a Adaga")
        print("Deste-lhe uma enorme coça")
        ir_para(local)
        
            
    else:
        game_over("morreste")
        
        
def ir_para(local):
    if (local == "sala3"):
        sala3()
    elif (local == "sala9"):
        sala9()


def sorte(valor):
    sortemin = 1
    sortemax = 100
    resultado = (random.randint(sortemin, sortemax))*valor
    return resultado
     




def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()
    
def play_again():
    print("\nQueres jogar novamente? (sim/não)")
    
    resposta = input(">").lower()
    
    if "s" in resposta:
        intro()
    
    else:
        print("ADEUS")
        exit()
        
        
        
intro()