'''
What I can do:
    - Hello
    - Goodbye
    - Math (+,-,*,/)
    - Check date and time
    - Start a timer (minutes/seconds)
    - Start a stopwatch
    - Check weather status
    - Pick a random number
    - Open Google, Google Drive, Google Hangouts, Google Meets, Google Earth, Google Translate
    - Open Youtube, GitHub, Facebook, Messenger
    - Search locations
    - Find current location
    - Search Google, Youtube
    - Shutdown/Restart laptop
    - Translate (10 languages)
    - Check Coronavirus status (VN)
    - Unable features
'''

import selenium
from selenium import webdriver
import speech_recognition
import pyttsx3
from datetime import datetime, date
from googletrans import Translator
import time
from time import sleep
import random
import webbrowser
import re
import requests
from pprint import pprint
import pyperclip
import os
import geocoder
import json

with open('config.json') as file:
    config = json.load(file)

bot_name = "Sonlove"

user_name = "You"

speak = pyttsx3.init()

listen = speech_recognition.Recognizer()

clear = lambda: os.system('clear')


greetings = ["Hello, I am {} - your virtual assistant. What can I help you with? ".format(bot_name),
            "I am your virtual assistant - {}. How can I help you?".format(bot_name),
            "Hey there, I'm {} - your virtual assistant. Do you need any help?".format(bot_name)]

processor = random.choice(greetings)


def remove_position(res,pos):

    res = res.split(" ")
    res.remove(res[pos])
    res = " ".join(res)

    return res


def remove_index(res, key):

    res = res.split(" ")
    for i in range(len(res)):
        if res[i] == key:

            return " ".join(res[i+1:])


def remove_element(res, key):

    res = res.split(" ")
    for elem in res:
        if elem == key:
            res.remove(elem)

    res = " ".join(res)

    return res


def check_string(s,res):

    for elem in res:

        if elem in res:
            return True
    

def synonyms(syn, res):

    res = res.split(" ")
    check = any(elem in syn for elem in res)
    
    if check is True:
            return True

    else:
        return False


def hello():
    
    now = datetime.today()
    now = now.strftime("%H")
    now = int(now)

    if now >= 0 and now <= 12: 
        return "Good morning!"

    elif now > 12 and now <= 17: 
        return "Good afternoon!"
        
    elif now > 17: 
        return "Good evening!"


def goodbye():

    end = ["Until we speak again.",
               "Hope to see you soon",
               "Nice talking with you, bye for now",
               "Ok. See you again",
               "Take care ..."]

    processor = random.choice(end)

    print()

    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()


def my_name():

    intros = ["My name is {}. Do you think it's a nice name?".format(bot_name),
                 "I was named after this laptop, {}".format(bot_name),
                 "{} is my name. How about yours?".format(bot_name)]

    processor = random.choice(intros)
    
    return processor


def your_name(name):

    compliments = ["That's a nice name {}".format(name.capitalize()),
                 "Very nice name {}".format(name.capitalize()),
                 "One of the best names I've ever heard, {}".format(name.capitalize())]

    processor = random.choice(compliments)
    
    return processor


def welcome():

    welcome = ["You're welcome",
               "I'll do my best for you",
               "No problems",
               "Anything to make you happy",
               "Your sastisfaction is my pleasure"]

    processor = random.choice(welcome)

    return processor


def ability():
    abilities = ["Here is what I can do:",
                 "- Say hello and goodbye",
                 "- Do easy math",
                 "- Check date and time",
                 "- Start a timer",
                 "- Start a stopwatch",
                 "- Check the weather status",
                 "- Pick a random number",
                 "- Open Google, Google Drive, Google Hangouts, Google Meets, Google Earth, Google Translate, Youtube, GitHub, Facebook, Messenger",
                 "- Search any locations",
                 "- Find current locations",
                 "- Search something on Google, Youtube",
                 "- Shutdown/Restart laptop",
                 "- Translate (10 languages)"
                 ]

    processor = "\n".join(abilities)
    return processor


