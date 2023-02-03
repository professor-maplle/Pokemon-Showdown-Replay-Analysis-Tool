import os
import shutil
from pathlib import Path

def main():
    folder_setup()



# Setup folders
def folder_setup():
        clean_folders()
        copy_replays()
        convert_replays()

def clean_folders():
    try:
        shutil.rmtree("src/logs")
    except OSError as e:
        pass

def copy_replays():
    shutil.copytree("src/replays", "src/logs")

def convert_replays():
    replays = os.listdir("src/logs")
    for replay in replays:
        p = Path("src/logs/" + str(replay))
        p.rename(p.with_suffix(".log"))




# Clear out replays
def clean_replays():
    pass




# Read through replays
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
def get_replays():
    replays = os.listdir("src/logs")
    for replay in replays:
        read_replays(replay)

def read_replays(battle):
    file = open("src/logs/" + str(battle), "r")
    read = file.readlines()
    print(read)

def get_teams():
    get_replays()




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