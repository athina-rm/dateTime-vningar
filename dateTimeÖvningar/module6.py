#Write a program letting the user input a date in format 2012-02-18 and you should convert it to a

#datetime
import datetime
date=datetime.datetime.strptime(input("Ange Datum yyyy-mm-dd : "),"%Y-%m-%d")
