import pandas as pd
import numpy as np
import smtplib
import matplotlib.pyplot as plt
from  sklearn.tree import DecisionTreeClassifier

def student_quality(choice,month,student_id,):
    dataframe=file_read(month)
    weak_ID=[]
    good_ID=[]
    for i in range(0,100):
        All_marks=get_marksAll(dataframe,student_id,student_id[i])
        #print(All_marks)
        A=All_Student_Performance(All_marks)
        #print(A)
        if(len(A[0])>len(A[1])):
            weak_ID.append(student_id[i])
        else:
            good_ID.append(student_id[i])
    if(choice==1):
        print("Weak Students are as follows:\n",weak_ID)
        return(weak_ID)
    elif(choice==2):
        print("Good Students are as follows:\n",good_ID)
        return(good_ID)

def smtp(E,choice):
    sender='asen75512@gmail.com'
    Email_ID=E
    receiver=Email_ID[1]
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()#identify computer
    mail.starttls()#transport layer security
    mail.ehlo()
    mail.login(sender,mail_password)
    header='To:'+receiver+'\n'+'From:'\
           +sender+'\n'+'subject:From: Student Managment Team \n'
    if(choice==1):
        msg="Your performance is not good in institute test in this month.increase your potential and do well\nThank you\n@Institute Student Management Head "
    elif(choice==2):
        msg="Your performance is good in institute test.keep your performance up,you will achive your target\nThank you\n@Institute Student Management Head"
    content=header+msg
    mail.sendmail(sender,receiver,content)
    mail.close()
    txt="Email Send successfully"
    return(txt)


def send_mail(student_ID,dataframe,choice):
    D=dataframe[2]
    Email_ID=[]
    for i in range(len(student_ID)):
        E=D[student_ID.index(student_ID[i])]
        Email_ID.append(E)
    print("you are in send mail()")
    txt=smtp(Email_ID,choice)
    print(txt)
        
    
    
def Admin_portal(student_id,dataframe):
    print("*************ADMIN PORTAL*************")
    AdminID=input("Enter Admin ID=")  #16CS07
    if(AdminID=='16CS07'):
        APassword=int(input("Enter Admin Password=")) #9999
        if(APassword==9999):
           pass
        else:
            print("somthing went wrong!,please enter correct password")

        print("\n************MENU**********")
        print("1.Total Number of Weak Student\n2.Total Number Of Good Student\n")
        choice=int(input("Enter Choice="))
        month=test_month()
        if(choice==1):
            weak_ID=student_quality(choice,month,student_id)
            mail=int(input("send mail?\n1.Yes\n2.No"))
            if(mail==1):
                send_mail(weak_ID,dataframe,choice)
            
        elif(choice==2):
            good_ID=student_quality(choice,month,student_id)
            mail=int(input("send mail?\n1.Yes\n2.No"))
            if(mail==1):
                send_mail(weak_ID,dataframe,choice)
        
        else:
            print("Wrong choice,please enter correct choice")
            

def Student_portal(student_id):
    print("*************STUDENT PORTAL*************")
    SID=input("Enter student ID=")
    r=SID in student_id
    if(r==True):
        return(SID)
    else:
        print("Wrong ID,Please Renter.")
    

def test_month():
    print("Select the test month..............")
    #print("1.january \n2.fabuary \n3.march \n4.april \n5.may \n6.jun \n7.july \n8.august \n9.septembar \n10.octobar \n11.novembar \n12.decembar")
    month_list=["january","fabuary","march","april","may","jun","july","august","septembar","octobar","novembar","decembar"]
    month=input()   #like january,fabuary,march,...
    r=month in month_list
    if( r==True):
        return(month)
    else:
        return(0)


def file_read(test_month):
    if(test_month=='january'):
        file=pd.read_csv(r"C:\Users\tech\Desktop\January.csv")
        data=np.array(file)
        df=pd.DataFrame(data)
        return(df)
    elif(test_month=='fabuary'):
        file=pd.read_csv(r"C:\Users\tech\Desktop\Fabuary.csv")
        data=np.array(file)
        df=pd.DataFrame(data)
        return(df)
        
        
    
def predict(marks_list):
    result=Trained.predict([marks_list])
    return(result)



def get_marks(Dataframe,student_id,SID,subject,i,j):
    row=student_id.index(SID)
    columns=Dataframe.iloc[6,i:j]
    arr=np.array(columns)
    marks=list(arr)
    return(marks)


def get_marksAll(Dataframe,student_id,SID):
    marks=[]
    for i in range(0,3):
        if(i==0):
            columns=Dataframe.iloc[student_id.index(SID),1:6]
            arr=np.array(columns)
            m=list(arr)
            #print(m)
            marks.append(m)
        elif(i==1):
            columns=Dataframe.iloc[student_id.index(SID),6:11]
            arr=np.array(columns)
            m=list(arr)
            #print(m)
            marks.append(m)
        elif(i==2):
            columns=Dataframe.iloc[student_id.index(SID),11:16]
            arr=np.array(columns)
            m=list(arr)
            #print(m)
            marks.append(m)
    #print(marks)
    return(marks)
                 
                 
def check_performance(p):
    if(p==1):
        print("Good Performace")
    elif(p==0):
        print("Bad performance")