def today():

    today = datetime.today()
    processor = today.strftime("%B %d, %Y")

    return processor


def blank():

    empty = ["I can't hear you, try again",
            "Go ahead. I'm listening",
            "I'm sorry I can't hear you. Can you please repeat?",
            "Pardon me. I didn't catch that. Could you try it again?",
            "I didn't quite hear you, try again",
            "Please speak louder, I can barely hear you from here"]

    processor = random.choice(empty)

    return processor


def addition():

    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 + num2

        print()
        print(num1,'+',num2,'=',answer)
        print()

        processor = "{} plus {} is {}".format(num1,num2,answer)

    except Exception:

        processor = "Sorry I didn't catch that. Can you please repeat?"

    return processor


def subtraction():

    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 - num2

        print()
        print(num1,'-',num2,'=',answer)
        print()

        processor = "{} minus {} is {}".format(num1,num2,answer)

    except Exception:

        processor = "Sorry I didn't catch that. Can you please repeat?"

    return processor


def multiplication():

    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 * num2

        print()
        print(num1,'*',num2,'=',answer)
        print()

        processor = "{} multiplied by {} is {}".format(num1,num2,answer)

    except Exception:

        processor = "Sorry I didn't catch that. Can you please repeat?"

    return processor


def division():

    digits = [int(x) for x in result.split() if x.isdigit()]

    try:
        
        num1 = digits[0]
        num2 = digits[1]

        answer = num1 / num2

        print()
        print(num1,'/',num2,'=',answer)
        print()

        processor = "{} divided by {} is {}".format(num1,num2,answer)

    except Exception:

        processor = "Sorry I didn't catch that. Can you please repeat?"

    return processor


def time():

    now = datetime.today()
    time_period = now.strftime("%H")
    time_period = int(time_period)

    if time_period < 12:
        processor = now.strftime("%H AM %M minutes %S seconds")

    else:
        processor = now.strftime("%H PM %M minutes %S seconds")

    return processor


def timer_seconds():

    limit = re.search("\d+", result)

    limit = int(limit[0])
    processor = "Ok. {} seconds and counting.".format(limit)

    print()
    
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    for i in range(limit,-1,-1):

        print("0:{:02d}".format(limit))
        sleep(1)
        limit -= 1

        if limit == 0:

            while True:
                try:

                    processor = "TIME'S UP!"
                    print(f"{bot_name}: {processor}")
                    speak.say(processor)
                    speak.runAndWait()
                    sleep(0.5)

                except KeyboardInterrupt:

                    break


def timer_minutes():

    limit = re.search("\d+", result)

    limit = int(limit[0])
    processor = "Got it. {} minutes and counting.".format(limit) 

    print()

    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()
    sec = 0

    for i in range (limit*60):

        print("{}:{:02d}".format(limit,sec))
        sleep(1)
        sec -= 1

        if sec < 0:
            limit -= 1
            sec = 59
            
        if limit == 0 and sec == 0:

            while True:
                try:
                    processor = "TIME'S UP!"
                    print(f"{bot_name}: {processor}")
                    speak.say(processor)
                    speak.runAndWait()
                    sleep(0.5)

                except KeyboardInterrupt:

                    break


def stopwatch():

    start_time = time.time()
    last_time = start_time
    lap = 1

    processor = "Stopwatch is ready. Press ENTER to begin and Ctrl + C to quit."
    speak.say(processor)
    speak.runAndWait()

    try:

        while True:

            input()

            lap_time = round(time.time()-last_time,2)
            total_time = round(time.time()-start_time,2)

            print(f"Lap #{lap}: {total_time} {lap_time}")
            last_time = time.time()

            processor = "Lap {} recorded".format(lap)
            speak.say(processor)
            speak.runAndWait()

            lap += 1

    except KeyboardInterrupt:

        processor = "Done."
        speak.say(processor)
        speak.runAndWait()


