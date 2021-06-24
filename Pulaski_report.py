def game():
    import random
    decide = ["direita", "esquerda"]
    aproach = ["s","n"]
    resposta = input("Queres jogar o jogo? (s/n)")
                  
    if resposta.lower() == 's':
        print("Bem-vindo ao cataclismo")
        start=True
        inventory=[]
            
    else:
        print("Ok, fica para a proxima")


    if start ==True:
        print("Estranho: Olá viajante, vejo que és novo nesta cidade.")
        print("Estranho: Bem-vindo, aqui é Pulaski. Mão encontrarás outra cidade no mundo mais interessada em proporcionar hospitalidade")
        print("Estranho: De momento, o importante é manter-te vivo, vejo que só tens 20HP. Não temas, isto irá ajudar na tua viagem.")
        choice=input("Queres a minha ajuda?(s/n)")
        
    if choice.lower() == "s":
        choiceY1 = True
        print("Ainda bem que aceitas miudo")
        print("###--- Recebeste uma soqueira ---###")
        print("Vamos lá então, vamos por-te a conhecer as ruas")
        inventory.append("Soqueira")
        
    else:
        choiceY1=False
        print("Tu é que sabes rapaz. Toma, fica com este mapa da cidade, no caso de te perderes, pelo menos")
        print("Bem, parece que isto é o adeus")
        print("###--- Recebeste um mapa ---###")
        inventory.append("Mapa")
        
        
    if choiceY1==False and "Mapa" in inventory:
        print("Verificas o mapa e vês que tens que ir para a esquerda")
        decide=input("vais para a direita ou esquerda?(direita/esquerda)") 
        
    elif choiceY1==True:
        print("Vamos lá rapaz, segue-me até ao parque. Há uma coisa importante para te mostrar lá e que te irá ajudar na tua viagem.")
        print("Oh, aguenta, está ali o Danger Dan. Ele gosta de lutar com pessoas com a mente e tu devias treinar com ele.")
        aproach=input("Tu aproximas-te do Danger Dan?(s/n)")
    
    if decide == "direita":
        print("Tu tiveste um acidente de carro e morreste")
        print("GAME OVER")   
        
    elif decide == "esquerda":
        aproach1=input("Tu estas no parque e alguem quer lutar contigo. Vais lutar?(s/n")
        
    
    
        
    if aproach1.lower() == "s":
        print("***--- Estás numa luta. Tu vais?: ---***")
        print("***--- A: Dar-lhe um soco? Sucesso: 66%")
        print("***--- B: Dar-lhe um pontapé? Sucesso: 33%")
        print("***--- Usar a Soqueira? Sucesso: 88%")
        decision= input("O que vais escolher: A,B,C?")
        
        minPoint=1
        maxPoint=100
        
        ChA = (random.randint(minPoint, maxPoint))*.66
        ChB = (random.randint(minPoint, maxPoint))*.33
        ChC = (random.randint(minPoint, maxPoint))*.88
        
        if decision.upper() == "A" and ChA > 25:
            print("Tu decidiste dar-lhe um soco")
            print("Ele aterrou no chão")
            print("Revistas-lo e encontras uma navalha")
            inventory.append("navalha")
            
        elif decision.upper() == "B" and ChB > 25:
            print("Tu decidiste dar-lhe um pontapé")
            print("Ele aterrou no chão")
            print("Revistas-lo e encontras uma navalha")
            inventory.append("navalha")
            
        elif decision.upper() == "C" and ChC > 25 and "Soqueira" in inventory:
            print("Tu usaste a Soqueira")
            print("Deste-lhe uma enorme coça")
            print("Revistas-lo e encontras uma navalha")
            inventory.append("navalha")
            
        else:
            print("Não conseguiste acertar e perdeste a luta")
            print("Game Over")
         
    if aproach =="n":
        print("És um cobarde.")
        print("game over")    
    
    if aproach == "s":
        print("***--- Estás numa luta. Tu vais?: ---***")
        print("***--- A: Dar-lhe um soco? Sucesso: 85%")
        print("***--- B: Dar-lhe um pontapé? Sucesso: 33%")
        print("***--- Usar a Soqueira? Sucesso: 95%")
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
            
        elif decision.upper() == "C" and ChC > 25 and "Soqueira" in inventory:
            print("Tu usaste a Soqueira")
            print("Deste-lhe uma enorme coça")
            
        else:
            print("Não conseguiste acertar e perdeste a luta")
            print("Game Over")
    
    
def predio():
    print("entras num predio abandonado")
    #TODO
        
game()