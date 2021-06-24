import random


inventario = []


def intro():
    
    print = ("Apusm loki, bla bla bla")
    print("TODO/TODO/TODO")
    

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
        return 1
            
    elif decision.upper() == "B" and ChB > 25:
        print("Tu decidiste dar-lhe um pontapé")
        print("Ele aterrou no chão")
        return 1
            
    elif decision.upper() == "C" and ChC > 25 and "Soqueira" in inventario:
        print("Tu usaste a Adaga")
        print("Deste-lhe uma enorme coça")
        return 1
            
    else:
        game_over("morreste")
        
        
def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()
    
def play_again():
    print("\nQueres jogar novamente? (sim/não)")
    
    resposta = input(">").lower()
    
    if "s" in resposta:
        start()
    
    else:
        exit()