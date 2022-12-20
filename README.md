# PlateUp Save Manager

This script allows you to save and load games in the PlateUp game on your computer. It also provides the ability to list all saved games.

## Prerequisites
- Python 3.x
- The PlateUp game installed on your computer

## Installing
1. Download or clone the repository to your local machine
2. Navigate to the root directory of the project in your terminal

## Usage
The script can be executed with the following command: 
  python main.py [subcommand] [arguments]

### Subcommands
- `save`: Saves the current game
- `load`: Loads a saved game
- `list`: Lists all saved games

### Arguments
- `--name`: The name of the game to be saved or loaded
- `--path`: The path to the PlateUp data folder. This is usually `C:/Users/%USER%/AppData/LocalLow/It's Happening/PlateUp` on Windows systems. If not provided, the script will try to detect the default path based on your system information.

### Examples
Saving a game: 
  
    python plateup_save.py save MyGame

Loading a saved game:
        
    python plateup_save.py load MyGame

Listing all saved games:

    python plateup_save.py list
    
Using a custom path: 

    python plateup_save.py save MyGame --path /path/to/PlateUp/folder 




