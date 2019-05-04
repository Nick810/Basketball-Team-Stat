import os
import copy
from constants import TEAMS, PLAYERS

constants_copy = copy.deepcopy(PLAYERS)
clean_data = []

for players in constants_copy:
    if players['experience'] == 'NO':
        players['experience'] = False
        players['guardians'] = players['guardians'].split()
        players['height'] = players['height'].split()
        del players['height'][1]
        players['height'] = (sum(list(map(int, players['height']))))
        clean_data.append(players)

for players in constants_copy:
    if players['experience'] == 'YES':
        players['experience'] = True
        players['guardians'] = players['guardians'].split()
        players['height'] = players['height'].split()
        del players['height'][1]
        players['height'] = (sum(list(map(int, players['height']))))
        clean_data.append(players)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def start():
        clear_screen()
        print(" BASKETBALL TEAM STATS TOOL\n")
        print("-"*28)
        print(" "*8, "- MENU -")
        print("-"*28)
        print("")
        while True:
            try:
                print("Here are your choices:")
                print(" 1) Display Team Stats\n 2) Quit\n\n")

                menu_choice = int(input("Enter an option > "))
                if menu_choice <= 0 or menu_choice >= 3:
                    print("That's not a valid option. Please enter a number either 1 or 2.\n")
                elif menu_choice == 1:
                    teams_options()
                    break
                elif menu_choice == 2:
                    break
            except ValueError:
                print("That's not a number... Please enter a number either 1 or 2.\n")
            

def teams_options():
    while True:
        try:
            print("1) Panthers")
            print("2) Bandits")
            print("3) Warriors\n")
            team_choice = int(input("Enter an option > "))
            if team_choice == 1:
                panthers_stats()
                break
            elif team_choice == 2:
                bandits_stats()
                break
            elif team_choice == 3:
                warriors_stats()
                break
            else:
                print("That's not a valid option. Please enter a number between 1 to 3.\n")
        except ValueError:
            print("That's not a number... Please enter a number between 1 to 3.\n")

def enterToContinue():
    while True:
        moveOn = input("Press ENTER to continue... ")
        if moveOn == "":
            start()
            break
        elif moveOn == str or int:
            print("You didn't press ENTER. Please press ENTER to continue\n")


def panthers_stats():
    panthers_team = clean_data[:3] + clean_data[-3:]
    panthers_players = []
    experienced_players = []
    inexperienced_players = []
    pGuardians = []
    heights_list = []

    for player in panthers_team:
        if player['name']:
            panthers_players.append(player['name'])
        
    pPlayers = ", ".join(panthers_players)

    for player in panthers_team:
        if player['experience'] == True:
            experienced_players.append(players['name'])
        else:
            inexperienced_players.append(players['name'])

    for player in panthers_team:
        if player['height']:
            heights_list.append(player['height'])
            
    total_height = sum(heights_list)
    average_height = int(total_height / len(panthers_players))
    
    for player in panthers_team:
        pGuardians.append(' '.join(player['guardians']))
        
    print("\nTeam: {} Stats".format(TEAMS[0]))
    print("-"*20)
    print("Total players {}\n".format(len(panthers_players)))
    print("Total number of experienced players: {}".format(len(experienced_players)))
    print("Total number of inexperienced players: {}".format(len(inexperienced_players)))
    print("The average height of the team: {}\n".format(average_height))
    print("Players on Team:\n  {}\n".format(pPlayers))
    print("Guardians on the Team:")
    print('  ', ', '.join(pGuardians))
    enterToContinue()


def bandits_stats():
    bandits_team = clean_data[3:6:] + clean_data[12:15:]
    bandits_players = []
    experienced_players = []
    inexperienced_players = []
    bGuardians = []
    heights_list = []

    for player in bandits_team:
        if player['name']:
            bandits_players.append(player['name'])
        
    bPlayers = ", ".join(bandits_players)

    for player in bandits_team:
        if player['experience'] == True:
            experienced_players.append(players['name'])
        else:
            inexperienced_players.append(players['name'])
            
    for player in bandits_team:
        if player['height']:
            heights_list.append(player['height'])
            
    total_height = sum(heights_list)
    average_height = int(total_height / len(bandits_players))
    
    for player in bandits_team:
        bGuardians.append(' '.join(player['guardians']))
        
    print("\nTeam: {} Stats".format(TEAMS[1]))
    print("-"*20)
    print("Total players {}\n".format(len(bandits_players)))
    print("Total number of experienced players: {}".format(len(experienced_players)))
    print("Total number of inexperienced players: {}".format(len(inexperienced_players)))
    print("The average height of the team: {}\n".format(average_height))
    print("Players on Team:\n  {}\n".format(bPlayers))
    print("Guardians on the Team:")
    print('  ', ', '.join(bGuardians))
    enterToContinue()


def warriors_stats():
    warriors_team = clean_data[6:9:] + clean_data[9:12:]
    warriors_players = []
    experienced_players = []
    inexperienced_players = []
    wGuardians = []
    heights_list = []

    for player in warriors_team:
        if player['name']:
            warriors_players.append(player['name'])
        
    wPlayers = ", ".join(warriors_players)

    for player in warriors_team:
        if player['experience'] == True:
            experienced_players.append(players['experience'])
        else:
            inexperienced_players.append(players['experience'])

    for player in warriors_team:
        heights_list.append(player['height'])

    total_height = sum(heights_list)
    average_height = int((total_height / len(warriors_players)))
    
    for player in warriors_team:
        wGuardians.append(' '.join(player['guardians']))
        
    print("\nTeam: {} Stats".format(TEAMS[2]))
    print("-"*20)
    print("Total players {}\n".format(len(warriors_players)))
    print("Total number of experienced players: {}".format(len(experienced_players)))
    print("Total number of inexperienced players: {}".format(len(inexperienced_players)))
    print("The average height of the team: {}\n".format(average_height))
    print("Players on Team:\n {}\n".format(wPlayers))
    print("Guardians on the Team:")
    print(', '.join(wGuardians))
    enterToContinue()
    

if __name__ == "__main__":
    start()
