import os
from time import gmtime, strftime
import datetime

DB_PATH =f"{os.path.expanduser('~')}/.config/fe"
SAVE_PATH = "vim-tmps"
DIR_PATH = f"{DB_PATH}/{SAVE_PATH}"

sufix_file_name =  datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S') 
file_name = f"{DIR_PATH}/{sufix_file_name}" 


if not os.path.exists(DIR_PATH):
    os.mkdir(DIR_PATH)

with open(file_name,"w"):
    pass


os.system("vim " + file_name)

