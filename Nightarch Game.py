def adventure_game(playername):
    print("Welcome " + playername + " To the adventure game.")
    print("\nYou are in the City of Nightarch, you work for the Urchins Syndicate and you were hired to rob a rich mans home. You went through the sewers to get into a manhole into the Dawnpoint District. \n As you climb from the manhole, the dusk of night cloaks your entry to the streets. The District has a nightly patrol for anyone out as this is a private District for the Rich. The home in question being robbed is a Blue two story house with the home number of 393 on this current street. \n I have two pathes. \n Up the street. \n Or down the street. ")
    one = input("type 'up' to go up.\n type 'down' to go down.")
    if one == 'up':
        bluehouse = input("You go up the street, You find A blue house with the number 393 (that was easy... hopefully not too easy.) and looks like no lights are on. you notice three points of entry. You could knock on the door(type 'knock knock'), Climb a tree to a window(type 'tree'), Or go around to the back for more options(type 'backway')")
        if bluehouse == 'knock knock':
            print('You knock on the door, seconds later a set of lights above turn on. (hopefully this isnt a dumb idea). 30 seconds pass, you  can ')

        if bluehouse == 'tree':
            print('end')

        if bluehouse =='backway':
            print('end')

    if one == 'down':
        trashcan = input("You go down the street. You hear racket to your left behind a fence post of a home. should you investigate?\n 'investigate' for yes.\n 'too risky'for no")
        if trashcan == 'investigate':
            input('end')
        if trashcan == 'too risky':
            input('end')
        

playername = input("What is your name...")

adventure_game(playername)