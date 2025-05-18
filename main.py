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

    if "show" in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todo = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    if "edit" in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(input("Number of the todo to edit: "))
        number = number -1

        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo.capitalize()

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    if "complete" in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(input("Number of the todo to complete: "))
        item_to_removed = todos.pop(number - 1)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {item_to_removed.strip('\n')} has been completed."
        print(message)
    if "exit" in user_action:
        break

print("Bye!")

