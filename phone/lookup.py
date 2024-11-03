import phonenumbers
from phonenumbers import geocoder, carrier
def phonenum_lookup(number):
    phone_number = number
    parsed_number = phonenumbers.parse(phone_number)
    country = geocoder.description_for_number(parsed_number, "en")
    carrier_name = carrier.name_for_number(parsed_number, "en")
    return "Country/Region: " + str(country) + "Carrier: " + str(carrier_name)
