import FreeSimpleGUI as sg
from zip_creator import make_archive

label_1 = sg.Text('Select files to compress:')
input_1 = sg.Input()
choose_btn_1 = sg.FilesBrowse('Choose', key='files')

label_2 = sg.Text('Select destination folder:')
input_2 = sg.Input()
choose_btn_2 = sg.FolderBrowse('Choose', key='folder')

compressed_btn = sg.Button('Compress')
output_text = sg.Text(key='output', text_color='green')

layout = [
    [label_1, input_1, choose_btn_1],
    [label_2, input_2, choose_btn_2],
    [compressed_btn, output_text]
]

window = sg.Window('File Compressor', layout)

while True:
    event, values = window.read()
    print(event, values)
    files_path = values['files'].split(';')
    folder_path = values['folder']
    make_archive(files_path, folder_path)
    window['output'].update(value='Compression successful!')
    if event == sg.WIN_CLOSED:
        break

window.close()