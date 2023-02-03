from pathlib import Path


def main():
    replay_to_log()



# Copy replays from replays folder to log files in logs folder
def replay_to_log():
    p = Path("resources/logs")
    p.mkdir(exist_ok=True)




# Read through log files
## Create a folder for each trainer found in replays
## Create a file for each Pokemon in their folder
## Store following data in each Pokemons file
### Number of battles fought
### Number of kills
### Number of deaths
### Number of times each move was used
### Number of times each item was used
### Number of times each ability was used
### Highest Damage Move in each game





# Compare data collected to determine winner of these categories
## League Wide
### Most kills
### Most deaths
### Most devastating move
## Per Pokemon
### Brought to {num} battles
### Most used item
### Most used move
### Most used ability





# Save results to "results.txt"




# Execute code
main()