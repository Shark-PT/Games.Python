def game():
    import random
    decide = ["right", "left"]
    aproach = ["y","n"]
    resposta = input("Queres jogar o jogo? (y/n)")
                  
    if resposta.lower() == 'y':
        print("Benvindo ao cataclismo")
        start=True
        inventory=[]
            
    else:
        print("Ok, fica para a proxima")


    if start ==True:
        print("Estranho: Olá viajante, vejo que és novo nesta cidade.")
        print("Estranho: Bem-vindo, aqui é Pulaski. Mão encontrarás outra cidade no mundo mais interessada em proporcionar hospitalidade")
        print("Estranho: De momento, o importante é manter-te vivo, vejo que só tens 20HP. Não temas, isto irá ajudar na tua viagem.")
        choice=input("Queres a minha ajuda?(y/n)")
        
    if choice.lower() == "y":
        choiceY1 = True
        print("Ainda bem que aceitas miudo")
        print("###--- Recebeste uma soqueira ---###")
        print("Vamos lá então, vamos por-te a conhecer as ruas")
        inventory.append("Soqueira")
        
    else:
        choiceY1=False
        print("Cool ma, I hear ya. Here, ave this map of the city so if you get lost you have something to guide you at least")
        print("Well, this seems to be the end")
        print("###--- You have been given a Map ---###")
        inventory.append("Map")
        
        
    if choiceY1==False and "Map" in inventory:
        print("your map tells you to take a left")
        decide=input("do you take a left or right?") 
        
    elif choiceY1==True:
        print("Cmon man, follow me to the park. There is something important there to show you - it will help you on your journey ")
        print("Oh, hold up, that there is dange dan, he likes to fight people with his mind and you should fight him")
        aproach=input("do you apropach danger dan?(y/n)")
    
    if decide == "right":
        print("you got in a car accident and now you are dead")
        print("game over")   
        
    elif decide == "left":
        aproach1=input("You are at a park and someone wants to fight you, do you approach him?(y/n")
    
    
    """    para continuar
    if aproach1.lower() == "y":
        print("") 
     """    
    if aproach =="n":
        print("you are a coward")
        print("game over")    
    
    if aproach == "y":
        print("***--- You are in a fight. Will you: ---***")
        print("***--- A: punch him? Sucess: 85%")
        print("***--- B: Kick him? Sucess: 33%")
        print("***--- Use Brass Knucles? Sucess: 95%")
        decision= input("What will be your choice: A,B,C?")
        
        minPoint=1
        maxPoint=100
        
        ChA = (random.randint(minPoint, maxPoint))*.85
        ChB = (random.randint(minPoint, maxPoint))*.33
        ChC = (random.randint(minPoint, maxPoint))*.95
        
        if decision.upper() == "A" and ChA > 25:
            print("You decide to punch him")
            print("He his knocked out cold")
            
        elif decision.upper() == "B" and ChB > 25:
            print("You decide to kick him")
            print("He is knocked out cold")
            
        elif decision.upper() == "C" and ChC > 25 and "Brass Knuckles" in inventory:
            print("You use your Brass Knucles")
            print("You beat hm pretty bad")
            
        else:
            print("That didn't knot work, and you are knocked out cold")
            print("Game Over")
    
game()