import PySimpleGUI as sg
import pyperclip3 as pc3
import main_window

sg.theme('dark grey 9')

def main():

    window=main_window.get()
    window.finalize()
    window['-Out1-'].bind('<Control-1>','ctl1')

    while True:
        event,values=window.read()
        if event =='-Input-':
            window['-Out1-'].Update(str(values['-Input-']))
        if event=='-Copy1-' or'-Out1-ctl1' :
            copy(window)
        if event==sg.WIN_CLOSED or event=='Exit':
            break

    window.close()

def copy(window):
    pc3.copy(str(window['-Out1-'].get()))

if __name__=="__main__":
    main()