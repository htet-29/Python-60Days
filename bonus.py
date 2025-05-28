import FreeSimpleGUI as sg

label_1 = sg.Text('Select files to compress:')
input_1 = sg.Input()
choose_btn_1 = sg.FilesBrowse('Choose')

label_2 = sg.Text('Select destination folder:')
input_2 = sg.Input()
choose_btn_2 = sg.FolderBrowse('Choose')

compressed_btn = sg.Button('Compress')

layout = [
    [label_1, input_1, choose_btn_1],
    [label_2, input_2, choose_btn_2],
    [compressed_btn]
]

window = sg.Window('File Compressor', layout)
window.read()
window.close()