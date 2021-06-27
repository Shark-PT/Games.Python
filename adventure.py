#Inicio do jogo
def start():
    print("\nYou are standing in a dark room.")
    print("There is a door to your left and right, wich one do you choose?")
    
    answer = input(">").lower()
    
    if "l" in answer:
        bear_room()
        
    elif "r" in answer:
        monster_room()
        
    else:
        game_over("Don't you know how to type something properly")
        
#Bear Room
def bear_room():
    print("\nThere is a bear here.")
    print("Behind the bear is another door.")
    print("The bear is eating nasty honey!")
    print("What would do? (1 or 2)")
    print("1). take the honey.")
    print("2). Taunt the bear.")
    
    answer = input(">")
    
    if answer == "1":
        game_over("The bear killed you.")
        
    elif answer == "2":
        print("\nYour good time, the bear moved from the door. You can proceed to the door.")
        diamond_room()
        
    else:
        game_over("Don't you know how to type a number?")
        
#monster room
def monster_room():
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.1nBehind the monster is another door.\nWhat would do? (1 or 2)")
    print("1=. Go through the door silentrly.")
    print("2). Kill the monster and show your courage.")
    
    answer = input(">")
    
    if answer == "1":
        diamond_room()
    
    elif answer == "2":
        game_over("The monster was hungry, he/it ate you.")
        
    else:
        game_over("Go and learn how to type a number.")
        
#diamond_room
def diamond_room():
    print("\nYou are in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you doo?(1 or 2)")
    print("1). Take some diamonds and go throught the door.")
    print("2). Just go through the door.")
    
    answer = input(">")
    
    if answer == "1":
        game_over("They were cursed diamonds! The moment you touched them, your heart stopped beating")
        
    elif answer == "2":
        print("\nNice, you are an honest man! Congrats, you win the game")
        play_again
        
    else:
        game_over("Learn to type a number.")
        
    
#Game_over
def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()
    
    
#play_again
def play_again():
    print("Do you want to play again? (y or n)")
    
    answer = input(">").lower()
    
    if "y" in answer:
        start()
    
    else:
        exit()
        
        
start()
