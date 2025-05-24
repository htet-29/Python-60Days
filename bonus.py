measure = input("Enter your measure: ")

def parsed(_measure):
    _measure = _measure.split(" ")
    feet = float(_measure[0])
    inches = float(_measure[1])
    return {'feet': feet, 'inches': inches}


def convert_to_meter(feet, inches):
    _meter = feet * 0.3048 + inches * 0.0254
    return _meter


units = parsed(measure)
meter = convert_to_meter(units['feet'], units['inches'])

print(f"{units['feet']} feet and {units['inches']} inches is equal to {meter}")

if meter < 1:
    print("The kid is too small.")
else:
    print("The kid can enter the ring.")

