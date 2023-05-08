import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('MobThePhone'))

phoneNumber = phonenumbers.parse(input("Enter the phone number: "))

Carrier = carrier.name_for_number(phoneNumber, 'en')

Region = geocoder.description_for_number(phoneNumber, 'en')



print(f'Opretor: {Carrier}')
print(f'Region: {Region}')