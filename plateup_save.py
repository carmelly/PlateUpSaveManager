import os
import sys
import shutil
import argparse

def main():

    global path
    global current_game 
    global save_path 

    args = parse_args()

    # exit if path is missing or invalid 
    if args.path is None: 
        sys.exit('Couldn\'t detect default path from system info. Please provide a path for your PlateUp data folder. In Windows this is usually C:/Users/%USER%/AppData/LocalLow/It\'s Happening/PlateUp')
    elif not os.path.exists(args.path): 
        sys.exit(f'Folder does not exist at {args.path}. Please provide a path for your PlateUp data folder. In Windows this is usually C:/Users/%USER%/AppData/LocalLow/It\'s Happening/PlateUp')

    # set save folder paths 
    path = args.path
    current_game =  f'{path}/Full'
    save_path = f'{path}/Saves'
    
    # execute subcommand
    if args.subcommand == 'save':
        game = args.name
        save_game(game)   
    elif args.subcommand == 'load':
        game = args.name
        load_game(game)
    elif args.subcommand == 'list': 
        list_games()

def save_game(game):
    dst = f'{save_path}/{game}/'
    # check if the game is already saved
    if os.path.exists(dst):
        # ask the user if they want to overwrite the existing game
        overwrite = input(f'{game} is already saved. Do you want to overwrite it? (y/n) ')
        if overwrite.lower() == 'y':
            # Overwrite the existing save
            shutil.rmtree(dst)
            shutil.copytree(current_game, dst)
            print(f'{game} saved successfully')
        else:
            print(f'Save cancelled')
    else:
        # copy the game folder to the save path
        shutil.copytree(current_game, dst)
        print(f'{game} has been saved')

def load_game(game):
    src = f'{save_path}/{game}/'
    
    # Check if the game folder already contains a saved game
    if os.path.exists(current_game) and len(os.listdir(current_game)) != 0:
        # Ask the user if they want to save the current game before loading a new one
        save_current = input('You have game in progress. Do you want to save it before loading a new game? (y/n) ')
        if save_current.lower() == 'y':
            # Get the name for the save file
            save_name = input('Enter a name for the save file: ')
            # Save the current game
            save_game(save_name)

    # Delete the current game folder
    shutil.rmtree(current_game)

    # Load the game from the specified save folder
    shutil.copytree(src, current_game)
    print('Game loaded successfully.')

def list_games(): 
    # Get a list of the files and subfolders in the specified folder
    entries = os.listdir(save_path)

    # Filter the list to include only the subfolders
    subfolders = [entry for entry in entries if os.path.isdir(os.path.join(save_path, entry))]

    # Print the list of subfolders
    print ('Existing saved games:')
    for folder in subfolders: 
        print(f' * {folder}')

def get_default_path(): 
    import getpass
    import platform

     # Get the current user
    current_user = getpass.getuser()

    # Get the system information
    system_info = platform.uname()
    # Detect operating system
    if system_info.system == 'Windows': 
        return f"C:/Users/{current_user}/AppData/LocalLow/It's Happening/PlateUp"

    # Check if the operating system is Linux and the machine type is 'x86_64' (indicating that it is running in WSL)
    elif system_info.system == 'Linux' and system_info.machine == 'x86_64':
        return  f"/mnt/c/Users/{current_user}/AppData/LocalLow/It's Happening/PlateUp"
    else:
        # System not recognized
        return None 

def parse_args(): 
       
    parser = argparse.ArgumentParser()

    default_path = get_default_path()
    parser.add_argument('-p', '--path', help=f'PlateUp data path (default {default_path})', default=default_path) 
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')

    parser_save =  subparsers.add_parser('save', help='save the current game')
    parser_save.add_argument('name', help='name for the new save')

    parser_load =  subparsers.add_parser('load', help='load a saved game')
    parser_load.add_argument('name', help='name of save file to load')

    parser_list = subparsers.add_parser('list', help='print a list of saved games')

    return parser.parse_args()

if __name__ == "__main__":
    main()

