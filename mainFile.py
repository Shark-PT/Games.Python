import random


codeSegment1 = random.randint(0,9)
codeSegment2 = random.randint(0,9)
codeSegment3 = random.randint(0,9)
code = int(str(codeSegment1) + str(codeSegment2) + str(codeSegment3))
items = ["Door", "window", "Backpack", "Vase", "Bucket", "Painting", "JewelryBox", "Rug", "Mirror", "Bookshelf"]
code1Location = random.randint(1,3)
code2Location = random.randint(4,6)
code3Location = random.randint(7,9)

def intro():
    print("Last night, you went to sleep in your own home.")
    print("Now, you wake up to an unfamiliar environment.")
    print("As your eyes flutter open, darkness greets you, Your sourrondings are blid to you.")
    print("You sat on a bed, and a wall hugs your back. Beside you is a table, whose outline you can vaguely determine.")
    
    print("1 - to check under the bed")
    print("2 - to check the table")
    
    while True:
        bedOrWall = input()
        
        try:
            if int(bedOrWall) == 1:
                print("Under the bed, you feel a note. But you cannot see to examine it.")
                print("You check the table and find a lamp. With a loud click, your surroundings are illuminated.")
                break
            elif int(bedOrWall) == 2:
                print("You check the table and find a lamp. With a loud click, your surroundings are illuminated.") 
                break
            else:
                print("Enter either 1 or 2:")
            
        except:
            print("Value must be whole number 1 or 2:")
    print("\n")
    print("The note reads:")
    print("My dearest participant,")
    print(" if you notice, the door contains a padlock with a three digit code.")
    print(" Youwill find this code within the room, and must solve it. You shall find three numbers, and must order them correctly.")
    print(" I wish you the best of luck.")
    print("Sincerely, your gracious host.")
    
    print("\n")
    print("You examine the room and see:")     
    
def menu(list, question):
        for item in list:
            print(list.index(item), item)
        
        while True:
            result = input(question)
            try:
                result = int(result)
                break
        
            except:
                print("selection must be whole number between 0-9:")
            
        return result


def Door(code):
    print("You walk top the door. The rotary padlock contains three digits. You enter a code")
    
    while True:
        try:
            option1 = int(input("Digit one: "))
            break
        
        except:
            print("Digit one must be a whole number betwee 0-9: ")
            
    while True:
        try:
            option2 = int(input("Digit two: "))
            break
        
        except: 
            print("Digit two must be a whole number between 0-9: ")
            
    while True:
        try:
            option3 = int(input("Digit three: "))
            break
        
        except:
            print("Digit three must be a whole number between 0-9: ")
            
    chosenCode = int(str(option1)+ str(option2) + str(option3))
    print("")
    if chosenCode == code:
        print("You hear a click, and the padlock shifts. As you press open the door a rush of fresh, warm air caresses your face. At last, you are free.")
        return(1)
    
    else:
        print("You jigle the padlock, but no avail. The code is incorrect.")
        return(0)
    
    
def Window(choice, codeLocation, codeValue):
    print("")
    print("You look at the windows. It's dark, and damp. Mold grows along the edges and you cannot see through its musty panes.")
    if choice == codeLocation:
        print("Carved into the edging, you see the number " +str(codeValue) + ".")
        print("")
    
    else:
        print("You find no code.")
        print("")          


def Backpack(choice, codeLocation, codeValue):
    print("")
    print("The backpack is your personnel bag. Strange, you though you lost it weeks ago.")
    if choice == codeLocation:
        print("Within the front pocket, you see the number " +str(codeValue) + "written on a crumpled note.")
        print("")
        
    else:
        print("You find no code.")
        print("")
        
        
def Vase(choice, codeLocation, codeValue):
    print("")
    print("A dark blue vase holds roses that seems to have died long ago.")
    if choice == codeLocation:
        print("On the base, you see the number " +str(codeValue) + ".")
        print("")
        
    else:
        print("You find no code.")
        print("")
        
        
def Bucket(choice, codeLocation, codeValue):
    print("")
    print("The bucket sits in the middsle of the floor. It catches a gentle leak from the dank ceiling")
    if choice == codeLocation:
        print("Within, you see exactly " +str(codeValue) + ".")
        print("")
        
    else:
        print("You find no code.")
        print("")
        
        
def Painting(choice, codeLocation, codeValue):
    print("")
    print("Has Mona lisa allways been this creepy? Her eyes peer into you, her smile gleams as if she knows the fate that awaits you unless you find the code.")
    if choice == codeLocation:
        print("Painted in the corner, you see the number " +str(codeValue) + ".")
        print("")
        
    else:
        print("You find no code.")
        print("")
        
        
def JewelryBox(choice, codeLocation, codeValue):
    print("")
    print("The oak Jewelry Box creeks open and gentle music fills the room. The music may have once been soothing, but years of age has ruined this once peaceful melody")
    if choice == codeLocation:
        print("Etched inside the lid, you see the number  " +str(codeValue) + ".")
        print("")
        
    else:
        print("You find no code.")
        print("")
        
        
def Rug(choice, codeLocation, codeValue):
    print("")
    print("A dusty woven rug adorns the otherwise ragged wooden floor, adding a hint of color to the eery room")
    if choice == codeLocation:
        print("Etched inside the lid, you see the number  " +str(codeValue) + ".")
        print("")
        
    else:
        print("You find no code.")
        print("")
        
        
def Mirror(choice, codeLocation, codeValue):
    print("")
    print("The mirror is grimey and unpleasent. The unnatural reflection leers back at you. The circlesunder your eyes are dark and full. It offers little comfort")
    if choice == codeLocation:
        print("As you study your reflection, you notice the number " +str(codeValue) + "painted onto your shirt.")
        print("")
        
    else:
        print("You find no code.")
        print("")
  
  
def Bookshelf(choice, codeLocation, codeValue):
    print("")
    print("The mirror is grimey and unpleseant. The unnatural reflection leers back at you. The circles under your eyes are dark and full. It offers little comfort.")
    if choice == codeLocation:
        print("As you study your reflection, you notice the number " + str(codeValue) + " painted onto your shirt.")
        print("")
    
    else:
        print("You find no code.")
        print("")
        
        
intro()       
result = 0
while True:
    choice = menu(items, "What do you want to inspect? ")

    if choice == 1:
	    Window(choice, code1Location, codeSegment1)
    elif choice == 2:
    	Backpack(choice, code1Location, codeSegment1)
    elif choice == 3:
    	Vase(choice, code1Location, codeSegment1)
    elif choice == 4:
	    Bucket(choice, code2Location, codeSegment2)
    elif choice == 5:
	    Painting(choice, code2Location, codeSegment2)
    elif choice == 6:
	    JewelryBox(choice, code2Location, codeSegment2)
    elif choice == 7:
	    Rug(choice, code3Location, codeSegment3)
    elif choice == 8:
	    Mirror(choice, code3Location, codeSegment3)
    elif choice == 9:
	    Bookshelf(choice, code3Location, codeSegment3)
    else:
	    result = Door(code)
    if result == 1:
	    break     