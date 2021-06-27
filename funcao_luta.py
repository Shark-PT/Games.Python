import random

def monstro(monstro, local, prob1, prob2, prob3):
    print("***--- Estás numa luta contra um " + monstro)
    print(". Tu vais?: ---***")
    print("***--- A: Ver o inventario ")
    print("***--- B: Dar-lhe um soco? Sucesso:" + prob1 + "%")
    print("***--- C: Dar-lhe um pontapé? Sucesso:" + prob2 + "%")
    print("***--- D: Usar uma arma do inventario? Sucesso: " + prob3 +"%")
    decision= input("O que vais escolher: A,B,C ou D?")
        
    minPoint=1
    maxPoint=100
        
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
        


