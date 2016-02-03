import os
import config

def clear_screen():
    os.system('cls' if config.OS == 'Windows' else 'clear')