def plotGraph(marks):
    X=["test1","test2","test3","test4","test5"]
    Y=marks
    plt.xlabel('test performed by student')
    plt.ylabel('Student Marks in test')
    plt.title('Student Progress Bar')
    plt.bar(X,Y,color='blue',width=0.4)
    plt.legend(shadow=True)
    test_name=["test1","test2","test3","test4","test5"]
    for i in range(5):
        plt.text( X[i],Y[i],test_name[i])
    plt.show()



def find_subject(sub,SID):
    if(sub==1):
        print("you selected -->Physics")
        subject="Physics"
        marks=get_marks(Dataframe,student_id,SID,subject,1,6)
        return(marks)
        

    elif(sub==2):
        print("you selected -->Chemestry")
        subject="Chemestry"
        marks=get_marks(Dataframe,student_id,SID,subject,6,11)
        return(marks)
        

    elif(sub==3):
        print("you selected -->Math")
        subject="Math"
        marks=get_marks(Dataframe,student_id,SID,subject,11,16)
        return(marks)
        

    elif(sub==4):
        marks=get_marksAll(Dataframe,student_id,SID)
        return(marks)
    else:
        print("please select subject as mentioned above...")

def All_Student_Performance( All_marks):
    for i in range(0,3):
        if(i==0):
            p=0
            for j in range(len(All_marks[i])):
                p=p+All_marks[0][j]
        elif(i==1):
            c=0
            for j in range(len(All_marks[i])):
                c=c+All_marks[0][j]
        if(i==2):
            m=0
            for j in range(len(All_marks[i])):
                m=m+All_marks[0][j]

    one=[]
    zero=[]
    A=[]
    if(p>250):
        one.append(p)
    else:
        zero.append(p)
    if(c>250):
        one.append(c)
    else:
        zero.append(c)
    if(m>250):
        one.append(m)
    else:
        zero.append(m)
    A.append(zero)
    A.append(one)
    return(A)

    

def All():
    All_marks=find_subject(sub,SID)
    print("Your marks in this month are as follows\n")
    print("Physics=",All_marks[0])
    print("Chemestry=",All_marks[1])
    print("Math=",All_marks[2])
    
    A=All_Student_Performance( All_marks)
    if(len(A[0])>len(A[1])):
        print("\nPoor Performance\n")
    else:
        print("\nGood Performance\n")
        
                
            
    p=int(input("Show Performance graph?\n1.YES\n2.No\n"))
    if(p==1):
        plt.figure(1)
        X=[1,2,3,4,5]
        plt.title('Student Progress Bar')
        
        plt.xlabel("Number of Test")
        plt.ylabel("Marks in Physics")
        plt.subplot(2,2,1)
        plt.plot(X,All_marks[2],color='red')
        #plt.bar(X,All_marks[0],color='blue',width=0.4)
        plt.legend(shadow=True)
        test_name=["test1","test2","test3","test4","test5"]
        for i in range(5):
            plt.text( X[i],All_marks[0][i],test_name[i])

        plt.xlabel("Number of Test")
        plt.ylabel("Marks in Chemestry")
        plt.subplot(2,2,2)
        plt.plot(X,All_marks[2],color='green')
        #plt.bar(X,All_marks[0],color='green',width=0.4)
        plt.legend(shadow=True)
        test_name=["test1","test2","test3","test4","test5"]
        for i in range(5):
            plt.text( X[i],All_marks[1][i],test_name[i])

        plt.xlabel("Number of Test")
        plt.ylabel("Marks in Math")
        plt.subplot(2,2,3)
        plt.plot(X,All_marks[2],color='blue')
        #plt.bar(X,All_marks[2],color='red',width=0.4)
        plt.legend(shadow=True)
        test_name=["test1","test2","test3","test4","test5"]
        for i in range(5):
            plt.text( X[i],All_marks[2][i],test_name[i])
        plt.show()

    else:
        print("**********************")



d=pd.read_csv(r"C:\Users\tech\Desktop\studentinfo12.csv")
data=np.array(d)
dataframe=pd.DataFrame(data)
b=dataframe[9]
c=list(b)
l=[]
for i in range(0,len(c)):
    l.append([c[i]])
    
student_id=dataframe[0]
student_id=list(student_id)

c=dataframe.iloc[:,4:9]
e=np.array(c)
f=list(e)
clf=DecisionTreeClassifier()
Trained=clf.fit(f,l)



print("********* STUDENT MARKS ANALYSIS**********")
print("\n****************************************************************************")
a=int(input("1.Admin\n2.Student\n"))
if(a==1):
    Admin_portal(student_id,dataframe)
   
elif(a==2):
    SID=Student_portal(student_id)
    test_month=test_month()
    if(test_month!=0):
        Dataframe=file_read(test_month)
        print("\n****************************************************************************")
        print("\nSubjects are...\n1.Physics\n2.Chemestry\n3.Math")
        sub=int(input("\nSelect the subject \nFor all subject press 4 other wise select subject number(1..3)\n "))
        if(sub==4):
            All()
        elif(sub!=4):
            marks=find_subject(sub,SID)
            print("Your marks in this month are as follows\n",marks)
            print("****************************************************************************")
            performance=predict(marks)
            #print("****************************************************************************")
            check_performance(performance)
            print("\n****************************************************************************")
            p=int(input("Show Performance graph?\n1.YES\n2.No\n"))
            if(p==1):
               plotGraph(marks)
            else:
                print("**********************")

else:
    print("you selected wrong month,please month as mentioned ...")





