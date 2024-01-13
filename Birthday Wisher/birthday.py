##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas
# 1. Update the birthdays.csv
# done

# 2. Check if today matches a birthday in the birthdays.csv
df_file = pandas.read_csv("birthdays.csv")
print(df_file)

list_letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt","letter_templates/letter_3.txt"]

myemail = XXXX
password = XXXX

now = dt.datetime.now()

for ind in df_file.index:
    if df_file["month"][ind] == now.month and df_file["day"][ind] == now.day:
        nametosend = df_file.loc[ind,"name"]
        print(nametosend)
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        random_pick = random.choice(list_letters)
        print(random_pick)
        with open(f"{random_pick}") as fil:
            full_line = fil.readlines()
            print(type(full_line))
            # full_line[0] = full_line[0].replace("[NAME]", "XX")
            message = "".join(full_line)
            print(message)
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= myemail, password= password)
            connection.sendmail(from_addr=myemail,
                                to_addrs=df_file["email"][ind],
                                msg=f"Subject:Happy Birthday!!\n\n{message}")


