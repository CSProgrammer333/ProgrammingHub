import pandas as pd
import cv2
import numpy as np
import face_recognition as fc
import random
import datetime
import smtplib
import xlsxwriter
v=cv2.VideoCapture(0)

df=pd.read_csv(r"C:\Users\tech\Desktop\MY Projects\BIO Metric Attendence\image_path.csv")
#print(df)
image=np.array(df)
img_path=image[:,1]
#print(img_path)
img_path_list=list(img_path)
#print(img_path)


img_encoding=[]
fd=cv2.CascadeClassifier(r"C:/Users/tech/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
for j in range(0,3):
    link=img_path_list[j]
    i=fc.load_image_file(img_path_list[j])
    fl=fc.face_locations(i)
    fe=fc.face_encodings(i,fl)[0]
    img_encoding.append(fe)
#print(img_encoding)

d1=pd.read_csv(r'C:\Users\tech\Desktop\MY Projects\BIO Metric Attendence\Database.csv')
#print(d1)
data1=np.array(d1)
c=pd.DataFrame(data1)
#print(c)
knowfcnm=list(c[1])
#print(knowfcnm)
email=list(c[3])
#print(email)
knowfc=[img_encoding]
face_locations=[]
face_encodings=[]
face_names=[]
presentlist=[]
currenttime=[]
def smtp1(em):
    sender='asen75512@gmail.com'
    receiver=em
    #print(receiver)
    p=str(random.randint(1000,9999))
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()#identify computer
    mail.starttls()#transport layer security
    mail.ehlo()
    mail.login(sender,'9001ajay')
    header='To:'+receiver+'\n'+'From:'\
           +sender+'\n'+'subject:Your OTP is \n'
    content=header+p
    mail.sendmail(sender,receiver,content)
    otp=input("enter your otp for attandance:")
    if(otp==p):
        presentlist.append("P")
        d=datetime.datetime.now()
        print("Successfully marked attendence,thank you.......")
        #d1=d.strftime("%I:%M:%S %P")
        currenttime.append(d)
    else:
        print("Incorrect OTP,please try again,thank you......")
    mail.close()

process_this_frame=True
while(True):
    ret,frame=v.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=small_frame[:,:,::-1]
    if(process_this_frame):
        face_locations=fc.face_locations(rgb_small_frame)
        face_encodings=fc.face_encodings(rgb_small_frame,face_locations)
        face_names=[]
        for face_encoding in face_encodings:
            matches=fc.compare_faces(img_encoding,face_encoding)
            name="unknown"
            if(True in matches):
                first_match_index=matches.index(True)
                name=knowfcnm[first_match_index]
            face_distances=fc.face_distance(img_encoding,face_encoding)
            best_match_index=np.argmin(face_distances)
            if(matches[best_match_index]):
                name=knowfcnm[best_match_index]
                em=email[best_match_index]
                #print(em)
            face_names.append(name)
    process_this_frame=not process_this_frame
    for(top,right,bottom,left),name in zip(face_locations,face_names):
        top*=4
        right*=4
        bottom*=4
        left*=4
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,0,255),cv2.FILLED)
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,'hello'+name,(left+6,bottom-6),font,1.0,(255,255,255),1)
        #cv2.putText(frame,'your otp is send mail',(left+8,bottom-8),font,1.0,(255,255,255),1)
    cv2.imshow('video',frame)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        break

#print(em)
print("Looking nice...\n")
smtp1(em)
print(presentlist)
print(currenttime)
A=pd.DataFrame({"NAME":name,"P/A": presentlist,"Time": currenttime})
excel_writer=pd.ExcelWriter(r'C:\Users\tech\Desktop\MY Projects\BIO Metric Attendence\attendence_mark.xlsx',engine='xlsxwriter')
A.to_excel(excel_writer,'studentinfo')
excel_writer.save()


cv2.destroyAllWindows()
#cv2.release()        
        

        

    
