"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
todaydate = datetime.today().day
todaymonth = datetime.today().month
from calendar import month_name

name = input("Hello, what is your name? ")
month = input("Hi {0}, what was the name of the month you were born in? ".format(name))
year = int(input("And what year were you born in, {0}? ".format(name)))
date = int(input("And the day? "))

if month == "October" and date == 31:
    print ("You were born on Halloween!")
elif month == month_name[todaymonth] and todaydate == date:
    print("Happy birthday!")
else:
    decade = "Stone Age"
    if year >= 2000:
        decade = "two thousands"
    elif year >= 1990:
        decade = "nineties"
    elif year >= 1980:
        decade = "eighties"
    if month in ["January", "February", "December"]:
        season = "winter"
    elif month in ["March", "April", "May"]:
        season = "spring"
    elif month in ["June", "July", "August"]:
        season = "summer"
    else:
        season = "fall"
    print("{0}, you are a {1} baby of the {2}.".format(name, season, decade))