def random_number(res):

    num = [int(x) for x in res.split(" ") if x.isdigit()]

    num1 = num[0]

    num2 = num[1]

    pick = random.randint(num1,num2)

    rd = ["That would be {}".format(pick),
          "The answer is {}".format(pick),
          "It's {}".format(pick)]

    processor = random.choice(rd)

    return processor


def shutdown():

    print()

    processor = "Shutting down laptop. Are you sure?"

    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    with speech_recognition.Microphone() as source:

        print()

        print("Listening ...")

        print()

        audio = listen.record(source=source, duration=5)
    
    try:

        result = ""
        result = listen.recognize_google(audio)
        result = result.lower()

        print(f"{user_name}: {result}")
    
    except Exception: 

        pass

    if "yes" in result or "please" in result:

        processor = "System poweroff. See you again"

        print()

        print(f"{bot_name}: {processor}")
        speak.say(processor)
        speak.runAndWait()

        sleep(3)

        if config['device_OS'] == 'linux':

            os.system('systemctl poweroff')

        elif config['device_OS'] == 'window':

            os.system('shutdown -s')
        
        elif config['device_OS'] == 'mac':

            os.system('sudo shutdown -r now')

    else:

        processor = "Shutting down process canceled"

        print()

        print(f"{bot_name}: {processor}")
        speak.say(processor)
        speak.runAndWait()

        sleep(3)


def restart():

    print()

    processor = "Rebooting down laptop. Are you sure?"

    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    with speech_recognition.Microphone() as source:

        print()

        print("Listening ...")

        print()

        audio = listen.record(source=source, duration=5)
    
    try:

        result = ""
        result = listen.recognize_google(audio)
        result = result.lower()

        print(f"{user_name}: {result}")
    
    except Exception: 

        pass

    if "yes" in result or "please" in result:

        processor = "Rebooting laptop."

        print()

        print(f"{bot_name}: {processor}")
        speak.say(processor)
        speak.runAndWait()

        sleep(3)

        if config['device_OS'] == 'linux':

            os.system('systemctl reboot -i')

        elif config['device_OS'] == 'window':

            os.system('shutdown -r')
        
        elif config['device_OS'] == 'mac':

            os.system('sudo halt')

    else:

        processor = "Rebooting process canceled"

        print()

        print(f"{bot_name}: {processor}")
        speak.say(processor)
        speak.runAndWait()

        sleep(3)


def translator(result):

    languages_pack = ["vietnamese","french","german","italian","spanish","russian","japanese",
                          "korean","malaysian","chinese"]

    result = result.split(" ")

    dest = result[-1]

    if dest not in languages_pack:

        processor = "Translate to what?"

        return processor

    result.remove("translate")

    result.remove(result[-1])

    if result[-1] == "into" or result[-1] == "to":
        
        result.remove(result[-1])

    translator = Translator()

    result = " ".join(result)

    if dest == "vietnamese":

        sub = translator.translate(result,dest="vi")

    elif dest == "french":

        sub = translator.translate(result,dest="fr")

    elif dest == "german":

        sub = translator.translate(result,dest="de")

    elif dest == "italian":

        sub = translator.translate(result,dest="it")
    
    elif dest == "russian":

        sub = translator.translate(result,dest="ru")

    elif dest == "spanish":

        sub = translator.translate(result,dest="es")

    elif dest == "japanese":

        sub = translator.translate(result,dest="ja")

    elif dest == "korean":

        sub = translator.translate(result,dest="ko")

    elif dest == "malaysian":

        sub = translator.translate(result,dest="ms")

    elif dest == "chinese":

        sub = translator.translate(result,dest="zh-CN")
    
    print()
    print("Result: "+sub.text)
    print()

    processor = "{} in {} is {}".format(result,dest.capitalize(),sub.text)
    return processor


