
#  File: term project

#  Description:

#  Student Name: Jesse Ilangoraja

#  Student UT EID: jvi83

#  Partner Name: Isabella Zeballos

#  Partner UT EID: iez79

#  Course Name: CS 313E

#  Unique Number: 50775

#  Date Created: 4/16

#  Date Last Modified: 4/16


players_stats = {
    "Luka Doncic": {
        "PTS": 33.9,
        "REB": 9.2,
        "AST": 9.8,
        "STL": 1.4,
        "BLK": 0.5,
        "Missed_FG": 8.4,
        "Missed_FT": 0.8,
        "TO": 4.0,
        "GP": 70
    },
    "Giannis Antetokounmpo": {
        "PTS": 30.4,
        "REB": 11.5,
        "AST": 6.5,
        "STL": 1.2,
        "BLK": 1.1,
        "Missed_FG": 8.8,
        "Missed_FT": 2.7,
        "TO": 3.4,
        "GP": 73
    },
    "Shai Gilgeous-Alexander": {
        "PTS": 30.1,
        "REB": 5.5,
        "AST": 6.2,
        "STL": 0.9,
        "BLK": 0.9,
        "Missed_FG": 4.7,
        "Missed_FT": 0.9,
        "TO": 2.2,
        "GP": 75
    },
    "Jalen Brunson": {
        "PTS": 28.7,
        "REB": 3.6,
        "AST": 6.7,
        "STL": 0.6,
        "BLK": 0.2,
        "Missed_FG": 3.1,
        "Missed_FT": 0.6,
        "TO": 2.4,
        "GP": 77
    },
    "Kevin Durant": {
        "PTS": 27.1,
        "REB": 6.6,
        "AST": 5.0,
        "STL": 0.8,
        "BLK": 1.2,
        "Missed_FG": 6.1,
        "Missed_FT": 0.5,
        "TO": 3.3,
        "GP": 75
    },
    "Devin Booker": {
        "PTS": 27.1,
        "REB": 4.5,
        "AST": 6.9,
        "STL": 0.8,
        "BLK": 0.4,
        "Missed_FG": 3.7,
        "Missed_FT": 0.8,
        "TO": 2.6,
        "GP": 68
    },
    "Jayson Tatum": {
        "PTS": 26.9,
        "REB": 4.9,
        "AST": 4.9,
        "STL": 1.0,
        "BLK": 0.6,
        "Missed_FG": 7.2,
        "Missed_FT": 0.9,
        "TO": 2.5,
        "GP": 74
    },
    "De'Aaron Fox": {
        "PTS": 26.6,
        "REB": 5.6,
        "AST": 5.6,
        "STL": 2.0,
        "BLK": 0.4,
        "Missed_FG": 3.7,
        "Missed_FT": 0.9,
        "TO": 2.6,
        "GP": 74
    },
    "Stephen Curry": {
        "PTS": 26.4,
        "REB": 5.1,
        "AST": 5.1,
        "STL": 0.7,
        "BLK": 0.4,
        "Missed_FG": 4.0,
        "Missed_FT": 0.5,
        "TO": 2.8,
        "GP": 74
    },
    "Nikola Jokic": {
        "PTS": 26.4,
        "REB": 9.0,
        "AST": 9.0,
        "STL": 1.4,
        "BLK": 0.9,
        "Missed_FG": 9.5,
        "Missed_FT": 2.8,
        "TO": 3.0,
        "GP": 79
    },
    "Tyrese Maxey": {
        "PTS": 25.9,
        "REB": 6.2,
        "AST": 6.2,
        "STL": 1.0,
        "BLK": 0.5,
        "Missed_FG": 3.2,
        "Missed_FT": 0.5,
        "TO": 1.7,
        "GP": 70
    },
    "Anthony Edwards": {
        "PTS": 25.9,
        "REB": 5.1,
        "AST": 5.1,
        "STL": 1.3,
        "BLK": 0.5,
        "Missed_FG": 4.8,
        "Missed_FT": 0.7,
        "TO": 3.1,
        "GP": 79
    },
    "LeBron James": {
        "PTS": 25.7,
        "REB": 8.3,
        "AST": 8.3,
        "STL": 1.3,
        "BLK": 0.5,
        "Missed_FG": 6.4,
        "Missed_FT": 0.9,
        "TO": 3.5,
        "GP": 71
    },
    "Kyrie Irving": {
        "PTS": 25.6,
        "REB": 5.2,
        "AST": 5.2,
        "STL": 1.3,
        "BLK": 0.5,
        "Missed_FG": 4.2,
        "Missed_FT": 0.8,
        "TO": 1.8,
        "GP": 58
    },
    "Anthony Davis": {
        "PTS": 24.7,
        "REB": 12.6,
        "AST": 3.5,
        "STL": 1.2,
        "BLK": 2.3,
        "Missed_FG": 9.5,
        "Missed_FT": 3.1,
        "TO": 2.1,
        "GP": 76
    },
    "Damian Lillard": {
        "PTS": 24.3,
        "REB": 7.0,
        "AST": 7.0,
        "STL": 1.0,
        "BLK": 0.2,
        "Missed_FG": 3.9,
        "Missed_FT": 0.5,
        "TO": 2.6,
        "GP": 73
    },
    "DeMar DeRozan": {
        "PTS": 24.0,
        "REB": 5.3,
        "AST": 5.3,
        "STL": 1.1,
        "BLK": 0.6,
        "Missed_FG": 3.8,
        "Missed_FT": 0.5,
        "TO": 1.7,
        "GP": 79
    },
    "Kawhi Leonard": {
        "PTS": 23.7,
        "REB": 3.6,
        "AST": 3.6,
        "STL": 1.6,
        "BLK": 0.9,
        "Missed_FG": 4.9,
        "Missed_FT": 1.2,
        "TO": 1.8,
        "GP": 68
    },
    "Jaylen Brown": {
        "PTS": 23.0,
        "REB": 3.6,
        "AST": 3.6,
        "STL": 1.2,
        "BLK": 0.5,
        "Missed_FG": 4.3,
        "Missed_FT": 1.2,
        "TO": 2.4,
        "GP": 70
    },
    "Zion Williamson": {
        "PTS": 22.9,
        "REB": 5.0,
        "AST": 5.0,
        "STL": 1.1,
        "BLK": 0.7,
        "Missed_FG": 4.1,
        "Missed_FT": 1.7,
        "TO": 2.8,
        "GP": 70
    },
    "Cade Cunningham": {
        "PTS": 22.7,
        "REB": 7.5,
        "AST": 7.5,
        "STL": 0.9,
        "BLK": 0.4,
        "Missed_FG": 3.8,
        "Missed_FT": 0.5,
        "TO": 3.4,
        "GP": 62
    },
    "Paul George": {
        "PTS": 22.6,
        "REB": 3.5,
        "AST": 3.5,
        "STL": 1.5,
        "BLK": 0.5,
        "Missed_FG": 4.7,
        "Missed_FT": 0.5,
        "TO": 2.1,
        "GP": 74
    },
    "Paolo Banchero": {
        "PTS": 22.6,
        "REB": 5.4,
        "AST": 5.4,
        "STL": 0.9,
        "BLK": 0.6,
        "Missed_FG": 5.9,
        "Missed_FT": 1.0,
        "TO": 3.1,
        "GP": 80
    },
    "Jaren Jackson Jr.": {
        "PTS": 22.5,
        "REB": 2.3,
        "AST": 2.3,
        "STL": 1.2,
        "BLK": 1.6,
        "Missed_FG": 4.2,
        "Missed_FT": 1.3,
        "TO": 2.4,
        "GP": 66
    },
    "Dejounte Murray": {
        "PTS": 22.5,
        "REB": 6.4,
        "AST": 6.4,
        "STL": 1.4,
        "BLK": 0.3,
        "Missed_FG": 4.5,
        "Missed_FT": 0.8,
        "TO": 2.6,
        "GP": 78
    },
    "Cam Thomas": {
        "PTS": 22.5,
        "REB": 2.9,
        "AST": 2.9,
        "STL": 0.7,
        "BLK": 0.2,
        "Missed_FG": 2.8,
        "Missed_FT": 0.4,
        "TO": 1.9,
        "GP": 66
    },
    "Kyle Kuzma": {
        "PTS": 22.2,
        "REB": 4.2,
        "AST": 4.2,
        "STL": 0.5,
        "BLK": 0.7,
        "Missed_FG": 5.7,
        "Missed_FT": 0.9,
        "TO": 2.7,
        "GP": 70
    },
    "Karl-Anthony Towns": {
        "PTS": 21.8,
        "REB": 13.0,
        "AST": 3.0,
        "STL": 0.7,
        "BLK": 0.7,
        "Missed_FG": 6.8,
        "Missed_FT": 1.5,
        "TO": 2.9,
        "GP": 62
    },
    "Pascal Siakam": {
        "PTS": 21.7,
        "REB": 4.3,
        "AST": 4.3,
        "STL": 0.8,
        "BLK": 0.3,
        "Missed_FG": 5.3,
        "Missed_FT": 1.7,
        "TO": 1.8,
        "GP": 80
    },
    "Victor Wembanyama": {
        "PTS": 21.4,
        "REB": 3.9,
        "AST": 3.9,
        "STL": 0.9,
        "BLK": 3.6,
        "Missed_FG": 8.4,
        "Missed_FT": 2.3,
        "TO": 3.7,
        "GP": 71
    }
}


