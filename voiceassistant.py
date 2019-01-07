
import subprocess
from selenium import webdriver
import speech_recognition as sr
import psutil,os
import re
import webbrowser
import smtplib
import requests
from weather import Weather
import pyautogui
import time
import pyttsx3

engine = pyttsx3.init()

def talkMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

def utkCommands():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = utkCommands();

    return command


def utkvr(command):
    if 'navigate up' in command:
        pyautogui.moveRel(0, -100, duration=0.25)
        print('Done!')

    if 'tts' in command:
        saystuff = command.replace('tts ','')
        engine.say(saystuff)
        engine.runAndWait()

    if 'mouse position' in command:
        print(pyautogui.position())

    
    if 'navigate down' in command:
        pyautogui.moveRel(0, 100, duration=0.25)
        print('Done!')

    if 'niche' in command:
        pyautogui.moveRel(0, 100, duration=0.25)
        print('Done!')


    if 'navigate right' in command:
        pyautogui.moveRel(100, 0, duration=0.25)
        print('Done!')


    if 'navigate light' in command:
        pyautogui.moveRel(100, 0, duration=0.25)
        print('Done!')


    if 'navigate left' in command:
        pyautogui.moveRel(-100, 0, duration=0.25)
        print('Done!')

    if 'scroll up' in command:
        pyautogui.scroll(200) 
        print('Done!')

    if 'scroll down' in command:
        pyautogui.scroll(-200) 
        print('Done!')

    if 'type' in command:
        newt = command.replace('type ','')
        pyautogui.typewrite(newt) 
        print('Done!')
        
    if 'likho' in command:
        new = command.replace('likho ','')
        pyautogui.typewrite(new) 
        print('Done!')
        

    if 'eco' in command:
        new = command.replace('eco ','')
        pyautogui.typewrite(new) 
        print('Done!')
        
    if 'left click' in command:
        pyautogui.click() 
        print('Done!')

    if 'right click' in command:
        pyautogui.click(button='right') 
        print('Done!')

    if 'double click' in command:
        pyautogui.click()
        pyautogui.click()
        print('Done!')

    if 'open discord' in command:
        subprocess.Popen(r'C:\Users\utkarsh\AppData\Local\Discord\Update.exe --processStart Discord.exe')
        print('Done!')

    if 'shutdown computer' in command:
        subprocess.Popen(r'SHUTDOWN /s')
        print('Done!')

    if 'restart computer' in command:
        subprocess.Popen(r'SHUTDOWN /r')
        print('Done!')

    if 'open chrome' in command:
        subprocess.Popen(r'"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
        print('Done!')

    if 'open calculator' in command:
        subprocess.Popen(r'C:\Windows\system32\calc.exe')
        print('Done!')

    if 'app open' in command:
        cmd = command.replace('app open ' , '')
        subprocess.Popen(cmd + '.exe')
        print('Done!')

    if 'open command prompt' in command:
        subprocess.Popen(r'C:\Windows\system32\cmd.exe')
        print('Done!')

    if 'app close' in command:
        newtxt = command.replace('app close ','')
        for process in (process for process in psutil.process_iter() if process.name()==newtxt+ '.exe'):
          process.kill()
        print('Done!')

    if 'open notepad' in command:
        subprocess.Popen(r'C:\Program Files\Notepad++\notepad++.exe')
        print('Done!')

    if 'screen' in command:
        pyautogui.typewrite(['printscreen'])
        print('Done!')

    if 'applause' in command:
        newtxt = command.replace('app close ','')
        for process in (process for process in psutil.process_iter() if process.name()==newtxt+ '.exe'):
          process.kill()
        print('Done!')        

    if 'close command prompt' in command:
        for process in (process for process in psutil.process_iter() if process.name()=="cmd.exe"):
          process.kill()
        print('Done!')

    if 'close chrome' in command:
        for process in (process for process in psutil.process_iter() if process.name()=="chrome.exe"):
          process.kill()
        print('Done!')

    if 'close calculator' in command:
        for process in (process for process in psutil.process_iter() if process.name()=="calc.exe"):
          process.kill()
        print('Done!')

    if 'close notepad' in command:
        for process in (process for process in psutil.process_iter() if process.name()=="notepad++.exe"):
          process.kill()
        print('Done!')

    if 'close discord' in command:
        for process in (process for process in psutil.process_iter() if process.name()==r"Discord.exe"):
          process.kill()
        print('Done!')

    elif 'what\'s up' in command:
        talkMe('Just doing my thing')
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkMe(str(res.json()['joke']))
        else:
            talkMe('oops!I ran out of jokes')

    elif 'open explorer' in command:
        subprocess.Popen('explorer.exe')
        talkMe('What do you wanna see there?')
        recipient = utkCommands()

#note you should use primary documents command because secondary documents command
#will only work for me( I made it for personal use )
        if 'primary documents' in recipient:
            pyautogui.moveTo(91, 241)
            pyautogui.click()
        elif 'secondary documents' in recipient:
            pyautogui.moveTo(91, 241)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(603, 279)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(364, 196)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(303, 196)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(303, 196)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(303, 196)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(303, 196)
            pyautogui.click()
            pyautogui.click()
        elif 'computer' in recipient:
            pyautogui.moveTo(92, 382)
            pyautogui.click()
        elif 'desktop' in recipient:
            pyautogui.moveTo(91, 129)
            pyautogui.click()

#note you should use primary download command because secondary download command
#will only work for me( I made it for personal use )
        elif 'primary download' in recipient:
            pyautogui.moveTo(54, 159)
            pyautogui.click()
        elif 'secondary download' in recipient:
            pyautogui.moveTo(91, 241)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(603, 279)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(303, 196)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(303, 196)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(303, 196)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(303, 196)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(303, 196)
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(303, 196)
            pyautogui.click()
            pyautogui.click()
        elif 'videos' in recipient:
            pyautogui.moveTo(54, 288)
            pyautogui.click()
        else:
            return
    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    if 'open drive' in command:
        drv_ex = re.search('open drive (.*)', command)
        url = 'https://drive.google.com/drive/u/0/my-drive'
        webbrowser.open(url)
        print('Done!')


    if 'open facebook' in command:
        fb_ex = re.search('open facebook (.*)', command)
        url = 'https://www.facebook.com/'
        webbrowser.open(url)
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'current weather in' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            talkMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))

    elif 'weather forecast in' in command:
        reg_ex = re.search('weather forecast in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            forecasts = location.forecast()
            for i in range(0,3):
                talkMe('On %s will it %s. The maximum temperture will be %.1f degree.'
                         'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))


talkMe('I am ready for your command')

while True:
    nøøb Gamer(NGCommands())
