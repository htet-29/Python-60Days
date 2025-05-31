def feet_inches_to_meters(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


if __name__ == "__main__":
    meter = feet_inches_to_meters(3, 4)
    print(meter)