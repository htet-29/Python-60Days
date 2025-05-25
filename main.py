import functions

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos_from_file()

        todos.append(todo.capitalize())

        functions.write_todos_to_file(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos_from_file()

        # new_todo = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):

        try:
            todos = functions.get_todos_from_file()

            number = int(user_action[5:])
            number = number -1

            new_todo = input("Enter a new todo: ") + '\n'
            todos[number] = new_todo.capitalize()

            functions.write_todos_to_file(todos)
        except ValueError:
            print("Command is not valid!")
            continue

    elif user_action.startswith("complete"):

        try:
            todos = functions.get_todos_from_file()

            number = int(user_action[9:])
            item_to_removed = todos.pop(number - 1)

            functions.write_todos_to_file(todos)

            message = f"Todo {item_to_removed.strip('\n')} has been completed."
            print(message)

        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print('Command is not valid! Try keywords(add, show, edit, complete, exit).')

print("Bye!")