def maps(res):

    key = ["where","direction","way","map","locate","location"]

    for elem in key:

        while elem in res:

            res = remove_index(res=res, key=elem)

    rm = ["to","the","is","of"]

    for elem in rm:

        while elem in res:

            res = remove_index(res=res,key=elem)

    processor = "Here is the location of the {}".format(res)

    print()

    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()
    
    webbrowser.open('https://www.google.com/maps/place/'+res)


def current_location():

    print()

    g = geocoder.ip('me')
    processor = "You are currently at {}, {}".format(g.city, g.country)

    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()


def weather():

    city = "vietnam"

    print()

    try:

        query='q='+city;
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
        w_data=res.json();

        processor = "Here is the weather forecast for today"
        print(f"{bot_name}: {processor}")
        speak.say(processor)
        speak.runAndWait()

        print()
        print("Temperature: {}°C ".format(w_data['main']['temp']))
        processor = "Temperature: {} Celsius ".format(w_data['main']['temp'])
        speak.say(processor)
        speak.runAndWait()

        print("Wind speed: {} m/s".format(w_data['wind']['speed']))
        processor = "Wind speed: {} meters per second".format(w_data['wind']['speed'])
        speak.say(processor)
        speak.runAndWait()

        print("Description: {}".format(w_data['weather'][0]['description']))
        processor = "Description: {}".format(w_data['weather'][0]['description'])
        speak.say(processor)
        speak.runAndWait()

        print("Weather: {}".format(w_data['weather'][0]['main']))
        processor = "Weather: {}".format(w_data['weather'][0]['main'])
        speak.say(processor)
        speak.runAndWait()

        if "rain" in result:

            print()

            if "rain" in w_data['weather'][0]['description']:
                processor = "Looks like it's raining at the moment. Remember to stay warm"
                print(f"{bot_name}: {processor}")
                speak.say(processor)
                speak.runAndWait()

            else:
                processor = "Looks like it's not raining at the moment."
                print(f"{bot_name}: {processor}")
                speak.say(processor)
                speak.runAndWait()
        
    except:

        processor = "Sorry but I'm unable to display weather data at the moment"
        print()
        print(f"{bot_name}: {processor}")
        speak.say(processor)
        speak.runAndWait()

def open_google():

    processor = "Opening Google ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://www.google.com")


def open_google_drive():
    
    processor = "Opening Google Drive ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://drive.google.com/")


def open_google_translate():

    processor = "Opening Google Translate ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://translate.google.com/")


def open_google_meet():

    processor = "Opening Google Meet ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://meet.google.com/") 


def open_google_hangouts():

    processor = "Opening Google Hangouts ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://hangouts.google.com/")


def open_google_earth():

    processor = "Opening Google Earth ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://earth.google.com/")


def search_google(key):

    processor = "Finding {} on Google.".format(key)
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("http://www.google.com/search?q="+key)


def open_youtube():

    processor = "Opening Youtube ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://www.youtube.com")


def search_youtube(key):

    processor = "Finding {} on Youtube".format(key)
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open('https://www.youtube.com/results?search_query='+key)


def open_messenger():

    processor = "Opening Messenger ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://www.messenger.com/")


def open_facebook():

    processor = "Opening Facebook ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://www.facebook.com/")


def open_gmail():

    processor = "Opening Gmail ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://mail.google.com/")


def open_github():

    processor = "Opening GitHub ..."
    print()
    print(f"{bot_name}: {processor}")
    speak.say(processor)
    speak.runAndWait()

    webbrowser.open("https://github.com/")


def unable():

    unable = ["Sorry but I haven't been programmed for this feature",
                  "I'm sorry. I afraid I can't do that",
                  "Sorry but that is beyond my limits",
                  "I'm sorry. This feature has not been programmed yet",
                  "I'm not sure I understand."]

    processor = random.choice(unable)

    return processor



