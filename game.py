print("Welcome to stick game")
print("Description,the player to pick the last stick losses the game")
print("Rules:")
print("This is two player game.\n 16 sticks are on table")
print("Each player can picks one set of sticks during his/her turn.")
print("a set contain 1,2 or 3 sticks")

remaining_sticks=16
player1=input("Enter the name of the player 1")
player2=input("Enter the name of the player 2")

turn=player1
n=1
while True:
    turn=player1 if n%2!=0 else player2
    print(f"Remaining sticks:{remaining_sticks}")
    number_of_sticks_in_the_set=int(input(f"{turn},pick a set of 1,2 or 3 sticks:"))
    if (remaining_sticks-number_of_sticks_in_the_set)<0:
        print("/n insufficient sticks.please try again.")
        continue
    elif remaining_sticks==number_of_sticks_in_the_set:
        print(f"\n{turn} lost the game")
        break
    else:
        remaining_sticks-=number_of_sticks_in_the_set
    n+=1