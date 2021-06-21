import random

inventario = []
def start():
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
            print("\nOlhas pelo tunel sombrio e pensas no que te estás a meter")
            print("Após um periodo de habituação, vês um caminho àa tua direita")
            print("Queres ir pelo caminho da esquerda ou vais em frente?(frente/esquerda)")
            caminho = input(">")
    
        else:
            print("\nDecidiste ir pelo caminho da esquerda")
            print("")
    
        if "e" in caminho:
            monstro("ogre")
        
        else:
            print("\nO caminho está bolorento e escuro e imaginas os horrores que terão passado nestes caminhos")
            print("ves que o caminho vira à direita e continuas até chegar a uma intersecção.")
            print("Queres seguir em frente ou virar à esquerda?(Frente/Esquerda")
        


def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()


def play_again():
    print("Queres jogar novamente? (sim/não)")
    
    resposta = input(">").lower()
    
    if "s" in resposta:
        start()
    
    else:
        exit()
        
def monstro(monstro):
    print("***--- Estás numa luta contra um " + monstro)
    print(". Tu vais?: ---***")
    print("***--- A: Dar-lhe um soco? Sucesso: 85%")
    print("***--- B: Dar-lhe um pontapé? Sucesso: 33%")
    print("***--- Usar a Adaga? Sucesso: 95%")
    decision= input("O que vais escolher: A,B,C?")
        
    minPoint=1
    maxPoint=100
        
    ChA = (random.randint(minPoint, maxPoint))*.85
    ChB = (random.randint(minPoint, maxPoint))*.33
    ChC = (random.randint(minPoint, maxPoint))*.95
    
    if decision.upper() == "A" and ChA > 25:
        print("Tu decidiste dar-lhe um soco")
        print("Ele aterrou no chão")
            
    elif decision.upper() == "B" and ChB > 25:
        print("Tu decidiste dar-lhe um pontapé")
        print("Ele aterrou no chão")
            
    elif decision.upper() == "C" and ChC > 25 and "Soqueira" in inventario:
        print("Tu usaste a Adaga")
        print("Deste-lhe uma enorme coça")
            
    else:
        game_over("morreste")
            
start()