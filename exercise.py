import FreeSimpleGUI as sg

label_1 = sg.Text("Enter feet:")
input_1 = sg.Input()

label_2 = sg.Text("Enter inches:")
input_2 = sg.Input()

convert_btn = sg.Button("Convert")
layout = [
    [label_1, input_1],
    [label_2, input_2],
    [convert_btn]
]

window = sg.Window('Convertor', layout)
window.read()
window.close()