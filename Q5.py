PlayerOneScore = 0
PlayerTwoScore = 0
NoOfGamesInMatch= int(input("How many games?: "))

for i in range (0,NoOfGamesInMatch ):
    PlayerOneWinsGame = chr(input("Did Player One win the game (enter Y or N)?: "))
    if PlayerOneWinsGame == "y":
        PlayerOneScore = PlayerOneScore + 1
    else:
        PlayerTwoScore = PlayerTwoScore + 1

    
print(PlayerOneScore, PlayerTwoScore)
#changes