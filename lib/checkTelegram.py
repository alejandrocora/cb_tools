import getpass
from os.path import exists

def checkTelegram():
    return exists('/home/'+getpass.getuser()+'/.config/telegram-send.conf')
