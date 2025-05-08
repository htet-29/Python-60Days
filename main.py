user_prompt = "Enter your todo: "

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo.capitalize())
    print(todos)

