todos = []

while True:
    user_action = input("Enter add, show or exit: ")
    user_action = user_action.lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case "show":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break

print("Bye!")

