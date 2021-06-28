import random
from main import *
from salas import *


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