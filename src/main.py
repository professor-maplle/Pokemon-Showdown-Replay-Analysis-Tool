import os
import shutil
import bs4
from pathlib import Path

def main():
    folder_setup()
    get_trainers()



# Setup folders
def folder_setup():
        clean_folders()
        create_logs_dir()
        get_battle_logs()

## Deletes logs folder so it can be filled with new logs
def clean_folders():
    try:
        shutil.rmtree("src/logs")
    except OSError as e:
        pass

## Create logs directory to store battle logs in
def create_logs_dir():
    p = Path("src/logs")
    try:
        p.mkdir()
    except FileExistsError as exc:
        pass

## Runs through each replay, obtaining their battle log data and passing it into save_log()
def get_battle_logs():
    replays=os.listdir("src/replays")
    for replay in replays:
        file = open("src/replays/" + str(replay), "r")
        read = file.readlines()
        file.close()
        soup = bs4.BeautifulSoup(str(read), "html.parser")
        battle_log = soup.find(class_="battle-log-data")
        save_log(battle_log, str(replay))

## Saves battle log data into a new file in logs directory
def save_log(battle_log, file_name):
    file = open("src/logs/" + file_name, "x")
    p = Path("src/logs/" + file_name)
    p.rename(p.with_suffix(".log"))
    file.write(str(battle_log))
    file.close()




# Read through replays
## Create a folder for each trainer found in replays
def get_trainers():
    pass

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