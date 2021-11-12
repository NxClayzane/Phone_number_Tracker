import phonenumbers
from phonenumbers import carrier, geocoder, timezone

print("------------------------------------------------------------")
print("|              Number tracker v-1.0                       |")
print("___________________________________________________________")


mobileNo=input("Enter a phone number with country code = ")

mobileNo=phonenumbers.parse(mobileNo)

print("           carrier timezone       ")
print(timezone.time_zones_for_number(mobileNo))


print("           Carrier name      ")
print(carrier.name_for_number(mobileNo,"en"))

print("           Country name       ")
print(geocoder.description_for_number(mobileNo,"en"))


print("Valid number = ",phonenumbers.is_possible_number(mobileNo))
