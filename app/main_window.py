import PySimpleGUI as sg


layout=[
    [sg.Input(key='-Input-',enable_events=True)],
    [sg.Button('#1',key='-Copy1-'),sg.Text('',key='-Out1-')],
    [sg.Button('▽',key='-Down-')],
    [sg.Input(key='-Format-')]
]

def get():
    return sg.Window('dict',layout)