import random


def roll(): #returns random integer between 1 and 6
    minimum_value = 1
    maximum_value = 6
    number = random.randint(minimum_value, maximum_value)
    return number


while True:
    players = input("Enter number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4: #ensures that no of players is between 2 and 4
            break
        else:
            print("Value must be between 2 and 4")
    else:
        print("Enter a valid number")

max_score = 100
player_scores = [0 for _ in range(players)] #defining dynamic array to store player scrores for any amount of players


while max(player_scores) < max_score: 

    for player_index in range(players): #simulating player turns
        print(f'\nPlayer#{player_index + 1} .Your turn has begun\n')
        print(f'Your total score is: {player_scores[player_index]}\n')
        current_score = 0

        while True:
            should_roll = input(f'Wanna roll? Press (y): ')

            if should_roll.lower() == "y": #calls the roll function if user inputs 'y'
                value = roll()
                
                #if the user rolls a 1, the users current score is reset. Otherwise, the users current score is added to his total score.
                if value == 1:
                    print("You've rolled a 1. That's tuff :(")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f'You have rolled a {value}')
                print(f'Your current score is: {current_score}')

            else:
                break

        player_scores[player_index] += current_score #adds the current score to the players total score
        print(f'You have a total score of: {player_scores[player_index]}')

max_score = max(player_scores) #resets the maximum score to the highest players score to give the other players a chance to win incase he or she rolls a number that makes that makes the player's score surpass the current highest player score.
#determining and displaying the winner.
winning_index = player_scores.index(max_score)
print(f'Player number#{winning_index + 1} is the winner with a score of {max_score}')









