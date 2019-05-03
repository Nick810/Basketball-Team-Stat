import os
from constants import TEAMS, PLAYERS


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
                elif menu_choice == 2:
                    break
            except ValueError:
                print("That's not a number... Please enter a number either 1 or 2.\n")
            break


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
            print("That's not a number... Please enter a number either 1 or 2.\n")


def panthers_stats():
    panther_players = []
    experienced_players = []
    inexperienced_players = []
    guardians_list = []
    heights_list = []
    average_height = ""

    panthers_team = PLAYERS.copy()
    del panthers_team[5]
    panthers_team = panthers_team[:6]

    for people in panthers_team:
        for keys, values in people.items():
            if keys == 'name':
                panther_players.append(values)

    each_pPlayers = [(i) for i in panther_players]
    pPlayers = ", ".join(each_pPlayers)

    for people in panthers_team:
        for keys, values in people.items():
            if values == 'YES':
                experienced_players.append([keys for keys in people.values()][0])

    for people in panthers_team:
        for keys, values in people.items():
            if values == 'NO':
                inexperienced_players.append([keys for keys in people.values()][0])

    for people in panthers_team:
        for keys, values in people.items():
            if keys == 'height':
                heights_list.append(values)

    panthers_height = [''.join([m for m in k if m.isnumeric()]) for k in heights_list]
    panthers_height = list(map(int, panthers_height))

    total_height = 0
    for player in panthers_height:
        total_height = total_height + player
    average_height = int(total_height / len(panthers_team))

    for people in panthers_team:
        for keys, values in people.items():
            if keys == 'guardians':
                guardians_list.append(values)

    each_pGuardians = [(i) for i in guardians_list]
    pGuardians = ", ".join(each_pGuardians)

    print("\nTeam: {} Stats".format(TEAMS[0]))
    print("-"*20)
    print("Total players {}\n".format(len(panther_players)))
    print("Total number of experienced players: {}".format(len(experienced_players)))
    print("Total number of inexperienced players: {}".format(len(inexperienced_players)))
    print("The average height of the team: {}\n".format(average_height))
    print("Players on Team:\n  {}\n".format(pPlayers))
    print("Guardians on the Team:\n  {}\n".format(pGuardians))
    enterToContinue()


def bandits_stats():
    bandit_players = []
    experienced_players = []
    inexperienced_players = []
    guardians_list = []
    heights_list = []
    average_height = ""

    bandits_team = PLAYERS.copy()
    del bandits_team[6]
    bandits_team = bandits_team[5:11:]

    for people in bandits_team:
        for keys, values in people.items():
            if keys == 'name':
                values = bandit_players.append(values)

    each_bPlayers = [(i) for i in bandit_players]
    bPlayers = ", ".join(each_bPlayers)

    for people in bandits_team:
        for keys, values in people.items():
            if values == 'YES':
                experienced_players.append([keys for keys in people.values()][0])

    for people in bandits_team:
        for keys, values in people.items():
            if values == 'NO':
                inexperienced_players.append([keys for keys in people.values()][0])

    for people in bandits_team:
        for keys, values in people.items():
            if keys == 'height':
                heights_list.append(values)

    bandits_height = [''.join([m for m in k if m.isnumeric()]) for k in heights_list]
    bandits_height = list(map(int, bandits_height))

    total_height = 0
    for player in bandits_height:
        total_height = total_height + player
    average_height = int(total_height / len(bandits_team))

    for people in bandits_team:
        for keys, values in people.items():
            if keys == 'guardians':
                guardians_list.append(values)

    each_bGuardians = [(i) for i in guardians_list]
    bGuardians = ", ".join(each_bGuardians)

    print("\nTeam: {} Stats".format(TEAMS[1]))
    print("-"*19)
    print("Total players {}\n".format(len(bandits_team)))
    print("Total number of experienced players: {}".format(len(experienced_players)))
    print("Total number of inexperienced players: {}".format(len(inexperienced_players)))
    print("The average height of the team: {}\n".format(average_height))
    print("Players on Team:\n  {}\n".format(bPlayers))
    print("Guardians on the Team:\n  {}\n".format(bGuardians))
    enterToContinue()


def warriors_stats():
    warriors_team = PLAYERS.copy()
    warriors_team = warriors_team[-6:]
    warrior_players = []
    experienced_players = []
    inexperienced_players = []
    guardians_list = []
    heights_list = []
    average_height = ""

    for people in warriors_team:
        for keys, values in people.items():
            if keys == 'name':
                values = warrior_players.append(values)

    for people in warriors_team:
        for keys, values in people.items():
            if values == 'YES':
                experienced_players.append([keys for keys in people.values()][0])

    for people in warriors_team:
        for keys, values in people.items():
            if values == 'NO':
                inexperienced_players.append([keys for keys in people.values()][0])

    each_wPlayers = [(i) for i in warrior_players]
    wPlayers = ", ".join(each_wPlayers)

    for people in warriors_team:
        for keys, values in people.items():
            if keys == 'height':
                heights_list.append(values)

    warriors_height = [''.join([m for m in k if m.isnumeric()]) for k in heights_list]
    warriors_height = list(map(int, warriors_height))

    total_height = 0
    for player in warriors_height:
        total_height = total_height + player
    average_height = int(total_height / len(warriors_team))

    for people in warriors_team:
        for keys, values in people.items():
            if keys == 'guardians':
                guardians_list.append(values)

    each_wGuardians = [(i) for i in guardians_list]
    wGuardians = ", ".join(each_wGuardians)

    print("\nTeam: {} Stats".format(TEAMS[2]))
    print("-"*20, "\n")
    print("Total players {}\n".format(len(warriors_team)))
    print("Total number of experienced players: {}".format(len(experienced_players)))
    print("Total number of inexperienced players: {}".format(len(inexperienced_players)))
    print("The average height of the team: {}\n".format(average_height))
    print("Players on Team:\n  {}\n".format(wPlayers))
    print("Guardians on the Team:\n  {}\n".format(wGuardians))
    enterToContinue()


def enterToContinue():
    while True:
        moveOn = input("Press ENTER to continue...")
        if moveOn == "":
            start()
            break
        elif moveOn == str or int:
            print("You didn't press ENTER. Please press ENTER to continue\n")


if __name__ == "__main__":
    start()
