import FreeSimpleGUI as sg

import functions

label = sg.Text('Type in a to-do')
input_text = sg.InputText(tooltip='Enter todo', key='todo_input')
add_button = sg.Button('Add')
todo_listbox = sg.Listbox(values=functions.get_todos_from_file(), key='todos_listbox',
                          enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My To-do App',
                   layout=[[label],
                           [input_text, add_button] ,
                           [todo_listbox, edit_button, complete_button],
                           [exit_button]],
                    font = ('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    match event:
        case "Add":
            todos = functions.get_todos_from_file()
            new_todo = values['todo_input'] + '\n'
            todos.append(new_todo)
            functions.write_todos_to_file(todos)
            window['todos_listbox'].update(values=todos)
            window['todo_input'].update(value='')
        case 'Edit':
            todos = functions.get_todos_from_file()
            todo_to_edit = values['todos_listbox'][0]
            index = todos.index(todo_to_edit)
            new_todo = values['todo_input'] + '\n'
            todos[index] = new_todo
            functions.write_todos_to_file(todos)
            window['todos_listbox'].update(values=todos) # update a listbox
        case 'todos_listbox':
            window['todo_input'].update(value=values['todos_listbox'][0].strip())
        case 'Complete':
            todo_to_complete = values['todos_listbox'][0]
            todos = functions.get_todos_from_file()
            todos.remove(todo_to_complete)
            functions.write_todos_to_file(todos)
            window['todos_listbox'].update(values=todos)
            window['todo_input'].update(value='')
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
