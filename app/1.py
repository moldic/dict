import PySimpleGUI as sg
import pyperclip3 as pc3

layout=[

    [sg.Input(),sg.FileBrowse()],
    [sg.Button('test',key='-MainBtn-')],
    [sg.Text('',key='-Out1-')],
    [sg.Input(key='-Input-',enable_events=True)]
    
]
for i in range(3):
    layout+= [[sg.Text('aaa')],[sg.Button('',key='-MainBtn-'+str(i))]]

window=sg.Window('タイトル',layout,size=(600,300),finalize=True)

while True:
    event,values=window.read()
    if event=='-MainBtn-':
        pc3.copy(str(window['-Input-'].get()))
        sg.popup('copied')
    if event =='-Input-':
        window['-Out1-'].Update(str(values['-Input-']).upper())
    if event==sg.WIN_CLOSED or event=='Exit':
        break

window.close()