import random
inventario = ["adaga"]

def monstro(monstro, local):
    print("***--- Estás numa luta contra um " + monstro)
    print(". Tu vais?: ---***")
    print("***--- A: Ver o inventario ")
    print("***--- B: Dar-lhe um soco? Sucesso: 85%")
    print("***--- C: Dar-lhe um pontapé? Sucesso: 33%")
    print("***--- D: Usar uma arma do inventario? Sucesso: 95%")
    decision= input("O que vais escolher: A,B,C ou D?")
        
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
        ir_para("local")
        return 1
            
    elif decision.upper() == "C" and ChC > 25:
        print("Tu decidiste dar-lhe um pontapé")
        print("Ele aterrou no chão")
        ir_para("local")
        return 1
            
    elif decision.upper() == "D" and ChD > 25 and "adaga" in inventario:
        print("Tu usaste a Adaga")
        print("Deste-lhe uma enorme coça")
        ir_para("local")
        
        return 1
            
    else:
        game_over("morreste")
        
        
def ir_para(local):
    if (local == "sala3"):
        sala3()
        
        
def sala3():
    print("Ipsum ipsum continuar")
    
            
def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()
    
def play_again():
    print("\nQueres jogar novamente? (sim/não)")
    
    resposta = input(">").lower()
    
    if "s" in resposta:
        monstro("ogre", "sala3")
    
    else:
        print("ADEUS")
        exit()
    
monstro("ogre", "sala3")