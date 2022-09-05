import PySimpleGUI as sg
import pyperclip3 as pc3
import openpyxl as xl
import main_window
from pathlib import Path

sg.theme('dark grey 9')

def main():

    #initialize
    path=str(Path.cwd())+'/resource/sample.xlsx'
    sheetName='Sheet1'

    #open_excel
    wb=xl.load_workbook(path)
    ws=wb[sheetName]
    ir=iter(ws.iter_rows())

    #title_dict
    title=ir.__next__()
    title_dict={}
    for i,key in enumerate(title):
        title_dict[key]=i
    
    #main_dict
    main_dict={}
    while(col:=next(ir,None)):
        key,*vals=col
        main_dict[str(key.value)]=vals

    #get_window
    window=main_window.get()
    window.finalize()

    #keybind
    window['-Out1-'].bind('<Control-1>','ctl1')

    while True:
        event,values=window.read()
        if event =='-Input-':
            window['-Out1-'].Update(search(main_dict,str(values['-Input-']),1))
        if event=='-Copy1-' or'-Out1-ctl1' :
            copy(window)
        if event=='-Down-':
            f=window['-Format-']
            f.Update(visible=f.visibility)
            window['-Format-'].Update()
        if event==sg.WIN_CLOSED or event=='Exit':
            break

    window.close()
    wb.close()

def copy(window):
    pc3.copy(str(window['-Out1-'].get()))

# search-dict
# dict={key:list}
def search(dict,key,index):
    if type(val:=dict.get(key,key))==list:
        return val[index].value
    return val
    

if __name__=='__main__':
    main()