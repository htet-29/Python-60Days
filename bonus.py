filenames = ['1.dog', "2.cat", "3.fish"]

filenames = [filename.replace(".", "-") + '.txt' for filename in filenames]

print(filenames)