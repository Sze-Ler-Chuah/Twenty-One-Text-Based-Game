import time
import random


def display_rules():
    print("""
  _____________________________________________________________________________
  Twenty One is a game of chance where players take turns rolling two dice every 
  round until they decide to stop rolling and lock in their score or end up 
  going bust with a total over 21. The objective is to be the closest to 21 
  when everyone is done rolling.

  Rules are as per follows:
    - Players begin with a score of 0.
    - Each player has one turn to either roll or stop rolling each round.
    - Players can only do a regular roll of two dice until they 
      reach a score of at least 14.
    - Players with a score >= 14 have the option to only roll one dice.
    - If a player scores more than 21 they go bust and are out of the game.
    - The winning player is the one with the score closest to 21 when everyone 
      has finished rolling.
    - If all players go bust, no one wins.
    - If more than one player has the winning score, no one wins.
  _____________________________________________________________________________
  """)
    input("Press enter to go back")
    return

# ----------------------------------------------------------------------------------------------------------------------


def display_main_menu():
    print("------------Main Menu------------")
    print("Welcome to Twenty One!")
    print("1. Solo")
    print("2. Local Multiplayer")
    print("3. Rules")
    print("4. Exit")
    print("---------------------------------")

# ----------------------------------------------------------------------------------------------------------------------


