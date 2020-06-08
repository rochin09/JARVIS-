    #Desktop Assistant

from gtts import gTTS 
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('save.mp3')
    os.system('mpg123 audio.mp3')

#listens to commands

def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '/n')

    #loop back to continue to listen for commands

    except sr.UnknownValueError:
        assistant(myCommand())

    return command

#if statements for executing commands
def assistant(command):

    if 'open Reddit python' in command:
        chrome_path = '/usr/bin/google-chrome'
        url = 'hrrps://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talkToMe('Chilling bro')

    if 'email' in command:
        talkToMe('Who is the recipient')
        recipient = myCommand()

        if 'John' in recipient:
            talkToMe('What should I say')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('PERSON NAME', 'emailaddress@whatever.com', content)

            #close connection
            mail.close()

            talkToMe('Email sent')

talkToMe('I am ready for your command, What is next')

while True:
    assistant(myCommand())
