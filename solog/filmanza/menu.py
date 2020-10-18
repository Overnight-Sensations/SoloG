from solog.filmanza.gameplay import hollywood_medium, bollywood_medium, bollywood_hard, hollywood_hard, hollywood_easy, bollywood_easy

def game_level():
    print("\t\t\tSelect Difficulty")
    print("Press '1' for Easy")
    print("Press '2' for Medium")
    print("Press '3' for Hard")
    lvl = int(input())
    val_level= [1,2,3]
    if lvl not in val_level:
        print('Wrong input')
        game_level()
    return lvl

def game_type():
    print("Press '1' for Bollywood ")
    print("Press '2' for Hollywood")
    choice_type = int(input())
    val_lvl = [1,2]
    if choice_type not in val_lvl:
        print('Wrong input')
        game_type()
    return choice_type

def menu():
    game = [[bollywood_easy(),bollywood_medium(),bollywood_hard()],
           [hollywood_easy(),hollywood_medium(),hollywood_hard()]]
    game[game_type][game_level]
