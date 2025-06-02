import FreeSimpleGUI as sg
from unit_convertor import feet_inches_to_meters

sg.theme('Black')

label_1 = sg.Text("Enter feet:")
input_1 = sg.Input(key="feet")

label_2 = sg.Text("Enter inches:")
input_2 = sg.Input(key="inches")

output = sg.Text(key="output")

convert_btn = sg.Button("Convert")
exit_btn = sg.Button("Exit")

layout = [
    [label_1, input_1],
    [label_2, input_2],
    [convert_btn, exit_btn, output],
]

window = sg.Window('Convertor', layout)

while True:
    event, values = window.read()
    print(event, values)

    match event:
        case 'Convert':
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                result = str(feet_inches_to_meters(feet, inches)) + ' m'
                window['output'].update(value=result)
            except ValueError:
                sg.popup("Please provide two numbers!", font=('Helvetica', 10))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()