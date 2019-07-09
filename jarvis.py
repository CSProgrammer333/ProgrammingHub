import speech_recognition as sr
import time, datetime, os
import face_recognition
import cv2, csv
import requests
import re
import pyttsx3
import dlib
#from googlesearch import search
import webbrowser as wb
import requests, json
import wikipedia

global word
def txt_to_speech(data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()
print('ready')
txt_to_speech("I am ready")
t = datetime.datetime.now()
r = sr.Recognizer()
r.energy_threshold = 2100
a=[]
b=[]
c=[]
v=[]
image = []
face_encoding = []
sir_face_encoding = []
x = 0
index =0
count=0

print("running.....")

#default face can remove it
##my_image = face_recognition.load_image_file(r'G:\arpit photo\akshay.jpg')
##my_face_encoding = face_recognition.face_encodings(my_image)[0]
##known_face_encodings = [my_face_encoding]
##known_face_names = ["akshay"]

with open(r"C:\Users\tech\AppData\Local\Programs\Python\Python36\admin.csv",'r') as new_file:
    csv_reader= csv.reader(new_file)
    for line in csv_reader:
        if len(line)!=0 :
            a.append(line[0])
            b.append(line[1])
            x=x+1
for i in range(0,x):
        image.append(face_recognition.load_image_file(b[i]))
        sir_face_encoding.append(face_recognition.face_encodings(image[i])[0])            

known_face_encodings =sir_face_encoding
known_face_names = a
face_locations = []
face_encodings = []
face_names = []
txt_to_speech("I am ready")
word=''
global flag
        
f=open(r"test.txt", "a+")

def cam():
            
    try:    
        video_capture = cv2.VideoCapture(0)
        print('camera')
        ret, frame = video_capture.read(0)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if True:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                abc = "hello "+ name 
                face_names.append(name)
                if name not in v and name != "Unknown": 
                    v.append(name)
                    txt_to_speech(abc)
                elif name =="Unknown":
                    txt_to_speech("May I know your name")
                    xa=speechrecognizer()

                    if xa=='':
                        print("please speak your name again")
                        xa=speechrecognizer()
                                
                    img_name ="Ajay pic_1.jpg"
                    cv2.imwrite(img_name, frame)
                    myData = [xa,img_name]
                    with open(r"C:\Users\tech\AppData\Local\Programs\Python\Python36\admin.csv",'a') as csv_file:
                        csv_append = csv.writer(csv_file)
                        csv_append.writerow(myData)
                            

                    print("Writing complete")
                    my_image = face_recognition.load_image_file(img_name)
                    my_face_encoding = face_recognition.face_encodings(my_image)[0]
                    known_face_encodings.append(my_face_encoding)
                    known_face_names.append(xa)
                    ab = "hello "+ xa + 'done'
                    txt_to_speech(ab)
                    name=xa
                            
        xa=''
        video_capture.release()
        cv2.destroyAllWindows()
        return name        
    except :
        print("Couldn't identify the face . PUT your face in front of camera")
        mainfunc()

def speechrecognizer():
    global word
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source,duration=1)        
            audio = r.listen(source , timeout=1)
        except:
            print("timed out ,Speak again")
            audio = r.listen(source)
            
    try:
        word = r.recognize_google(audio,language='en-IN')
        print("You said: " + word)
    except sr.UnknownValueError:
        word =''
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))     
    word=word.lower()
    return word

