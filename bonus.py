from converter import convert_to_meter
from parser import parsed

measure = input("Enter your measure: ")

units = parsed(measure)
meter = convert_to_meter(units['feet'], units['inches'])

print(f"{units['feet']} feet and {units['inches']} inches is equal to {meter}")

if meter < 1:
    print("The kid is too small.")
else:
    print("The kid can enter the ring.")

