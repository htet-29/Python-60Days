measure = input("Enter your measure: ")


def convert_to_meter(_measure):
    _measure = _measure.split(" ")
    feet = float(_measure[0])
    inches = float(_measure[1])
    meter = feet * 0.3048 + inches * 0.0254
    print(meter)
    return meter


result = convert_to_meter(measure)

if result < 1:
    print("The kid is too small.")
else:
    print("The kid can enter the ring.")

