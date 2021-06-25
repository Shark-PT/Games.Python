import random


inventario = []


def intro():
    
    while True:
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
    while True:
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
            
                
            
def sala_ogre():
    print("\nEntraste numa sala escura e fedorenta.") 
    print("Olhas com atenção e vês um ogre num canto a dormir.")
    print("1)Queres lutar com o Ogre ")     
    print("2)Queres passar pelo Ogre sem o acordar?")
    resposta = input(">")
    
    if resposta == "1":
        print("***--- Estás numa luta contra um ogre.")
        print(" Tu vais?: ---***")
        print("***--- A: Ver o inventario ")
        print("***--- B: Dar-lhe um soco? Sucesso: 85%")
        print("***--- C: Dar-lhe um pontapé? Sucesso: 33%")
        print("***--- D: Usar uma arma do inventario? Sucesso: 95%")
        decision= input("O que vais escolher: A,B,C?")
        
        minPoint=1
        maxPoint=100
        
        ChB = (random.randint(minPoint, maxPoint))*.85
        ChC = (random.randint(minPoint, maxPoint))*.33
        ChD = (random.randint(minPoint, maxPoint))*.95
    
        while "a" in decision.lower():
            for x in inventario:
                print(x)
                print("***--- B: Dar-lhe um soco? Sucesso: 85%")
                print("***--- C: Dar-lhe um pontapé? Sucesso: 33%")
                print("***--- D: Usar uma arma do inventario? Sucesso: 95%")
                decision= input("O que vais escolher: A,B,C?") 
    
        if decision.upper() == "B" and ChB > 25:
            print("Tu decidiste dar-lhe um soco")
            print("Ele aterrou no chão")
            sala3()
            return 1
            
        elif decision.upper() == "C" and ChC > 25:
            print("Tu decidiste dar-lhe um pontapé")
            print("Ele aterrou no chão")
            sala3()
            return 1
            
        elif decision.upper() == "D" and ChD > 25 and "adaga" in inventario:
            print("Tu usaste a Adaga")
            print("Deste-lhe uma enorme coça")
            sala3()
            return 1
            
        else:
            game_over("morreste")
            
    
        
def sala3():
    print("")
    
    
""""
def monstro(monstro):
    print("***--- Estás numa luta contra um " + monstro)
    print(". Tu vais?: ---***")
    print("***--- A: Ver o inventario ")
    print("***--- B: Dar-lhe um soco? Sucesso: 85%")
    print("***--- C: Dar-lhe um pontapé? Sucesso: 33%")
    print("***--- D: Usar uma arma do inventario? Sucesso: 95%")
    decision= input("O que vais escolher: A,B,C?")
        
    minPoint=1
    maxPoint=100
        
    ChB = (random.randint(minPoint, maxPoint))*.85
    ChC = (random.randint(minPoint, maxPoint))*.33
    ChD = (random.randint(minPoint, maxPoint))*.95
    
    if "a" in decision.lower():
                for x in inventario:
                    print(x) 
    
    if decision.upper() == "B" and ChB > 25:
        print("Tu decidiste dar-lhe um soco")
        print("Ele aterrou no chão")
        return 1
            
    elif decision.upper() == "C" and ChC > 25:
        print("Tu decidiste dar-lhe um pontapé")
        print("Ele aterrou no chão")
        return 1
            
    elif decision.upper() == "D" and ChD > 25 and "adaga" in inventario:
        print("Tu usaste a Adaga")
        print("Deste-lhe uma enorme coça")
        return 1
            
    else:
        game_over("morreste")
        """
        
        
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