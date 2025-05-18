while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()

    if "add" in user_action:
        todo = user_action[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo.capitalize())

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todo = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif "edit" in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(user_action[5:])
        number = number -1

        new_todo = input("Enter a new todo: ") + '\n'
        todos[number] = new_todo.capitalize()

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "complete" in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(user_action[9:])
        item_to_removed = todos.pop(number - 1)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {item_to_removed.strip('\n')} has been completed."
        print(message)
    elif "exit" in user_action:
        break
    else:
        print('Command is not valid! Try keywords(add, show, edit, complete, exit).')

print("Bye!")