while True:

    with speech_recognition.Microphone() as source:

        print(f"{bot_name}: {processor}")
        speak.say(processor)
        speak.runAndWait()

        print()

        print("Listening ...")

        print()

        audio = listen.record(source=source, duration=5)     
        # audio = listen.listen(source=mic,duration=7)
        # audio = listen.adjust_for_ambient_noise(source=mic, duration=7)

    try:

        result = ""
        result = listen.recognize_google(audio)
        # result = listen.recognize_bing(audio, key="BING_KEY")
        result = result.lower()

        print(f"{user_name}: {result}")
        
    except Exception:
        
        pass


    if result == "":

        processor = blank()


    elif synonyms(syn=["hello","hi","hey"],res=result):

        processor = hello()


    elif "name" in result:

        if "your" in result:

            processor = my_name()
    
        elif "my" in result:

            result = remove_index(res=result,key="name")

            result = remove_element(res=result,key="is")

            processor = your_name(name=result)

    
    elif synonyms(syn=["thank","thanks"],res=result):

        processor = welcome()


    elif synonyms(syn=["time","clock"],res=result):
    
        processor = time()


    elif synonyms(syn=["weather","forecast","raining","rain"],res=result):
        
        processor = weather()

        break


    elif synonyms(syn=["today","date"],res=result):
    
        processor = today()


    elif "what can you do" in result:

        processor = ability()


    elif "translate" in result:
    
        processor = translator(result=result)


    elif "+" in result:
    
        processor = addition()


    elif "-" in result:

        processor = subtraction()


    elif "*" in result:
    
        processor = multiplication()


    elif "/" in result:
    
        processor = division()


    elif "stopwatch" in result:

        stopwatch()

        break


    elif "set" and "timer" in result:

        limit = re.search("\d+", result)
    
        if not limit:

            processor = "Set a timer for how long?" 

            continue

        if "seconds" in result:
    
            timer_seconds()

            break

        if "minutes" in result:

            timer_minutes()

            break

    
    elif "random" and "number" in result:

        processor = random_number(res=result)

    elif result == "where am i" or "current location" in result:

        current_location()

        break


    elif synonyms(syn=["where","direction","way","map","locate","location"],res=result):

        maps(res=result)

        break


    elif synonyms(syn=["search","find","browse","look"],res=result):

        result = remove_position(res=result,pos=0)

        if "google" in result:

            result = remove_element(res=result, key="google")

            result = remove_element(res=result, key="on")

            while synonyms(syn=["for"],res=result):

                result = remove_element(res=result,key="for")

            if result == []:

                open_google()

                break
                
            else:

                search_google(key = result)
                
                break

        elif "youtube" in result:

            result = remove_element(res=result,key="youtube")

            result = remove_element(res=result,key="on")

            while synonyms(syn=["for"],res=result):

                result = remove_element(res=result, key="for")

            if result == []:

                open_youtube()

                break

            else:

                search_youtube(key = result)

                break
        
        else:

            result = result.split(" ")

            while "for" in result:

                result = " ".join(result)
    
                result = remove_index(res=result,key="for")

            search_google(key=result)

            break

    
    elif synonyms(syn="open",res=result):
        
        if "messenger" in result:

            open_messenger()

            break

        elif "facebook" in result:

            open_facebook()

            break

        elif "gmail" in  result:

            open_gmail()
            
            break

        elif "github" in result:

            open_github()

            break

        elif "google" in result:

            if "drive" in result:

                open_google_drive()

            elif "translate" in result:

                open_google_translate()

            elif "meet" in result:

                open_google_meet()

            elif "hangouts" in result:

                open_google_hangouts()

            elif "earth" in result:

                open_google_earth()

            else:

                open_google()

            break

        elif "youtube" in result:

            open_youtube()

            break

    elif synonyms(syn=["what","why","when","where","how"],res=result):

        search_google(key=result)

        break
    
    elif synonyms(syn=["goodbye","bye","away"],res=result) or "see you" in result:
        
        goodbye()

        break

    
    elif "shut down" in result or "power off" in result:

        shutdown()

    
    elif "restart" in result or "reboot" in result:

        restart()

            
    else:

        processor = unable()
    


