from tkinter import *
from khayyam import JalaliDate
import speech_recognition as sr
import urllib.request
import json 
from PIL import ImageTk, Image
from time import strftime, sleep
import threading
#from playsound import playsound
from pygame import mixer
import random 
import os 
import tkinter
from tkVideoPlayer import TkinterVideo
Path="D:/Research/Final Rakhshan/"

import os
#directories = [name for name in os.listdir(Path) if os.path.isdir(os.path.join(Path, name))]
#for dp in directories:
    #for filename in os.listdir(dp):
     #   if filename.startswith("._"):
      #      file_path = os.path.join(dp, filename)  
       #     os.remove(file_path)

#Recieving Weather Information
try:
    weatherAPIurl = 'https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=51.42&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=auto'
    with urllib.request.urlopen(weatherAPIurl) as url:
        data = json.loads(url.read().decode())
        weatherCode = data['daily']['weathercode'][0]
        weatherTemp = int((data['daily']['temperature_2m_max'][0]+data['daily']['temperature_2m_min'][0])/2)
        if weatherCode==0:
            weatherCondition = 'آسمون صافه'
            weatherCode=1
        elif weatherCode in [1,2,3]:
            weatherCondition = 'هوا ابریه'
            weatherCode=2
        elif weatherCode in [56, 57, 61, 63, 65, 66, 67, 80, 81, 82]:
            weatherCondition = 'بارون میاد'
            weatherCode=3
        elif weatherCode in [71, 73, 75, 77, 85, 86]:
            weatherCondition = 'برف میاد'
            weatherCode=4
        else:
            weatherCondition = 'هوا ابریه'
            weatherCode=2
        persiannums = ['۰','۱','۲','۳','۴','۵','۶','۷','۸', '۹']
        for i in range(0,10):
            weatherTemp = str(weatherTemp).replace(str(i),persiannums[i])
        weatherTemp+='°'
#If connection was not established
except:
    weatherTemp=None
    weatherCode=404
    weatherCondition='اینترنت قطعه'


root = Tk()
root.attributes("-fullscreen", True)
root.title('Rakhshan | IranDoc Smart Mirror')
root.configure(background='black')

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=5)
root.grid_rowconfigure(2, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=5)
root.grid_columnconfigure(2, weight=1)

frmweather = Frame(root,bd=1,background='black')
frmweather.grid(column=0, row=0,sticky='nsew')

frmtitle = Frame(root,bd=1,background='black')
frmtitle.grid(column=1, row=0,sticky='nsew')

frmclock = Frame(root,bd=1,background='black')
frmclock.grid(column=2, row=0,sticky='nsew')

frm4 = Frame(root,bd=1,background='black')
frm4.grid(column=0, row=1,sticky='nsew')

frmPrompt = Frame(root,bd=1,background='black')
frmPrompt.grid(column=1, row=1,sticky='nsew')

frm6 = Frame(root,bd=1,background='black')
frm6.grid(column=2, row=1,sticky='nsew')

frmLogo = Frame(root,bd=1,background='black')
frmLogo.grid(column=0, row=2,sticky='nsew')

frmNews = Frame(root,bd=1,background='black')
frmNews.grid(column=1, row=2, columnspan=2, sticky='nsew')

# frm9 = Frame(root,bd=1,background='yellow')
# frm9.grid(column=2, row=2,sticky='nsew')

 
def time():
    string = strftime('%H:%M')
    persiannums = ['۰','۱','۲','۳','۴','۵','۶','۷','۸', '۹']
    for i in range(0,10):
        string = string.replace(str(i),persiannums[i])
    labelclock.config(text=string)
    labelclock.after(500, time)
labelclock = Label(frmclock,font=('IRANSans UltraLight', 40), background='black', foreground='white', padx=30)
labeldate = Label(frmclock, text= JalaliDate.today().strftime('%A %D %B'), font=('IRANSans UltraLight', 15), background='black', foreground='white')

# lbl.grid(column=3, row=0,sticky='se')
labelclock.place(relx = 1.2,rely = -0.1,anchor ='ne')
labeldate.place(relx = 0.95,rely = 0.6,anchor ='ne')

labeltitle = Label(frmtitle,text='رخشان، آینه هوشمند',font=('IRANSans UltraLight', 15), background='black', foreground='white', padx=50)
labeltitle.place(relx = 0.5,rely = 0.2,anchor =CENTER)
time()