def player_search(players, target):
    #soting list
    sorted_players = sorted(players.keys())

    left = 0
    right = len(sorted_players) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_player = sorted_players[mid]
        
        # Check if the target player is found
        if mid_player == target:
            return players[mid_player]
        elif mid_player < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # If the player is not found, return None
    return None

def get_specific_stat(players, player_name):
    player_stats = player_search(players, player_name)
    if player_stats is not None:
        specific_stat_choice = input(f"Do you want to see a specific statistic for {player_name}? (yes/no): ").lower()
        if specific_stat_choice == "yes":
            stat_to_check = input("Which statistic would you like to see? (PTS, REB, AST, STL, BLK, Missed_FG, Missed_FT, TO): ").upper()
            if stat_to_check in player_stats:
                print(f"{player_name}'s {stat_to_check}: {player_stats[stat_to_check]}")
            else:
                print(f"Invalid statistic '{stat_to_check}'.")
        elif specific_stat_choice == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print(f"Player '{player_name}' not found in the database.")


def stat_leader(players, stat_req):
    stat_list=[]
    for player, stat  in players.items():
        for criteria, number in stat.items():
            if criteria == stat_req:
                stat_list.append(number)
    max_stat = max(stat_list)
    leader_list=[]
    for player, stat  in players.items():
        for criteria, number in stat.items():
            if number == max_stat:
                leader_list.append(player)
    return leader_list


