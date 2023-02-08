import os
import shutil
import bs4
from pathlib import Path

def main():
    folder_setup()
    get_battle_logs()
    get_trainers()
    get_pokemon()
    get_nicknames()
    clean_nicknames()
    get_stats()




# Setup folders
def folder_setup():
        clean_folders()
        create_logs_dir()
        create_trainers_dir()
        create_resources_dir()

## Deletes logs and trainers folder so they can be filled with new logs
def clean_folders():
    try:
        shutil.rmtree("src/logs")
    except OSError as e:
        pass

    try:
        shutil.rmtree("src/trainers")
    except OSError as exc:
        pass

    try:
        shutil.rmtree("src/resources")
    except OSError as exc:
        pass

## Create logs directory to store battle logs in
def create_logs_dir():
    p = Path("src/logs")
    try:
        p.mkdir()
    except FileExistsError as exc:
        pass

## Create trainers directory to store Pokemon information in
def create_trainers_dir():
    p = Path("src/trainers")
    try:
        p.mkdir()
    except FileExistsError as exc:
        pass

## Create resources directory
def create_resources_dir():
    p = Path("src/resources")
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
            index = name.index('|')
            name = name[0:index]
    
    return(name)

### Find player 2
def get_trainer_two(read):
    name = ""
    for line in read:
        if line.find("|player|p2|") != -1:
            name = line.strip("|player")
            name = name.strip("2|")
            index = name.index('|')
            name = name[0:index]

    return(name)

## Create a file for each Pokemon in their folder
def get_pokemon():
    logs = os.listdir("src/logs")
    for log in logs:
        file = open("src/logs/" + log, "r")
        read = file.readlines()
        file.close()
        trainer_one_pokemon(read)
        trainer_two_pokemon(read)

### Find trainer ones team
def trainer_one_pokemon(read):
    for line in read:
        name = get_trainer_one(read)

        if line.find("|poke|p1|") != -1:
            line = line.strip("|poke|p1|")
            if line.find("|"):
                line = line.replace("|","")
            if line.find(", F"):
                line = line.replace(", F","")
            if line.find(", M"):
                line = line.replace(", M","")

            try:
                file = open("src/trainers/" + name + "/" + line, "x")
                file.write("Stats\n")
            except:
                pass


### Find trainer twos team
def trainer_two_pokemon(read):
    for line in read:
        name = get_trainer_two(read)

        if line.find("|poke|p2|") != -1:
            line = line.strip("|poke|p2|")
            if line.find("|"):
                line = line.replace("|","")
            if line.find(", F"):
                line = line.replace(", F","")
            if line.find(", M"):
                line = line.replace(", M","")

            try:
                file = open("src/trainers/" + name + "/" + line, "x")
                file.write("Stats\n")
            except:
                pass

## Store following data in each Pokemons file
def get_stats():
    get_number_of_battles()
    get_number_of_kills()
    get_number_of_deaths()

### Number of battles fought
def get_number_of_battles():
    logs = os.listdir("src/logs")
    for log in logs:
        file = open("src/logs/" + log, "r")
        read = file.readlines()
        file.close()
        get_trainer_one_team_counters(read)
        get_trainer_two_team_counters(read)

#### Calculate number of times each Pokemon was brought to a battle for trainer one
def get_trainer_one_team_counters(read):
    for line in read:
        name = get_trainer_one(read)

        if line.find("|poke|p1|") != -1:
            line = line.strip("|poke|p1|")
            if line.find("|"):
                line = line.replace("|","")
            if line.find(", F"):
                line = line.replace(", F","")
            if line.find(", M"):
                line = line.replace(", M","")
            pokemon = line
            store_battle_counter(pokemon, name)

#### Calculate number of times each Pokemon was brought to a battle for trainer one
def get_trainer_two_team_counters(read):
    for line in read:
        name = get_trainer_two(read)

        if line.find("|poke|p2|") != -1:
            line = line.strip("|poke|p2|")
            if line.find("|"):
                line = line.replace("|","")
            if line.find(", F"):
                line = line.replace(", F","")
            if line.find(", M"):
                line = line.replace(", M","")
            pokemon = line
            store_battle_counter(pokemon, name)

##### Store new battle counter value in file
def store_battle_counter(pokemon, name):
    file = open("src/trainers/" + name + "/" + pokemon, "r")
    read = file.read()
    file.close()
    write_file = open("src/trainers/" + name + "/" + pokemon, "w")
    if read.find("battles:") == -1:
        write_file.write("battles: 1\n")
    else:
        battle_num = get_old_battle_num(read)
        battle_num = battle_num + 1
        write_file.write("battles: " + str(battle_num) + "\n")
    write_file.close()

##### Get previous battle counter value from file
def get_old_battle_num(read):
    old_battle_num = read.split("battles: ")[1]
    old_battle_num = int(old_battle_num)
    return old_battle_num

### Number of kills
def get_number_of_kills():
    pass

### Number of deaths
def get_number_of_deaths():
    pokemon = ""
    logs = os.listdir("src/logs")
    for log in logs:
        file = open("src/logs/" + log, "r")
        read = file.readlines()
        file.close()
        for line in read:
            if line.find("|faint|") != -1:
                if line.find("p1"):
                    line = line.replace("|faint|p1a:","")
                if line.find("p2"):
                    line = line.replace("|faint|p2a:","")
                pokemon = check_nicknames(line)
                print(pokemon)

### Number of times each move was used
def get_times_of_move_use():
    pass

### Number of times each item was brought to battle
def get_times_of_item_present():
    pass

### Number of times each ability was brought to battle
def get_times_of_ability_present():
    pass

### Highest Damage Move in each game
def get_highest_damage_move():
    pass




# Compare data collected to determine winner of these categories
## League Wide
### Most kills
### Most deaths
### Most devastating move
### Brought to most amount of fights
## Per Pokemon
### Brought to {num} battles
### Most used item
### Most used move
### Most used ability





# Get pokemon nicknames
def get_nicknames():
    name_set = ""
    index = 0
    logs = os.listdir("src/logs")
    for log in logs:
        file = open("src/logs/" + log, "r")
        read = file.readlines()
        file.close()
        for line in read:
            if line.find("|switch|") != -1:
                if line.find("p1a"):
                    line = line.replace("|switch|p1a: ","")
                if line.find("p2a"):
                    line = line.replace("|switch|p2a: ","")

                if line.find(",") != -1:
                    index = line.find(",")
                    line = line[0:index]
                line = line.split("|")
                nickname = line[0]
                name = line[1]
                name_set = nickname + "," + name
                try:
                    nicknames_file = open("src/resources/nicknames.txt.pre", "x")
                    nicknames_file.close()
                except FileExistsError as exc:
                    pass
                nicknames_file = open("src/resources/nicknames.txt.pre", "a")
                nicknames_file.writelines(name_set + "\n")

## Clean nicknames
def clean_nicknames():
    output_file = open("src/resources/nicknames.txt", "w")
    input_file = open("src/resources/nicknames.txt.pre", "r")
    lines_seen = set()
    for line in input_file:
        if line not in lines_seen:
            output_file.write(line)
            lines_seen.add(line)
    input_file.close()
    output_file.close()

## Compare pokemon name to nicknames
def check_nicknames(old_name):
    pokemon = ""
    file = open("src/resources/nicknames.txt", "r")
    read = file.readlines()
    file.close()
    for i in read:
        if i.find(old_name):
            index = i.index(",")
            pokemon = i[index+1:len(i)]
            return(pokemon)
            




# Save results to "results.txt"





# Execute code
main()