if(weatherCode==404):
    labelTemp = Label(frmweather,text=':(',font=('IRANSans UltraLight', 70), background='black', foreground='white', )
    labelweather = Label(frmweather,text=weatherCondition,font=('IRANSans UltraLight', 20), background='black', foreground='white')
    labelTemp.place(relx = 0.5,rely = -0.1 ,anchor ='n')
    labelweather.place(relx = 0.5,rely = 1,anchor ='s')
else:
    labelTemp = Label(frmweather,text=weatherTemp,font=('IRANSans UltraLight', 50), background='black', foreground='white', )
    labelweather = Label(frmweather,text=weatherCondition,font=('IRANSans UltraLight', 15), background='black', foreground='white')
    labelTemp.place(relx = 1,rely = 0.4 ,anchor ='e')
    labelweather.place(relx = 0.5,rely = 1,anchor ='s')
    weatherLogo = Image.open(Path+"weather/{}.png".format(weatherCode)).resize((60, 60), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(weatherLogo)
    labelweatherLogo = Label(frmweather, image=test,background='black')
    labelweatherLogo.image = test
    labelweatherLogo.place(relx = 0,rely = 0.4,anchor ='w')

labelPrompt = Label(frmPrompt,text='سلام! من رخشان هستم، یه آینه هوشمند! دوست داری بیشتر راجع بهم بدونی؟',font=('IRANSans Medium', 30), background='black', foreground='white',wraplength=1000)
labelPrompt.place(relx = 0.5,rely = 0.2,anchor =CENTER)

labelStat = Label(frm4,text='hi',font=('IRANSans UltraLight', 15), background='black', foreground='white',wraplength=1000)
labelStat.place(relx = 0.5,rely = 0.3,anchor =CENTER)

newsHeadlines =['هوش مصنوعی ماه گذشته میلادی ۴۰۰۰ نفر را در آمریکا بیکار کرده است',
 'دو توسعه‌دهنده از چت‌بات ساتوشی ناکاموتو، خالق بیت کوین رونمایی کردند',
 'هشدار رهبران صنعت هوش مصنوعی: این فناوری می‌تواند بشر را با خطر انقراض مواجه کند',
 'یک قاضی در آمریکا برای مقابله با هوش مصنوعی پیش‌نیاز جدیدی را جهت حضور در دادگاه معرفی کرد',
 'انویدیا با GPUهای خود هزینه آموزش مدل‌های زبانی بزرگ را ۲۵ برابر کاهش می‌دهد', 
 'توهمات دردسرساز ChatGPT؛ یک وکیل به‌خاطر استناد به دروغ‌های هوش مصنوعی به دادگاه می‌رود',
 'مدیرعامل سابق گوگل: هوش مصنوعی می‌تواند بسیاری از مردم را با خطر آسیب یا مرگ مواجه کند',
 'اسپیس ایکس در نظر دارد چهار موشک فالکون 9 به فضا پرتاب کند',
 'دستاورد محققان به رهبری دانشمند ایرانی؛ اولین انتقال بی‌سیم انرژی خورشیدی از فضا به زمین',
 'تراشه جدید سامسونگ با حسگر اثر انگشت امنیت کارت‌های بانکی را ارتقا می‌دهد',]

def showNews(i=0):
    labelNews.config(text='تازه های فناوری: '+newsHeadlines[i])
    if i==len(newsHeadlines)-1:
        i=-1
    labelNews.after(3500,lambda: showNews(i+1))
labelNews = Label(frmNews, text='تازه های فناوری:', font=('IRANSans UltraLight', 15), background='black', foreground='white', padx=10)
labelNews.place(relx = 1,rely = 1,anchor='se')
showNews()

iranDocLogo = Image.open(Path+"irandoclogo.png").resize((50, 50), Image.ANTIALIAS)
test = ImageTk.PhotoImage(iranDocLogo)
iranDocLogo = Label(frmLogo, image=test,background='black')
iranDocLogo.place(relx = 0,rely = 1,anchor ='sw')

    


state = False

#p = Process(target=lambda: playsound('notif.mp3'))

def mirrorPrompt(prompt_message,play_notif=True):
    labelPrompt.config(text=prompt_message)
    labelStat.config(text='')
    if play_notif:
        pass
        #playsound('D:/Research/Rakhshan/notif.mp3',block=FALSE)#p.start()


RecoIconFile = Image.open(Path+"RecognizeIcon.png")
RecoIconImage = ImageTk.PhotoImage(RecoIconFile.resize((40, int(RecoIconFile.size[1]*40/RecoIconFile.size[0]))))
ListenIconFile = Image.open(Path+"listenIcon.png")
ListenIconImage = ImageTk.PhotoImage(ListenIconFile.resize((40, int(ListenIconFile.size[1]*40/ListenIconFile.size[0]))))


def recognizer(phrase_time_limit=0):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        labelIconFile = Label(frm4, image = ListenIconImage,background='black')
        labelIconFile.place(relx=0.5, rely=0.3, anchor=CENTER)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        labelIconFile.destroy()
    try:
        labelIconFile = Label(frm4, image = RecoIconImage,background='black')
        labelIconFile.place(relx=0.5, rely=0.3, anchor=CENTER)
        query = r.recognize_google(audio, language ='fa-IR', show_all=False).encode('utf-8').decode("utf-8")
        labelIconFile.destroy()
        return(query)
    except Exception as e:
        #print(e)
        return(('Exception',e))








import cv2
import time

from deepface import DeepFace


#analyze emotion
def analyze_emotion(frame):
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    emotions = result[0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    return dominant_emotion

# Webcam activation and emotion analysis
cap = cv2.VideoCapture(1)

def facialExpression():
    start_time = time.time()
    emotions = []

    while True:
        ret, frame = cap.read()

        # Analyze emotion
        emotion = analyze_emotion(frame)
        emotions.append(emotion)

        if time.time() - start_time >= 2:
            break

    cap.release()
    #cv2.destroyAllWindows()

    # Calculate the average emotion
    emotion_counts = {}
    for emotion in emotions:
        emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1

    total_count = sum(emotion_counts.values())
    average_emotion = max(emotion_counts, key=lambda x: emotion_counts[x])

    # Calculate the weighted average based on counts
    for emotion in emotion_counts:
        emotion_counts[emotion] /= total_count

    average_emotion = max(emotion_counts, key=lambda x: emotion_counts[x])

    if average_emotion in ['happy', 'neutral', 'surprise']:
        return("happy")
    elif average_emotion in ['fear', 'disgust', 'angry', 'sad']:
        return("sad")

def speechrecogonizer():    
    global state
    global unrecognizedCounter 
    unrecognizedCounter = 0
    while True:
        labelStat.config(text='')
        query = recognizer()
        print(query)
        if type(query) == tuple:
            if state==False:        
                mirrorPrompt('!سلام! من رخشان هستم، یه آینه هوشمند',play_notif=False)    
            else:
                mirrorPrompt("نفهمیدم چی گفتی")   
                unrecognizedCounter+=1
                if unrecognizedCounter>=3:
                    state=False    
            continue
        else:
            state=True
            unrecognizedCounter = 0

            if('کتاب' in query): 
                mirrorPrompt('خب ، بیا اول با هم آشنا بشیم تا بتونم کتابهای بهتری رو بهت معرفی کنم. به خاطر همین چندتا سوال ازت میپرسم. ')
                sleep(5)
                mirrorPrompt('آماده ای؟')
                unrecognizedCounter=0
                while True:
                    query = recognizer()
                    if any(keyword in query for keyword in ['آماده','آره','بله']):
                        n=0
                        s=0
                        mirrorPrompt("""به تفسیر و تحلیل آثار خلاقانه علاقه مندی؟""")
                        unrecognizedCounter=0
                        while True:
                            query = recognizer()
                            if any(keyword in query for keyword in ['اول','یک','نه','علاقه چیه','۹','۱','1','9','ندارم','نیستم','خیر','اصلا']):
                                s+=1
                            elif any(keyword in query for keyword in ['آره','خیلی','زیاد','حتما','بله','قطعا']):
                                n+=1
                            if n+s>0:
                                mirrorPrompt('حالا بهم بگو آیا از رفتن به موزه های هنری لذت میبری؟')
                                unrecognizedCounter=0
                                while True:
                                    query = recognizer()
                                    if any(keyword in query for keyword in ['اول','یک','نه','علاقه چیه','۹','۱','1','9','ندارم','نیستم','خیر','اصلا']):
                                        s+=1
                                    elif any(keyword in query for keyword in ['آره','خیلی','زیاد','حتما','بله','قطعا','دارم']):
                                        n+=1
                                    if n+s>1:
                                        mirrorPrompt('حالا میخوام بدونم به مباحث تئوری علاقه مندی یا نه؟')
                                        unrecognizedCounter=0
                                        while True:
                                            query = recognizer()
                                            if any(keyword in query for keyword in ['اول','یک','نه','علاقه چیه','۹','۱','1','9','ندارم','نیستم','خیر','اصلا']):
                                                s+=1
                                            elif any(keyword in query for keyword in ['آره','خیلی','زیاد','حتما','بله','قطعا','دارم','علاقه دارم','علاقه مندم','هستم']):
                                                n+=1
                                            if n+s>2:
                                                mirrorPrompt('خب حالا بگو نقاشی سمت راست رو بیشتر میپسندی یا سمت چپ؟')
                                                imageFile1 = Image.open(Path+"bookrecommender/1.jpg")
                                                imageFile2 = Image.open(Path+"bookrecommender/2.jpg")
                                                img1 = ImageTk.PhotoImage(imageFile1.resize((200, int(imageFile1.size[1]*200/imageFile1.size[0]))))
                                                img2 = ImageTk.PhotoImage(imageFile2.resize((200, int(imageFile2.size[1]*200/imageFile2.size[0]))))
                                                label1 = Label(frmPrompt, image = img1)
                                                label1.place(relx=0.6, rely=0.9, anchor='sw')
                                                label2 = Label(frmPrompt, image = img2)
                                                label2.place(relx=0.4, rely=0.9,anchor='se')
                                                #sleep(1)
                                                unrecognizedCounter=0
                                                while True:
                                                    query = recognizer()
                                                    if any(keyword in query for keyword in ['راست','راستی','اول','یک','۱']):
                                                        s+=1
                                                    elif any(keyword in query for keyword in ['چپ','چپی','سمت چپ',]):
                                                        n+=1
                                                    if n+s>3:
                                                        label1.destroy()
                                                        label2.destroy()
                                                        mirrorPrompt('الان چطور سمت راست رو بیشتر دوست داری یا سمت چپ رو؟')
                                                        imageFile1 = Image.open(Path+"bookrecommender/3.jpg")
                                                        imageFile2 = Image.open(Path+"bookrecommender/4.jpg")
                                                        img1 = ImageTk.PhotoImage(imageFile1.resize((200, int(imageFile1.size[1]*200/imageFile1.size[0]))))
                                                        img2 = ImageTk.PhotoImage(imageFile2.resize((200, int(imageFile2.size[1]*200/imageFile2.size[0]))))
                                                        label1 = Label(frmPrompt, image = img1)
                                                        label1.place(relx=0.6, rely=0.9, anchor='sw')
                                                        label2 = Label(frmPrompt, image = img2)
                                                        label2.place(relx=0.4, rely=0.9,anchor='se')
                                                        #sleep(1)
                                                        unrecognizedCounter=0
                                                        while True:
                                                            query = recognizer()
                                                            if any(keyword in query for keyword in ['راست','راستی','اول','یک','۱']):
                                                                s+=1
                                                            elif any(keyword in query for keyword in ['چپ','چپی','سمت چپ',]):
                                                                n+=1
                                                            if n+s>4:
                                                                label1.destroy()
                                                                label2.destroy()
                                                                mirrorPrompt('خب حالا بگو نقاشی سمت راست رو بیشتر میپسندی یا سمت چپ؟')
                                                                imageFile1 = Image.open(Path+"bookrecommender/5.jpg")
                                                                imageFile2 = Image.open(Path+"bookrecommender/6.jpg")
                                                                img1 = ImageTk.PhotoImage(imageFile1.resize((200, int(imageFile1.size[1]*200/imageFile1.size[0]))))
                                                                img2 = ImageTk.PhotoImage(imageFile2.resize((200, int(imageFile2.size[1]*200/imageFile2.size[0]))))
                                                                label1 = Label(frmPrompt, image = img1)
                                                                label1.place(relx=0.6, rely=0.9, anchor='sw')
                                                                label2 = Label(frmPrompt, image = img2)
                                                                label2.place(relx=0.4, rely=0.9,anchor='se')
                                                                sleep(1)
                                                                unrecognizedCounter=0
                                                                while True:
                                                                    query = recognizer()
                                                                    if any(keyword in query for keyword in ['راست','راستی','اول','یک','۱']):
                                                                        s+=1
                                                                    elif any(keyword in query for keyword in ['چپ','چپی','سمت چپ',]):
                                                                        n+=1
                                                                    if n+s>5:
                                                                        label1.destroy()
                                                                        label2.destroy()
                                                                        if(n>s):
                                                                            bookAddress = random.choice(os.listdir(Path+'bookrecommender/N'))
                                                                            mirrorPrompt('من کتاب '+bookAddress[:-4]+' رو بهت پیشنهاد میدم دوست من')
                                                                            imageFile1 = Image.open(Path+"bookrecommender/N/"+bookAddress)
                                                                            img1 = ImageTk.PhotoImage(imageFile1.resize((250, int(imageFile1.size[1]*250/imageFile1.size[0]))))
                                                                            label1 = Label(frmPrompt, image = img1)
                                                                            label1.place(relx=0.5, rely=0.7, anchor=CENTER)                                                                            
                                                                        else:
                                                                            bookAddress = random.choice(os.listdir(Path+'bookrecommender/N'))
                                                                            mirrorPrompt('من کتاب '+bookAddress[:-4]+' رو بهت پیشنهاد میدم دوست من')
                                                                            imageFile1 = Image.open(Path+"bookrecommender/N/"+bookAddress)
                                                                            img1 = ImageTk.PhotoImage(imageFile1.resize((250, int(imageFile1.size[1]*250/imageFile1.size[0]))))
                                                                            label1 = Label(frmPrompt, image = img1)
                                                                            label1.place(relx=0.5, rely=0.7, anchor=CENTER)                                                                              
                                                                        sleep(10)
                                                                        label1.destroy()
                                                                        break
                                                                    else:
                                                                        unrecognizedCounter+=1
                                                                        if unrecognizedCounter>=3:
                                                                            break
                                                                        mirrorPrompt('ببخشید متوجه نشدم گفتی به کدوم بیشتر علاقه داری؟')
                                                                break    
                                                            else:
                                                                unrecognizedCounter+=1
                                                                if unrecognizedCounter>=3:
                                                                    break
                                                                mirrorPrompt('ببخشید متوجه نشدم گفتی به کدوم بیشتر علاقه داری؟')
                                                        break                                                        
                                                    else:
                                                        unrecognizedCounter+=1
                                                        if unrecognizedCounter>=3:
                                                            break
                                                        mirrorPrompt('ببخشید متوجه نشدم گفتی به کدوم بیشتر علاقه داری؟')
                                                break
                                            else:
                                                unrecognizedCounter+=1
                                                if unrecognizedCounter>=3:
                                                    break
                                                mirrorPrompt('ببخشید متوجه نشدم گفتی به مباحث تئوری علاقه مندی؟')
                                        break
                                    else:
                                        unrecognizedCounter+=1
                                        if unrecognizedCounter>=3:
                                            break
                                        mirrorPrompt('ببخشید متوجه نشدم گفتی از رفتن به موزه های هنری لذت میبری؟')
                                break
                            else:
                                unrecognizedCounter+=1
                                if unrecognizedCounter>=3:
                                    break
                                mirrorPrompt('ببخشید متوجه نشدم گفتی به تفسیر و تحلیل آثار خلاقانه علاقه مندی؟')
                        break
                    elif any(keyword in query for keyword in ['نه', 'نیستم', 'نمیخوام','برگرد','تمام','خیر','۹','9']):
                        break
                    else:
                        unrecognizedCounter+=1
                        if unrecognizedCounter>=3:
                            break
                        mirrorPrompt('ببخشید متوجه نشدم گفتی آماده ای؟')
                try:
                    label1.destroy()
                    label2.destroy()
                except:
                    pass
                mirrorPrompt('دیگه چه کاری میتونم برات انجام بدم؟')
            
           
            elif any(keyword in query for keyword in ['موسیقی','آهنگ','موزیک','موسیقی']):
                mirrorPrompt('من میتونم تو رو ببینم و بر اساس حس و حالت بهت موسیقی پیشنهاد بدم. بیا با هم امتحان کنیم.')
                sleep(3)
                mirrorPrompt('آماده ای؟')
                unrecognizedCounter=0
                while True:
                    query = recognizer()
                    if any(keyword in query for keyword in ['آماده','آره','بله']):
                        mirrorPrompt('لطفا چند لحظه صبر کن تا خوب نگاهت کنم')
                        unrecognizedCounter=0
                        while True:
                            facialExp = facialExpression()
                            if facialExp=='happy':
                                mirrorPrompt('به نظر سر حالی.')
                            elif facialExp=='sad':
                                mirrorPrompt('به نظر میاد خیلی رو به راه نیستی.')
                            if facialExp:
                                sleep(2)
                                mirrorPrompt('از بین ژانرهای کلاسیک، سنتی و پاپ کدوم رو بیشتر ترجیح میدی؟')
                                
                                unrecognizedCounter=0
                                continueTheLoop=True
                                while continueTheLoop:
                                    query = recognizer()
                                    if 'کلاسیک' in query:
                                        musicAddress = random.choice(os.listdir(Path+'music/classic/'+facialExp))
                                        mirrorPrompt('از گوش دادن به آهنگ '+musicAddress[:-4] +' لذت ببر')
                                        mixer.init() #Initialzing pyamge mixer
                                        mixer.music.load(Path+'music/classic/'+facialExp+'/'+musicAddress) #Loading Music File
                                        mixer.music.play() #Playing Music with Pygame
                                        
                                        play = True
                                        while(play==True):
                                            query = recognizer(phrase_time_limit=2)
                                            #mirrorPrompt(query)
                                            if any(keyword in query for keyword in ['بسه','کافیه','تمام','تموم','خداحافظ','خدانگهدار','خدا نگهدار','وایسا','نگهدار','توقف','خاموش',]):
                                                play = False
                                                mixer.music.stop()
                                                mirrorPrompt('توقف آهنگ')
                                                continueTheLoop=False 
                                    elif 'سنتی' in query:
                                        musicAddress = random.choice(os.listdir(Path+'music/traditional/'+facialExp))
                                        mirrorPrompt('از گوش دادن به آهنگ '+musicAddress[:-4] +' لذت ببر')
                                        mixer.init() #Initialzing pyamge mixer
                                        mixer.music.load(Path+'music/traditional/'+facialExp+'/'+musicAddress) #Loading Music File
                                        mixer.music.play() #Playing Music with Pygame #Playing Music with Pygame
                                        
                                        play = True
                                        while(play==True):
                                            query = recognizer(phrase_time_limit=2)
                                            #mirrorPrompt(query)
                                            if any(keyword in query for keyword in ['بسه','کافیه','تمام','تموم','خداحافظ','خدانگهدار','خدا نگهدار','وایسا','نگهدار','توقف','خاموش',]):
                                                play = False
                                                mixer.music.stop()
                                                mirrorPrompt('توقف آهنگ')
                                                continueTheLoop=False 
                                    
                                    elif 'پاپ' in query:
                                        musicAddress = random.choice(os.listdir(Path+'music/pop/'+facialExp))
                                        mirrorPrompt('از گوش دادن به آهنگ '+musicAddress[:-4] +' لذت ببر')
                                        mixer.init() #Initialzing pyamge mixer
                                        mixer.music.load(Path+'music/pop/'+facialExp+'/'+musicAddress) #Loading Music File
                                        mixer.music.play() #Playing Music with Pygame

                                        play = True
                                        while(play==True):
                                            query = recognizer(phrase_time_limit=2)
                                            #mirrorPrompt(query)
                                            if any(keyword in query for keyword in ['بسه','کافیه','تمام','تموم','خداحافظ','خدانگهدار','خدا نگهدار','وایسا','نگهدار','توقف','خاموش',]):
                                                play = False
                                                mixer.music.stop()
                                                mirrorPrompt('توقف آهنگ')   
                                                continueTheLoop=False 

                                    else:
                                        unrecognizedCounter+=1
                                        if unrecognizedCounter>=3:
                                            break
                                        mirrorPrompt('ببخشید متوجه نشدم گفتی کدوم ژانر رو دوست داری؟')
                                break
                            elif unrecognizedCounter==2:
                                mirrorPrompt('متاسفانه نمیتونم چهره ات رو تشخیص بدم. عوضش بهم بگو از بین ژانرهای کلاسیک، سنتی و پاپ کدوم رو انتخاب میکنی؟')
                                secondLoopContinue=True
                                secondLoopCount=0
                                while secondLoopContinue:
                                    query=recognizer()
                                    if 'کلاسیک' in query:
                                        secondLoopCount=10
                                        musicAddress = random.choice(os.listdir(Path+'music/classic/happy'))
                                        mirrorPrompt('از گوش دادن به آهنگ '+musicAddress[:-4] +' لذت ببر')
                                        mixer.init() #Initialzing pyamge mixer
                                        mixer.music.load(Path+'music/classic/happy/'+musicAddress) #Loading Music File
                                        mixer.music.play() #Playing Music with Pygame
                                        
                                        play = True
                                        while(play==True):
                                            query = recognizer(phrase_time_limit=2)
                                            #mirrorPrompt(query)
                                            if any(keyword in query for keyword in ['بسه','کافیه','تمام','تموم','خداحافظ','خدانگهدار','خدا نگهدار','وایسا','نگهدار','توقف','خاموش',]):
                                                play = False
                                                mixer.music.stop()
                                                mirrorPrompt('توقف آهنگ')
                                                secondLoopContinue=False
                                                unrecognizedCounter=4
                                            
                                        break
                                        
                                    elif 'پاپ' in query:
                                        secondLoopCount=10
                                        musicAddress = random.choice(os.listdir(Path+'music/pop/happy'))
                                        mirrorPrompt('از گوش دادن به آهنگ '+musicAddress[:-4] +' لذت ببر')
                                        mixer.init() #Initialzing pyamge mixer
                                        mixer.music.load(mixer.music.load(Path+'music/pop/happy/'+musicAddress)) #Loading Music File
                                        mixer.music.play() #Playing Music with Pygame

                                        play = True
                                        while(play==True):
                                            query = recognizer(phrase_time_limit=2)
                                            #mirrorPrompt(query)
                                            if any(keyword in query for keyword in ['بسه','کافیه','تمام','تموم','خداحافظ','خدانگهدار','خدا نگهدار','وایسا','نگهدار','توقف','خاموش',]):
                                                play = False
                                                mixer.music.stop()
                                                mirrorPrompt('توقف آهنگ')
                                                secondLoopContinue=False
                                                unrecognizedCounter=4
                                        break

                                    elif 'سنتی' in query:
                                        secondLoopCount=10
                                        musicAddress = random.choice(os.listdir(Path+'music/traditional/happy'))
                                        mirrorPrompt('از گوش دادن به آهنگ '+musicAddress[:-4] +' لذت ببر')
                                        mixer.init() #Initialzing pyamge mixer
                                        mixer.music.load(mixer.music.load(Path+'music/traditional/happy/'+musicAddress)) #Loading Music File
                                        mixer.music.play() #Playing Music with Pygame
                                        
                                        play = True
                                        while(play==True):
                                            query = recognizer(phrase_time_limit=1)
                                            if any(keyword in query for keyword in ['بسه','کافیه','تمام','تموم','خداحافظ','خدانگهدار','خدا نگهدار','وایسا','نگهدار','توقف','خاموش',]):
                                                play = False
                                                mixer.music.stop()
                                                mirrorPrompt('توقف آهنگ')
                                                secondLoopContinue=False
                                                unrecognizedCounter=4
                                        break
                                    else: 
                                        mirrorPrompt('ببخشید متوجه حرفت نشدم گفتی چه ژانری رو دوست داری؟')
                                        secondLoopCount+=1
                                        if secondLoopContinue>=3:
                                            secondLoopContinue = False
                                            break
                                    break

                            else:
                                unrecognizedCounter+=1
                                if unrecognizedCounter>=3:
                                    break
                                mirrorPrompt('ببخشید نمیتونم خوب ببینمت لطفا تو فاصله مناسب ازم بایست')
                        break
                    elif any(keyword in query for keyword in ['نه', 'نیستم', 'نمیخوام','برگرد','تمام','خیر','۹','9']):
                        break
                    else:
                        unrecognizedCounter+=1
                        if unrecognizedCounter>=3:
                            break
                        mirrorPrompt('ببخشید متوجه نشدم گفتی آماده ای؟')
                try:
                    label1.destroy()
                    label2.destroy()
                except:
                    pass
                mirrorPrompt('دیگه چه کاری میتونم برات انجام بدم؟')             
            elif any(keyword in query for keyword in ['کلیپ','ویدیو','ویدئو','فیلم']):
                videoplayer = TkinterVideo(master=frmPrompt, scaled=True)
                if random.random()<0.5:
                    mirrorPrompt('کلیپ معرفی پژوهشگاه')
                    videoplayer.load(Path+"irandoc.mp4")
                    videoplayer.place(relx=0.5, rely=0.7, anchor=CENTER,width=654,height=367)
                    mixer.init() #Initialzing pyamge mixer
                    mixer.music.load(Path+'irandoc.mp3') #Loading Music File
                    mixer.music.play() #Playing Music with Pygame
                else:
                    mirrorPrompt('پخش کلیپ درباره هوش مصنوعی')
                    videoplayer.load(Path+"AIclip.mp4")
                    videoplayer.place(relx=0.5, rely=0.7, anchor=CENTER,width=654,height=367)
                    mixer.init() #Initialzing pyamge mixer
                    mixer.music.load(Path+'AIclip.mp3') #Loading Music File
                    mixer.music.play() #Playing Music with Pygame
                videoplayer.play() # play the video

                
                play = True
                while(play==True):
                    query = recognizer(phrase_time_limit=2)
                    #mirrorPrompt(query)
                    if any(keyword in query for keyword in ['بسه','کافیه','تمام','تموم','خداحافظ','خدانگهدار','خدا نگهدار','وایسا','نگهدار','توقف','خاموش',]):
                        play = False
                        mixer.music.stop()
                        videoplayer.destroy()
                        mirrorPrompt('دیگه چه کاری میتونم برات انجام بدم؟')    
            if('خوبی' in query):
                mirrorPrompt("قربونت ممنونم")
            
            elif('سلام' in query):
                mirrorPrompt('حالت چطوره؟')
                query = recognizer()
                mirrorPrompt('من میتونم کارهای زیادی برات انجام بدم. مثلا برات آهنگ یا ویدیو پخش کنم یا بهت کتاب معرفی کنم. ')

            ################################################


            ################################################

            elif any(keyword in query for keyword in ['موسیقی','آهنگ','موزیک','موسیقی']):
                mirrorPrompt('من میتونم تو رو ببینم و بر اساس حس و حالت بهت موسیقی پیشنهاد بدم. آماده ای یه امتحانی بکنیم؟')
                sleep(3)
                mirrorPrompt('')
                query = recognizer()
                if 'کلاسیک' in query:
                    mirrorPrompt('از گوش دادن به آهنگ بهار از آنتونیو ویوالدی لذت ببر')
                    mixer.init() #Initialzing pyamge mixer
                    mixer.music.load(Path+'vivaldi_spring.mp3') #Loading Music File
                    mixer.music.play() #Playing Music with Pygame
                    
                    play = True
                    while(play==True):
                        query = recognizer(phrase_time_limit=2)
                        #mirrorPrompt(query)
                        if any(keyword in query for keyword in ['بسه','کافیه','تمام','تموم','خداحافظ','خدانگهدار','خدا نگهدار','وایسا','نگهدار','توقف','خاموش',]):
                            play = False
                            mixer.music.stop()
                            mirrorPrompt('توقف آهنگ')
                    
                elif 'پاپ' in query:
                    mirrorPrompt('پاپ کی گوش میده بابا؟')

                elif 'سنتی' in query:
                    mirrorPrompt('از گوش دادن به آهنگ وطن از همایون شجریان لذت ببر')
                    mixer.init() #Initialzing pyamge mixer
                    mixer.music.load(Path+'VatanHomayoun.mp3') #Loading Music File
                    mixer.music.play() #Playing Music with Pygame
                    
                    play = True
                    while(play==True):
                        query = recognizer(phrase_time_limit=1)
                        if any(keyword in query for keyword in ['بسه','کافیه','تمام','تموم','خداحافظ','خدانگهدار','خدا نگهدار','وایسا','نگهدار','توقف','خاموش',]):
                            play = False
                            mixer.music.stop()
                            mirrorPrompt('توقف آهنگ')
                else: 
                    mirrorPrompt('ببخشید متوجه حرفت نشدم')

            elif any(keyword in query for keyword in ['تمام','تموم','خداحافظ','خدانگهدار','خدا نگهدار']):
                mirrorPrompt('خدانگهدار')
                state = False
            else:
                unrecognizedCounter+=1
                if(unrecognizedCounter>=3):
                    state= False
                    mirrorPrompt('!سلام! من رخشان هستم، یه آینه هوشمند',play_notif=False)

        


thread1 = threading.Thread(target=speechrecogonizer, daemon=True)

thread1.start()
mainloop()