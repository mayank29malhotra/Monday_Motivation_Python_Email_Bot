import smtplib
import datetime as dt
import random
now = dt.datetime.now()
main_quote = ""
writer = ""


def read_quote():
    global writer, main_quote
    with open(file="quotes.txt") as file:
        lines = file.readlines()
        quote = random.choice(lines)
        try:
            main_quote, writer = quote.split('" -', 1)
            main_quote = main_quote + '"'
            print("Generated")
        except:
            print("Failed Genearating again")
            read_quote()

my_email = "email@gmail.com"
password = "PassWord"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password= password)
if now.weekday() == 0:
    read_quote()
    connection.sendmail(from_addr=my_email, to_addrs="reciever_email@gmail.com", msg=f"Subject: Monday Motivation by{writer} \n\n {main_quote}")
    print(f"Subject: Monday Motivation by{writer} \n\n {main_quote}")


else:
    print("Not sent ")

if now.day == 30:
    connection.sendmail(from_addr=my_email, to_addrs="admin@gmail.com", msg=f"Subject: Renew Automated Tasks \n\n Renew Motivation Task")


connection.close()

