import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os
print("------------------------------------")
print("Welcome to the password generator!")
print("------------------------------------")
platform=input("Enter which platform the password is generated for: ")
length=int(input("Enter the length of a password : "))
cp=platform.capitalize()
number='1234567890'
loweralph="abcdefghijklmnopqrstuvwxyz"
upperalph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specialsym="~!@#$%^&*"

sp=list(specialsym) 
lo=list(loweralph)
up=list(upperalph)
num=list(number)

finalpass=lo+up+num+sp

shuff=random.sample(finalpass,length)
password="".join(shuff)
print("Password is : ",password)

# store the password into the cloud
with open("passwords.txt", "a+") as f:
    f.write(f"{platform} : {password}" )

def save_password_to_sheet(platform, password):
    # Google Sheet setup
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("true-shoreline-466314-p2-9d9e6cd7d8d8.json", scope)
    client = gspread.authorize(creds)

    # Open the sheet by name
    sheet = client.open("password_generator").sheet1

    # Prepare date and time
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = [platform, password, time]

    # Append as a new row
    sheet.append_row(data)
    print("Password saved to cloud.")



save_password_to_sheet(platform, password)