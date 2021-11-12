import pywhatkit


phone_number = input('Enter The Number Here => ')
message = input('Enter The Message Here => ')
Hour = int(input("Hour =>"))
Minute = int(input("Minute =>"))

pywhatkit.sendwhatmsg(f'+91{phone_number}', message, Hour, Minute)
