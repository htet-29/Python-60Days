import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme('Black')

label_1 = sg.Text('Select file to extract:')
input_1 = sg.Input()
choose_btn_1 = sg.FileBrowse('Choose', key='archive')

label_2 = sg.Text('Select destination folder:')
input_2 = sg.Input()
choose_btn_2 = sg.FolderBrowse('Choose', key='folder')

compressed_btn = sg.Button('Extract')
output_text = sg.Text(key='output', text_color='green')

col1 = sg.Column([[label_1], [label_2]])
col2 = sg.Column([[input_1], [input_2]])
col3 = sg.Column([[choose_btn_1], [choose_btn_2]])

layout = [
    [col1, col2, col3],
    [compressed_btn, output_text]
]

window = sg.Window('Zip Extractor', layout)

while True:
    event, values = window.read()
    file_path = values['archive']
    folder_path = values['folder']
    extract_archive(file_path, folder_path)
    window['output'].update(value='Extraction successful!')
    if event == sg.WIN_CLOSED:
        break

window.close()