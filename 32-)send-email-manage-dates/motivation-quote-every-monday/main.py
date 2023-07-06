import datetime as dt
import smtplib
import random
# datetime
now = dt.datetime.now()

day_of_week = now.weekday()

if (day_of_week == 0):
    file1 = open(r'32-)send-email-manage-dates\quotes.txt', 'r')
    Lines = file1.readlines()
    random_quote = random.choice(Lines)
    # random.choice(quotes)

    # date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
    # print(date_of_birth)
    my_email = "YOUR-EMAIL"
    password = "YOUR-APP-PASSWORD(two-factor-authentication-app-password)"
    target_email = "TARGET-EMAIL"

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=target_email,
                        msg=f"Subject:Hello\n\n{random_quote}.")
    connection.close()
