import os
import shutil
import bs4
from pathlib import Path

def main():
    folder_setup()
    get_battle_logs()
    get_trainers()




# Setup folders
def folder_setup():
        clean_folders()
        create_logs_dir()
        create_trainers_dir()

## Deletes logs folder so it can be filled with new logs
def clean_folders():
    try:
        shutil.rmtree("src/logs")
    except OSError as e:
        pass

    try:
        shutil.rmtree("src/trainers")
    except OSError as exc:
        pass

## Create logs directory to store battle logs in
def create_logs_dir():
    p = Path("src/logs")
    try:
        p.mkdir()
    except FileExistsError as exc:
        pass

def create_trainers_dir():
    p = Path("src/trainers")
    try:
        p.mkdir()
    except FileExistsError as exc:
        pass

## Runs through each replay, obtaining their battle log data and passing it into save_log()
def get_battle_logs():
    replays=os.listdir("src/replays")
    for replay in replays:
        file = open("src/replays/" + str(replay), "r")
        read = file.read()
        file.close()
        soup = bs4.BeautifulSoup(str(read), "html.parser")
        battle_log = soup.find(class_="battle-log-data")
        save_log(battle_log, str(replay))

## Saves battle log data into a new file in logs directory
def save_log(battle_log, file_name):
    file = open("src/logs/" + file_name, "x")
    p = Path("src/logs/" + file_name)
    p.rename(p.with_suffix(".log"))
    file.write(str(battle_log).strip())
    file.close()




# Read through replays
## Create a folder for each trainer found in replays
### Store player name in a string by going to "p1|" in log and reading until the next "|", then "p2"
### Create new directory with players username as the directory name
def get_trainers():
    logs = os.listdir("src/logs")
    for log in logs:
        file = open("src/logs/" + log, "r")
        read = file.readlines()
        file.close()
        trainer_one = get_trainer_one(read)
        trainer_two = get_trainer_two(read)
        
        p = Path("src/trainers/" + trainer_one)
        try:
            p.mkdir()
        except FileExistsError as exc:
            pass

        p = Path("src/trainers/" + trainer_two)
        try:
            p.mkdir()
        except FileExistsError as exc:
            pass

### Find player 1
def get_trainer_one(read):
    name = ""
    for line in read:
        if line.find("|player|p1|") != -1:
            name = line.strip("|player")
            name = name.strip("1|")
    
    return(name)

### Find player 2
def get_trainer_two(read):
    name = ""
    for line in read:
        if line.find("|player|p2|") != -1:
            name = line.strip("|player")
            name = name.strip("2|")

    return(name)

## Create a file for each Pokemon in their folder
def get_pokemon():
    logs = os.listdir("src/logs")
    for log in logs:
        pass

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