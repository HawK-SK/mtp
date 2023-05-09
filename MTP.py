import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('MobThePhone'))

print("Enter the number with the country code! ")
phoneNumber = phonenumbers.parse(input("Enter the phone number: "))

# Features
valid = phonenumbers.is_valid_number(phoneNumber)
Carrier = carrier.name_for_number(phoneNumber, 'en')
Timezone = timezone.time_zones_for_number(phoneNumber, 'en')
Region = geocoder.description_for_number(phoneNumber, 'en')

# On-screen print
print(f'Validation: {valid}')
print(f'Opretor: {Carrier}')
print(f'Timezone: {Timezone}')
print(f'Region: {Region}')