def conversation(user_name):
    flag=0
    while (flag!=1):
        word=''
        print('Please say something')
        txt_to_speech("Please say something")
        word = speechrecognizer()
        f.write("\n" +user_name+ " : " + word +"\n")
        if "hello" in  word or "hi jarvis" in word or "hey jarvis" in word:
            d = "Hello"
            print("Jarvis : ",d)
            txt_to_speech(d)
        elif "manufacturer" in  word or"manufacturers" in  word and "name" in word:
            d = "Ms. Aditi khandel "
            print("Jarvis : ",d)
            txt_to_speech(d)
        
        elif "search from google" in word or "google for me" in word:
            txt_to_speech("what to search")
            print("what to search")
            word2=speechrecognizer()
            for d in search(word2, tld="co.in", num=10, stop=10, pause=2):
                print(d)
                txt_to_speech(d)

        elif "location" in word:
            g = geocoder.ip('me')
            lat=g.latlng
            str1= "latitude position is "+str(lat[0])
            str2= "longitude position is "+str(lat[1])
            print("Jarvis: ",str1)
            print("Jarvis: ",str2)
            d= str1 +str2
            txt_to_speech(str1)
            txt_to_speech(str2)
            
        elif "weather" in  word or "temperature" in  word:
            txt_to_speech("Tell your city")
            city_name=speechrecognizer()
            print("city you said is",city_name)
            #city_name=input("enter city name to confirm")
            api_key = "cca979ed5fb2c8d3a9c99594191482f9"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
            json_data=requests.get(complete_url).json()
            try:
                temp=json_data['main']
                temp=str(int(int(temp['temp'])-273.15))
                temp1=json_data['weather'][0]['description']
                d =" Current Temperature in "+city_name+" is "+temp+" degree celsius with "+temp1
                print("Jarvis : ",d)
                txt_to_speech(d)
            except KeyError:
                print("Key invalid or city not found")
        elif "time" in  word:
            tttt=time.ctime()
            d=str(tttt[11:19])
            print("Jarvis : ",d)
            txt_to_speech(d)
        elif "date" in  word:
            tttt=time.ctime()
            d=tttt[4:11]+tttt[20:24]
            print("Jarvis : ",d)
            txt_to_speech(d)
        elif "day" in  word:
            tttt=time.ctime()
            day=tttt[0:3]
            di={'Mon':'Monday','Tue':'Tuesday','Wed':'Wednesday','Thu':'Thursday','Fri':'Friday','Sat':'Saturday','Sun':'Sunday'}
            d=di[day]
            print("Jarvis : ",d)
            txt_to_speech(day)
        elif "doing" in  word or "doing here" in  word:
            d = "I am here to help you"
            print("Jarvis : ",d)
            txt_to_speech(d)
        elif "how are you" in  word:
            d = "I am fine."
            print("Jarvis : ",d)
            txt_to_speech(d)
        elif " open youtube for me" in word or "youtube" in word:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chrome_path).open('youtube.com')
            d="opened you tube for you in chrome"
            txt_to_speech(d)
        elif "your" in  word and "name" in word:
            d = "I am Jarvis"
            print("Jarvis : ",d)
            txt_to_speech(d)
        elif "about yourself" in  word or "who are you" in word:
            d = "I am Jarvis and I am your virtual assistant bassed on Artificial Intelligence."
            print("Jarvis : ",d)
            txt_to_speech(d)
        elif "what is machine learning" in  word or "about machine learning" in word:
            d = "I am only possible because of machine learning. Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves. "
            print("Jarvis : ",d)
            txt_to_speech(d)
        elif "wikipedia" in word:
            txt_to_speech("what you want to search on wikipedia")
            se=speechrecognizer()
            d=wikipedia.summary(se, sentences=2)
            print("Jarvis :" ,d)
            txt_to_speech(d)
                             
        elif word == '':
            d = "Sorry couldn't recognize try again" 
            print("Jarvis : Sorry couldn't recognize try again",d)
            
        elif "thank you" in  word or "thanks" in  word:
            d = "You're welcome. I am just doing my job"
            print("Jarvis : ",d)
            txt_to_speech(d)
            f.write("*****************************************************")
            flag=1
        else :
            d = "I am not trained for this."
            txt_to_speech(d)
       
        f.write("Jarvis : " +d +"\n")
    f.close()

def mainfunc():
    try:
        user_name=cam() 
        conversation(user_name)
    except:
        mainfunc()

mainfunc()
    
        
    
    