# We did not use this function as our group has planned to do your own input error-proofin :D
def int_input(prompt="", restricted_to=None):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one is entered. Input 
    can also be restricted to a set of integers.

    Arguments:
      - prompt: String representing the message to display for input
      - restricted: List of integers for when the input must be restricted
                    to a certain set of numbers

    Returns the input in integer type.
    """
    while True:
        player_input = input(prompt)
        try:
            int_player_input = int(player_input)
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
            break

    return int_player_input

# ----------------------------------------------------------------------------------------------------------------------


# We have modified the cpu to be more intelligent and perform like a normal player :D
def cpu_player_choice(player, cpu_player):
    """
    This function simply returns a choice for the CPU player based
    on their score.

    Arguments:
      - score: Int

    Returns an int representing a choice from 1, 2 or 3.
    """
    if not cpu_player['bust']:  # Determine whether cpu need to execute_turn
        time.sleep(1.5)
        display_game_options(cpu_player)
        if cpu_player['score'] < 14:  # Roll two dice to get higher score
            player_input = "1"
        # To determine whether the cpu have to roll dice to get nearer to 21
        elif cpu_player['score'] >= 14 and cpu_player['score'] <= 17:
            player_input = "3"
        elif player['bust']:  # Cpu does not need to add score as the player already busted
            player_input = "2"
        # To determine whether the cpu have to roll dice to get nearer to 21
        elif cpu_player['score'] >= 18 and cpu_player['score'] < 21 and cpu_player['score'] <= player['score']:
            player_input = "3"
        else:  # Cpu's score is higher than the player
            player_input = "2"
        execute_turn(cpu_player, player_input)  # Cpu's turn to roll dice

# ----------------------------------------------------------------------------------------------------------------------


def display_game_options(player):
    """
    Prints the game options depending on if a player's score is
    >= 14.

    Arguments:
      - player: A player dictionary object
    """
    print("------------" + player['name'] + "'s turn------------")
    print(player['name'] + "'s score:", player['score'])
    if player['at_14'] == True:
        print("1. Roll\n2. Stay\n3. Roll One")
    else:
        print("1. Roll\n2. Stay")

# ----------------------------------------------------------------------------------------------------------------------


def display_round_stats(r, players):
    """
    Print the round statistics provided a list of players.

    Arguments:
      - round: Integer for round number
      - players: A list of player-dictionary objects
    """
    print("-----------Round", str(r)+"-----------")
    for i in range(len(players)):
        # Print out player's name and score at each round
        print(players[i]['name'], "is at", players[i]['score'])

# ----------------------------------------------------------------------------------------------------------------------


def roll_dice(num_of_dice=1):
    """
    Rolls dice based on num_of_dice passed as an argument.

    Arguments:
      - num_of_dice: Integer for amount of dice to roll

    Returns the following tuple: (rolls, display_string)
      - rolls: A list of each roll result as an int
      - display_string: A string combining the dice art for all rolls into one string
    """
    dice = [0] * num_of_dice  # The list to store the value of each rolled dice
    for i in range(num_of_dice):  # Roll the dice how many times
        # The 'i'th element of dice list which will replace the value '0' for each initial element of the list.
        dice[i] = random.randint(1, 6)

    die_art = {
        1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
        2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
        3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
        4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
        5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
        6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
    }
    dieart_sum = ""  # To be used to print several die_art of rolled dice in String

    # To be used to print the die_art of a rolled dice in String format.
    for x in range(5):
        dieart = ""
        for y in dice:  # To make sure the dieart result is same to the rolled dice result
            dieart += die_art[y][x] + ""
        dieart_sum += dieart + "\n"

    # Tuples to store dice and dice_art accordingly.
    result = (dice, dieart_sum)
    return result

# ----------------------------------------------------------------------------------------------------------------------


def execute_turn(player, player_input):
    """
    Executes one turn of the round for a given player.

    Arguments:
      - player: A player dictionary object

    Returns an updated player dictionary object.
    """
    if int(player_input) == 2:  # Player choose not to roll the dice
        print(player['name'], "has stayed with a score of", player['score'])
        player['stayed'] = True
        return player  # Update player's dictionary for player['stayed']

    elif int(player_input) == 1:  # Player choose to roll 2 dices
        player['stayed'] = False
        print("Rolling both...")
        # Store the result of dice, diceart_sum in a tuple
        result = roll_dice(2)
        for x in range(2):  # Store the tuple into the player's dictionary
            player['score'] += result[0][x]
        print(result[1])  # Print the dice
        print("\n" + player['name'], "is now on",
              player['score'])  # Print the player's result

    elif int(player_input) == 3:  # Player choose to roll 1 dice(if he/she has at least 14 score)
        player['stayed'] = False
        print("Rolling one...")
        # Store the result of dice, diceart_sum in a tuple
        result = roll_dice(1)
        # Store the tuple into the player's dictionary
        player['score'] += result[0][0]
        print(result[1])  # Print the dice
        print("\n" + player['name'], "is now on",
              player['score'])  # Print the player's result

    else:  # Determine whether the player's input is valid
        print("Invalid Choice")
        return False

    # Update player's status(busted or at_14)
    if player['score'] >= 14 and player['score'] <= 21:
        player['at_14'] = True

    elif player['score'] > 21:
        player['at_14'] = True
        player['bust'] = True
        print(player['name'], "goes bust!")

    return player  # Update player's dictionary

# ----------------------------------------------------------------------------------------------------------------------


def end_of_game(players):
    """
    Takes the list of all players and determines if the game has finished,
    returning false if not else printing the result before returning true.

    Arguments:
      - players: A list of player-dictionary objects

    Returns True if round has ended or False if not. If true results are
    printed before return.
    """
    bust_count = 0  # Calculate the number of players who has busted
    winner_score = -1  # To ensure nobody stay at the beginning of the game
    end = 0  # To determine whether the game will end
    draw = False

    for player in players:  # Loop through every player in players list
        if player['bust']:  # Accumulate the number of players who has busted or stayed
            bust_count += 1
            end += 1
        if player['stayed']:  # Accumulate the number of players who has stayed
            end += 1

    # To determine whether the game ended
    if bust_count >= (len(players)-1) or end == len(players):
        # This loop is to determine the result of the game
        for player in players:
            if not player['bust']:  # Find the player who doesn't bust when the game ended
                # To determine whether the player has the highest score
                if player['score'] > winner_score:
                    draw = False  # To avoid 'draw' error
                    # Winner_score replaced by player{'score'] which is higher than it
                    winner_score = player['score']
                    winner = player['name']  # Store the winner's name
                elif player['score'] == winner_score:
                    draw = True  # There's a draw situation occur
                    break

        if bust_count == len(players):  # A situation of everyone has busted
            print("Everyone's gone bust! No one wins :(")
        elif draw == True:  # A situation of everyone is draw
            print("The game is a draw! No one wins :(")
        else:  # A situation of one of players is the winner
            print(winner, 'is the winner!')
        return True

    else:
        return False

# ----------------------------------------------------------------------------------------------------------------------


def solo_game(player, cpu_player, players):
    r = 0  # To record the current round
    while not end_of_game(players):  # Continue the game as the game hasn't ended
        display_round_stats(r, players)  # display the stat

        # if player['bust'] || player['stayed'] is false, execute code below
        if not (player['bust'] or player['stayed']):
            display_game_options(player)
            while True:  # To determine the input's validity
                player_input = input("Please enter an option: ")
                # When player score < 14, players have the option to roll one dice or stay.
                if not player['at_14'] and (player_input == '1' or player_input == '2'):
                    break  # While loop break so that execute_turn can be excuted
                # When player score >= 14, players have the option to roll one or two dices or stay
                elif player['at_14'] and (player_input == '1' or player_input == '2' or player_input == '3'):
                    break
                else:
                    # The user input wrongly, the loop start again
                    print("Invalid Choice")
            execute_turn(player, player_input)

        # Cpu can only execute its turn when it does not bust, not stayed and player does not bust.
        if not (cpu_player['bust'] or cpu_player['stayed'] or player['bust']):
            cpu_player_choice(player, cpu_player)

        r += 1  # Accumulate the current round

# ----------------------------------------------------------------------------------------------------------------------


def multiplayer_game(num_of_players):
    r = 0  # To record the current round
    players = []

    # To set the starting index to 1 and end at num_of_player+1 and create dictionaries same as the amount of players
    for i in range(1, num_of_players+1):
        player = {'name': 'Player 1', 'score': 0,
                  'stayed': False, 'at_14': False, 'bust': False}
        player['name'] = 'Player '+str(i)  # Change the name of player
        # Add dictionaries to the list same as the amount of players
        players.append(player)

    while not end_of_game(players):  # Continue the game as the game hasn't ended
        display_round_stats(r, players)  # Display round stat
        for player in players:  # Players take turn to execute turn
            # To determine whether the player can execute or not
            if not (player['bust'] or player['stayed']):
                display_game_options(player)  # Display game option
                while True:  # To determine the input's validity
                    player_input = input("Please enter an option: ")
                    # When player score < 14, players have the option to roll one dice or stay.
                    if not player['at_14'] and (player_input == '1' or player_input == '2'):
                        break
                    # When player score >= 14, players have the option to roll one or two dices or stay
                    elif player['at_14'] and (player_input == '1' or player_input == '2' or player_input == '3'):
                        break
                    else:
                        # The user input wrongly, the loop start again
                        print("Invalid Choice")
                execute_turn(player, player_input)
        r += 1  # Accumulate the current round

# ----------------------------------------------------------------------------------------------------------------------


def main():
    """
    Defines the main loop that allows the player to start a game, view rules or quit.
    """
    display_main_menu()
    selection = int(input("Please select an option: "))

    if selection == 1:
        # Set the dictionary of player and cpu
        player = {'name': 'Player 1', 'score': 0,
                  'stayed': False, 'at_14': False, 'bust': False}
        cpu_player = {'name': 'CPU Player', 'score': 0,
                      'stayed': False, 'at_14': False, 'bust': False}
        players = [player, cpu_player]  # Create a list for dictionaries
        solo_game(player, cpu_player, players)
        main()  # Execute again after finishing the game

    elif selection == 2:
        # To determine the amount of player(prevent too many player or negative values)
        while True:
            no_of_players = int(
                input("Enter the amount of players(2 to 10): "))
            if no_of_players >= 2 and no_of_players <= 10:
                break
            else:
                print("Please enter the amount of players between 2 to 10")
        multiplayer_game(no_of_players)
        main()  # Execute again after finishing the game

    elif selection == 3:
        display_rules()
        main()  # Display rules

    elif selection == 4:
        print("Thank You for playing!")
        quit()  # Exit the program

    else:
        print("Invalid Selection")
        main()  # Execute again for user to make another valid selection


main()


