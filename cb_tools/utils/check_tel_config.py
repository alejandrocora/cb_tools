import getpass
from os.path import exists

def check_tel_config():
    if getpass.getuser() != 'root':
        return exists('/home/'+getpass.getuser()+'/.config/telegram-send.conf')
    else:
        return exists('/'+getpass.getuser()+'/.config/telegram-send.conf')
