def start():
    print("Bem Vindo á MASMORRA DA MORTE")
    print("\nComo the chamas?")
    nome = input(">")
    print("Bem vindo, ", nome)
    print("Na tua frente tens uns portões ferruguentos que aparentam ter centenas de anos desde que foram abertos")
    print("que misterios, lendas, monstros e tesouros se escondem lá dentro")
    print("Tens coragem de abrir? (sim/não)")
    resposta = input(">")
    
    if "s" in resposta:
        entrada_principal()
    else:
        game_over("Nunca saberás que riquezas se escondem dentro desta masmorra!!")
        
        
def entrada_principal():
    print("\nAbriste com esforço os portões ferrugentos.")
    print("Observas com horror")

    
    
start()