import PySimpleGUI as sg


layout=[
    [sg.Input(key='-Input-',enable_events=True)],
    [sg.Button('c',key='-Copy1-'),sg.Text('',key='-Out1-')],
]

def get():
    return sg.Window('dict',layout)