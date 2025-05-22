def get_average():
    with open("file/data.txt") as file:
        data = file.readlines()
        values = data[1:]
        values = [float(i) for i in values]
        _average = sum(values) / len(values)
        return _average


average = get_average()
print(average)