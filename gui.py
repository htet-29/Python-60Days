import FreeSimpleGUI as sg

import functions

label = sg.Text('Type in a to-do')
input_text = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')

window = sg.Window('My To-do App',
                   layout=[[label], [input_text, add_button]],
                    font = ('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos_from_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos_to_file(todos)
        case sg.WIN_CLOSED:
            break

window.close()