def effeciency_cal(players_list, player):
    results= player_search(players_list, player)
    points = results["PTS"]
    rebounds = results["REB"]
    assists = results["AST"]
    steals = results["STL"]
    blocks = results["BLK"]
    missed_fg = results["Missed_FG"]
    missed_ft = results["Missed_FT"]
    turnovers = results["TO"]
    games_played = results["GP"]
    eff = (points + rebounds + assists + steals + blocks - missed_fg - missed_ft - turnovers)/games_played
    return eff



def stat_over(category, number):
    over_list=[]
    for key,value in players_stats.items():
        if value[category] >= number:
            over_list.append(key)
    return over_list


def stat_under(category, number):
    under_list=[]
    for key,value in players_stats.items():
        if value[category] < number:
            under_list.append(key)
    return under_list



def main():
   
    while True:
            player_name = input("Welcome to the NBA player efficiency calculator. Enter the name of a player here for their efficiency score: ")
            player_stats = player_search(players_stats, player_name)

            if player_stats is None:
                print(f"Player '{player_name}' is not in the database.")
                retry = input("Would you like to try another player? (yes/no): ").lower()
                if retry == "no":
                    break
                else:
                    continue

            target = effeciency_cal(players_stats, player_name)
            print(f"Efficiency rating for {player_name}: {target}")

            get_specific_stat(players_stats, player_name)

            goodbye = input("Would you like to know the efficiency score of another player? (yes/no): ").lower()
            if goodbye == "no":
                break
    
    leader_q = input("Would you like to see the leader in a particular statistical category? (yes/no):")
    if leader_q == "yes":
        category = input('Which category?(PTS, REB, AST, STL, BLK, Missed_FG, Missed_FT, TO):')
        if category not in ["PTS", "REB", "AST", "STL",  "BLK", "Missed_FG", "Missed_FT",  "TO",  "GP"]:
            print("Not a valid category")
        else:
            answer = stat_leader(players_stats, category)
            leaders = ", ".join(answer)
            print(f"The leader(s) in {category} is/are: {leaders}")
    

    over_under_q = input("Would you like to see players over or under a specific stat for a category? (yes/no): ")
    if over_under_q == "yes":
        category = input("Enter the category (PTS, REB, AST, STL, BLK, Missed_FG, Missed_FT, TO): ")
        if category not in ["PTS", "REB", "AST", "STL", "BLK", "Missed_FG", "Missed_FT", "TO"]:
            print("Not a valid category")
        else:
            comparison = input("Would you like to see players over or under this stat? (over/under): ")
            if comparison == "over":
                number = float(input("Enter the number for comparison: "))
                over_list = stat_over(category, number)
                print(f"Players with {category} over {number}: {', '.join(over_list)}")
            elif comparison == "under":
                number = float(input("Enter the number for comparison: "))
                under_list = stat_under(category, number)
                print(f"Players with {category} under {number}: {', '.join(under_list)}")
            else:
                print("Invalid input.")

    print('Thank you for using the NBA player efficiency calculator! Goodbye.')
   

if __name__ == "__main__":
    main()