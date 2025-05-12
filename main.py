todos = []

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case "show":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
            print(f"Length of todos : {index+1}. The last item is {item}")
            print(f"Length of todos : {len(todos)}. The last item is {todos[-1]}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number -1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo.capitalize()
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case "exit":
            break

print("Bye!")


