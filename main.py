import random
from funcao_luta import monstro


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
        monstro("Ogre","sala3")
    
    else:
        sortemin = 1
        sortemax = 100
        hipotese = (random.randint(sortemin, sortemax))*.75
        
        if hipotese > 60:
            print("\nTu conseguiste passar pelo ogre a dormir")
            ir_para("sala3")
            
        elif hipotese > 25 and hipotese < 60:
            print("\nEle acordou e vais ter que lutar com ele")
            monstro("Ogre", "sala3")
            
        else:
            game_over("\nO Ogre acordou e atacou-te pelas costas. Nunca tiveste hipotese")
        
def sala3():
    print("\nConseguiste ultrapassar o Ogre e passaste para uma sala nova.")
    print("Olhas para o chão e vês moedas de ouro espalhadas")
    print("Achas estranho, mas vais querer apanha-las?(sim/não)")
    resposta = input(">")
    
    if "s" in resposta.lower():
        print("Apanhaste as moedas do chão e ficaste com 5 moedas de ouro.")
        print("Olhas em frente e vês que tem dois caminhos.")
        print("Vais querer ir para a esquerda ou direita? (Esquerda/direita")
        inventario.append("Moedas de Ouro")
        caminho = input(">")
        
        
    else:
        print("Ignoras as moedas e olhas em frente e vês que tem dois caminhos.")
        print("Vais querer ir para a esquerda ou direita? (Esquerda/direita")
        caminho = input(">")
        
    if "d" in caminho:
        sala4()
        
    else:
        sala5()
            
def monstro(monstro, local):
    print("***--- Estás numa luta contra um " + monstro)
    print(". Tu vais?: ---***")
    print("***--- A: Ver o inventario ")
    print("***--- B: Dar-lhe um soco? Sucesso: 85%")
    print("***--- C: Dar-lhe um pontapé? Sucesso: 75%")
    print("***--- D: Usar uma arma do inventario? Sucesso: 95%")
    decision= input("O que vais escolher: A,B,C ou D?")
        
    minPoint=1
    maxPoint=100
        
    ChB = (random.randint(minPoint, maxPoint))*.85
    ChC = (random.randint(minPoint, maxPoint))*.75
    ChD = (random.randint(minPoint, maxPoint))*.95
    
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
        



def sala3():
    print("\nConseguiste ultrapassar o Ogre e passaste para uma sala nova.")
    print("Olhas para o chão e vês moedas de ouro espalhadas")
    print("Achas estranho, mas vais querer apanha-las?(sim/não)")
    resposta = input(">")
    
    if "s" in resposta.lower():
        print("Apanhaste as moedas do chão e ficaste com 5 moedas de ouro.")
        print("Olhas em frente e vês que tem dois caminhos.")
        print("Vais querer ir para a esquerda ou direita? (Esquerda/direita")
        inventario.append("Moedas de Ouro")
        caminho = input(">")
        
        
    else:
        print("Ignoras as moedas e olhas em frente e vês que tem dois caminhos.")
        print("Vais querer ir para a esquerda ou direita? (Esquerda/direita")
        caminho = input(">")
        
    if "d" in caminho.lower():
        sala4()
        
    else:
        sala5()
        
        
def sala4():
    print("Ipsum TODO")
    
def sala5():
    print("IPsum TODO")
        

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