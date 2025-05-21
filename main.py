while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo.capitalize())

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todo = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(user_action[5:])
            number = number -1

            new_todo = input("Enter a new todo: ") + '\n'
            todos[number] = new_todo.capitalize()

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Command is not valid!")

    elif user_action.startswith("complete"):
        try:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(user_action[9:])
            item_to_removed = todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {item_to_removed.strip('\n')} has been completed."
            print(message)
        except IndexError:
            print("There is no item with that number!")
    elif user_action.startswith("exit"):
        break
    else:
        print('Command is not valid! Try keywords(add, show, edit, complete, exit).')

print("Bye!")

