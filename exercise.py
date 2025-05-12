filenames = ['document', 'report', 'presentation']

for index, filename in enumerate(filenames):
    row = f"{index}-{filename.capitalize()}.txt"
    print(row)
