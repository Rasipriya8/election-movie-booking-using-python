import mysql.connector
import smtplib
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="booking"
)
mycursor=mydb.cursor()
def email_msg(email,total):
    try:
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login("rasipriya959@gmail.com","iwei saxw umzo ojxt")
        msg=(f"thank you for choosing priya cinemas\n your total amount is {total}\n your seat is conformed")
        s.sendmail("rasipriya959@gmail.com",email,msg)
        s.quit()
        print("email sent successfully")
    except:
        print("email not sent successfully")
amt=0
gst=0
total=0
def main():
    print("\t\t__________________PRIYA CINEMAS_____________________")
    print("the running movies in our thetre\nARANMANAI 4\n KARUDAN\n PTSIR")
    movie_list=["aranmanai4","karudan","ptsir"]
    movie=input("enter the movie name :")
    if movie in movie_list:
        if movie=="aranmanai4":
            print("**************************")
            no_of_ticket=int(input("how many ticket do you want:"))
            print("...AVAILABLE CLASS...")
            print("first class=$150\nsecond class=$120\nthird class=$100")
            select_class=int(input("enter the class you want :"))
            if (select_class==1):
                amt=no_of_ticket*150
                gst=amt*0.18
                total=amt+gst
                print(f"the amount for the ticket booking is {total}")
                sql="insert into movie_booking(name,email,movie_name,no_of_ticket,select_class,total)values(%s,%s,%s,%s,%s,%s)"
                name=input("enter your name :")
                email=input("enter your email id :")
                movie_name=movie
                no_of_ticket=no_of_ticket
                select_class=select_class
                total=total
                val=(name,email,movie_name,no_of_ticket,select_class,total)
                mycursor.execute(sql,val)
                mydb.commit()
                print("data saved successfully")
                email_msg(email,total)
            elif (select_class==2):
                amt=no_of_ticket*120
                gst=amt*0.18
                total=amt+gst
                print(f"the amount for the ticket booking is {total}")
                sql="insert into movie_booking(name,email,movie_name,no_of_ticket,select_class,total)values(%s,%s,%s,%s,%s,%s)"
                name=input("enter your name :")
                email=input("enter your email id :")
                movie_name=movie
                no_of_ticket=no_of_ticket
                select_class=select_class
                total=total
                val=(name,email,movie_name,no_of_ticket,select_class,total)
                mycursor.execute(sql,val)
                mydb.commit()
                print("data saved successfully")
                email_msg(email,total)
            elif (select_class==3):
                amt=no_of_ticket*100
                gst=amt*0.18
                total=amt+gst
                print(f"the amount for the ticket booking is {total}")
                sql="insert into movie_booking(name,email,movie_name,no_of_ticket,select_class,total)values(%s,%s,%s,%s,%s,%s)"
                name=input("enter your name :")
                email=input("enter your email id :")
                movie_name=movie
                no_of_ticket=no_of_ticket
                select_class=select_class
                total=total
                val=(name,email,movie_name,no_of_ticket,select_class,total)
                mycursor.execute(sql,val)
                mydb.commit()
                print("data saved successfully")
                email_msg(email,total)
            else:
                print("please select the available classes")
        elif movie=="karudan":
            print("**************************")
            no_of_ticket=int(input("how many tickets do you want"))           
            print("...AVAILABLE CLASS...")
            print("first class=$150\nsecond class=$120\nthird class=$100")
            select_class=int(input("enter the class you want :"))
            if (select_class==1):
                amt=no_of_ticket*150
                gst=amt*0.18
                total=amt+gst
                print(f"the amount for the ticket booking is {total}")
                sql="insert into movie_booking(name,email,movie_name,no_of_ticket,select_class,total)values(%s,%s,%s,%s,%s,%s)"
                name=input("enter your name :")
                email=input("enter your email id :")
                movie_name=movie
                no_of_ticket=no_of_ticket
                select_class=select_class
                total=total
                val=(name,email,movie_name,no_of_ticket,select_class,total)
                mycursor.execute(sql,val)
                mydb.commit()
                print("data saved successfully")
                email_msg(email,total)
            elif (select_class==2):
                amt=no_of_ticket*120
                gst=amt*0.18
                total=amt+gst
                print(f"the amount for the ticket booking is {total}")
                sql="insert into movie_booking(name,email,movie_name,no_of_ticket,select_class,total)values(%s,%s,%s,%s,%s,%s)"
                name=input("enter your name :")
                email=input("enter your email id :")
                movie_name=movie
                no_of_ticket=no_of_ticket
                select_class=select_class
                total=total
                val=(name,email,movie_name,no_of_ticket,select_class,total)
                mycursor.execute(sql,val)
                mydb.commit()
                print("data saved successfully")
                email_msg(email,total)
            elif (select_class==3):
                amt=no_of_ticket*100
                gst=amt*0.18
                total=amt+gst
                print(f"the amount for the ticket booking is {total}")
                sql="insert into movie_booking(name,email,movie_name,no_of_ticket,select_class,total)values(%s,%s,%s,%s,%s,%s)"
                name=input("enter your name :")
                email=input("enter your email id :")
                movie_name=movie
                no_of_ticket=no_of_ticket
                select_class=select_class
                total=total
                val=(name,email,movie_name,no_of_ticket,select_class,total)
                mycursor.execute(sql,val)
                mydb.commit()
                print("data saved successfully")
                email_msg(email,total)
            else:
                print("please select the available classes")
        elif movie=="ptsir":
            print("**************************")
            no_of_ticket=int(input("how many tickets do you want"))
            print("...AVAILABLE CLASS...")
            print("first class=$150\nsecond class=$120\nthird class=$100")
            select_class=int(input("enter the class you want :"))
            if (select_class==1):
                amt=no_of_ticket*150
                gst=amt*0.18
                total=amt+gst
                print(f"the amount for the ticket booking is {total}")
                sql="insert into movie_booking(name,email,movie_name,no_of_ticket,select_class,total)values(%s,%s,%s,%s,%s,%s)"
                name=input("enter your name :")
                email=input("enter your email id :")
                movie_name=movie
                no_of_ticket=no_of_ticket
                select_class=select_class
                total=total
                val=(name,email,movie_name,no_of_ticket,select_class,total)
                mycursor.execute(sql,val)
                mydb.commit()
                print("data saved successfully")
                email_msg(email,total)
            elif (select_class==2):
                amt=no_of_ticket*120
                gst=amt*0.18
                total=amt+gst
                print(f"the amount for the ticket booking is {total}")
                sql="insert into movie_booking(name,email,movie_name,no_of_ticket,select_class,total)values(%s,%s,%s,%s,%s,%s)"
                name=input("enter your name :")
                email=input("enter your email id :")
                movie_name=movie
                no_of_ticket=no_of_ticket
                select_class=select_class
                total=total
                val=(name,email,movie_name,no_of_ticket,select_class,total)
                mycursor.execute(sql,val)
                mydb.commit()
                print("data saved successfully")
                email_msg(email,total)
            elif (select_class==3):
                amt=no_of_ticket*100
                gst=amt*0.18
                total=amt+gst
                print(f"the amount for the ticket booking is {total}")
                sql="insert into movie_booking(name,email,movie_name,no_of_ticket,select_class,total)values(%s,%s,%s,%s,%s,%s)"
                name=input("enter your name :")
                email=input("enter your email id :")
                movie_name=movie
                no_of_ticket=no_of_ticket
                select_class=select_class
                total=total
                val=(name,email,movie_name,no_of_ticket,select_class,total)
                mycursor.execute(sql,val)
                mydb.commit()
                print("data saved successfully")
                email_msg(email,total)
            else:
                print("please select the available classes")
        else:
            print(f"sorry.....{movie} movie is not available")
main()