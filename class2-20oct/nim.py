TotalNumMatchesLeft = 15

def playerInput (player : str) -> int :
    value = input(player + ", please enter the number of matches you want to take?")
    return value

print("Game Start")
print("Total number of matches = " + str(TotalNumMatchesLeft) )


while TotalNumMatchesLeft > 0:
    ip = playerInput("player1")
    TotalNumMatchesLeft -= int(ip)
    print(ip)
