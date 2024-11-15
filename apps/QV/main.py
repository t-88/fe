import os
from time import gmtime, strftime

DB_PATH =f"{os.path.expanduser('~')}/.config/fe"
SAVE_PATH = "vim-tmps"

sufix_file_name = strftime("%Y-%m-%d-%H:%M:%S", gmtime())
file_name = f"{DB_PATH}/{sufix_file_name}" 


if not os.path.exists(file_name):
    os.mkdir(file_name)

if not os.path.exists(file_name):
    os.mkdir(file_name)


s.open
