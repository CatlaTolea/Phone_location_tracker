import phonenumbers

from phonenumbers import carrier
from phonenumbers import geocoder

type_number = input("Enter the phone number: ")

number = phonenumbers.parse(type_number)
print(geocoder.description_for_number(number, 'en'))
print(carrier.name_for_number(number, 'en'))

