import smtplib
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="election"
)
mycursor=mydb.cursor()
count=0
bjp=[]
congress=[]
namelist=[]
def insert_data():
    sql="insert into vote1 (voter_id,name,email_id,age,candidate) values (%s,%s,%s,%s,%s)"
    voter_id=input("enter your voter id :")
    name=input("enter your name :")
    email_id=input("enter your email id :")
    age=int(input("enter your age :"))
    candidate=input(f"enter you want to vote :")
    val=(voter_id,name,email_id,age,candidate)
    mycursor.execute(sql,val)
    mydb.commit()
    print("......data saved successfully.......")
receiver_mailid=[]
def email_sending():
    try:
        email_id=input("enter your email id :")
        receiver_mailid.append(email_id)
        for i in receiver_mailid:
            s=smtplib.SMTP('SMTP.gmail.com',587)
            s.starttls()
            s.login("rasipriya959@gmail.com","iwei saxw umzo ojxt")
            message=("***thanks for voting***")
            s.sendmail("rasipriya959@gmail.com",i,message)
            s.quit()
            print("mail sent successfully")
    except:
        print("mail not sent")
def main():
    print("1.BJP 2.CONGRESS ")
    candidates_people=["bjp","congress"]
    people=input("enter you want to vote :")
    name=input("enter your name :")
    if people in candidates_people:
        print("thank you for come to vote here ")
        if people=="bjp":
            insert_data()
            namelist.append(name)
            bjp.append(name)
            print("bjp voted:",bjp)
            print("who are all voted names:",namelist)
            print("thanks for voting")
            email_sending()
            print("next person can vote please come front...")
            main()
        elif people=="congress":
            insert_data()
            namelist.append(name)
            congress.append(name)
            print("congress voted:",congress)
            print("who are all voted names:",namelist)
            print("thanks for voting")
            email_sending()
            print("next person can vote please come front....")
            main()
    else:
        print(f"{people} is not a candidate")
main()