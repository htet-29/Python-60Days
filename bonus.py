contents = ["The dogs are barking", "The cats are eating the fish", "My grandma is sleeping"]

filenames = ["dogs.txt", "cats.txt", "grandma.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.writelines(content)
    file.close()