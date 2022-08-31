import smtplib
import pandas
import datetime as dt
import random

MY_EMAIL_LOGIN = "learningtocode991@gmail.com"
MY_EMAIL_PASSWORD = "bsvkswhygqfzdkab"

birthday_wishes = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthdays_file = pandas.read_csv("birthdays.csv")

today = dt.datetime.now()
birthday_day = birthdays_file["day"]
birthday_month = birthdays_file["month"]

for (index, row) in birthdays_file.iterrows():
    if row.month == today.month and row.day == today.day:
        my_wishes = random.choice(birthday_wishes)
        with open(f"./letter_templates/{my_wishes}") as wish_text:
            my_wishes_fill = wish_text.read()

        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            connection.login(user=MY_EMAIL_LOGIN, password=MY_EMAIL_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL_LOGIN, to_addrs=row.email,
                                msg=f"Subject:Birthday Wishes from Adam\n\n{my_wishes_fill.replace('[NAME]', row[0])}")
