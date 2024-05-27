# Sets the template
MADLIB = "If you give a {} a {}, they are going to ask for a {}. When you give them the {}, they will want to {}. \nWhen they've finished, they will {}. Then they will {} and {} to the {}. \nSince that doesn't work out, they will want to go to {}. On the way, they will see a {} and will want {}. Then you will have to take them to the {}. \nThey will {}. When they are done, they will ask you for some {}. On the way home they will start a game of {}. When you finally get home, you'll have to {}. \nThen they will want a {}. You'll have to find a {} and {}. When they see the {}, they will start {}. \nThen they will {} out of {}. Of course, when they are finished they will want to {}. So, they will ask for a {}, and chances are if you give them a {}, they are going to want a {}"

# Intro
print("""\
        ███▄ ▄███▓ ▄▄▄      ▓█████▄     ██▓     ██▓ ▄▄▄▄     ██████    
        ▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌   ▓██▒    ▓██▒▓█████▄ ▒██    ▒    
        ▓██    ▓██░▒██  ▀█▄  ░██   █▌   ▒██░    ▒██▒▒██▒ ▄██░ ▓██▄      
        ▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌   ▒██░    ░██░▒██░█▀    ▒   ██▒   
        ▒██▒   ░██▒ ▓█   ▓██▒░▒████▓    ░██████▒░██░░▓█  ▀█▓▒██████▒▒   
        ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▒░▓  ░░▓  ░▒▓███▀▒▒ ▒▓▒ ▒ ░   
        ░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒    ░ ░ ▒  ░ ▒ ░▒░▒   ░ ░ ░▒  ░ ░   
        ░      ░     ░   ▒    ░ ░  ░      ░ ░    ▒ ░ ░    ░ ░  ░  ░     
            ░         ░  ░   ░           ░  ░ ░   ░            ░     
                            ░                           ░             
        """)

print("welcome to Mad-libs")
animal = input("first, name an animal\n")
food1 = input("Name a food\n")
noun1 = input("Name a noun\n")
verb1 = input("Name a verb that doesn't end with -ing\n")
verb2 = input("Name another verb that doesn't end with -ing\n")
verb3 = input("Name another verb that doesn't end with -ing\n")
verb4 = input("Name another verb that doesn't end with -ing\n")
noun2 = input("Name a noun again\n")
location1 = input("Name a location\n")
noun3 = input("Name a noun again\n")
noun4 = input("Name a noun again\n")
location2 = input("Name another location\n")
verb5 = input("Name another verb that doesn't end with -ing \n")
food2 = input("Name another food\n")
game = input("Name a game\n")
verb6 = input("Name another verb that doesn't end with -ing\n")
noun5 = input("Name a noun again\n")
noun6 = input("Name a noun again\n")
noun7 = input("Name a plural noun\n")
noun8 = input("Name a noun again\n")
verb7 = input("Name a verb that DOES end with -ing\n")
verb8 = input("Name another verb that doesn't end with -ing\n")
noun9 = input("Name a plural noun\n")
verb9 = input("Name another verb that doesn't end with -ing\n")

# outputs final mad lib
madlib_output = print(MADLIB.format(animal, food1, noun1, noun8, verb1, verb2, verb3, verb4, noun2, location1, noun3, noun4, location2, verb5, food2, game, verb6, noun5, noun6, noun7, noun8, verb7, verb8, noun9, verb9, noun1, noun1, food1))