import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_text = sg.InputText(tooltip='Enter todo')
add_button = sg.Button('Add')

window = sg.Window('My To-do App', layout=[[label], [input_text, add_button]])
window.read()
window.close()
