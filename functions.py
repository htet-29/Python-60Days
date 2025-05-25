def get_todos_from_file(filepath="todos.txt"):
    """Read a text file and return a list of todo-item."""
    with open(filepath, 'r') as _file:
        _todos = _file.readlines()
    return _todos


def write_todos_to_file(_todos, filepath="todos.txt"):
    """Write a list of todo-item to a text file."""
    with open(filepath, 'w') as _file:
        _file.writelines(_todos)

print('Functions.py')
if __name__ == '__main__':
    print('Hello!')
    print(get_todos_from_file())