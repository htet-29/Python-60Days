todos = []

while True:
    user_action = input("Enter add, show or exit: ")
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case "show":
            print(todos)
        case "exit":
            break

print("Bye!")

