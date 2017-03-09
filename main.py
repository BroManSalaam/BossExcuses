import smtplib
import time
import datetime
import math
import random

def getInput(msg):
        inpt = input(msg + " ")
        return inpt


# sends an email to a specified target

def sendEmail(excuse):
        # enter your account credentials
        gmail_user = 'yourusername@email.com'  
        gmail_password = ''

        sender = gmail_user  
        # recipiant of the email
        to = ['yourboss@gmail.com']  
        subject = 'I cannot make it to work today...'  
        # use a  \n to create a new line
        body = excuse

        email_text = """\  
        sender: %s  
        To: %s  
        Subject: %s

        %s
        """ % (sender, ", ".join(to), subject, body)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sender, to, email_text)
        server.close()

        print ('Email sent!')

def getExcuse():
        
        #put your excuses in here
        excuses = [
                'Youre not the boss of me',
                'I hate this job',
                'Ive fallen and I cant get up'
        ] 
        rand = random.randint(0, len(excuses)-1)
        return excuses[rand]

# this is the hour and minute that you wake up at and (hopefully) end this alarm
wake_hour = 7
wake_min = 0

# amount of time the program waits before it sends your boss an email can be set to a negative
sleepTime = 0

now = datetime.datetime.today()
alarm = datetime.datetime(now.year, now.month , now.day + 1, wake_hour, wake_min, 0)
delta = now - alarm

print ('wecome to pyMail early alpha. a python 3.6 script that emails your boss with a message made by you if you do not end your alarm!')
print('press ctr + c at any time to end the program, or take a hammer to it')

if getInput("is this your first time using this script?[y/n]") == 'y':
        print('we will need to collect some data then...')
        wake_hour = getInput("what is the hour of the day you regularly wake at?[hr]")
        wake_min = getInput("what are minutes following that hour?[min]")
        sleepTime = getInput("If we were to reach your alarm time, how much 'fudge room' do you want following that alarm time before an email is sent?[min]")
        print("Youre now ready to begin, be careful!")
        print(' ')
else:
        print("Youre now ready to begin, be careful!")

print('starting script...')

print('now: ', now)
print('alarm ', alarm)
print('delta ', delta)
print ("")
print('you have', math.ceil(delta.seconds / 3600 * 100) / 100 , 'hours to slumber...enjoy it while you can...')

while now < alarm:
        # update every 2 mins
        time.sleep(120)

        now = datetime.datetime.today()

        # 10 mins past alarm
        if( (now + now.minute + 10) > alarm):
                try:
                        sendEmail(getExcuse)
                        print("slept a little too late last night huh? no worries, your boss has recieved the message")
                        break
                except smtplib.SMTPException:
                        print("uh oh, you couldnt send an excuse to your boss!")

        print('2 mins passed... zzzzz')

