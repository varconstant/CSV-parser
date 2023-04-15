from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
from csv_parser import *

ws = Tk()
ws.title('CSV Converter by Suraj')
ws.geometry('400x200') 

rows = []
suffixToRemove = StringVar()
suffixToAdd = StringVar()
path = ''

def open_file():
    file_path = askopenfile(mode='r', filetypes=[("CSV Files","*.csv")])
    global path
    path = file_path.name
    if file_path is not None:
        print(file_path)
        global rows
        rows=file_path.readlines()
        # print(rows)


def uploadFiles():
    pb1 = Progressbar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
    process(path)

def process(path) :
    modified_rows = []
    global suffixToRemove
    global suffixToAdd
    print(suffixToRemove.get())
    print(suffixToAdd.get())
    for row in rows:
        row = re.sub('\n$','',row)
        modified_row = re.sub(suffixToRemove.get(),'',row)
        # print(modified_row)
        # print(replacement)
        modified_row = modified_row + suffixToAdd.get() +'\n'
        # print(modified_row)
        modified_rows.append(modified_row)
    saveCsv(path,modified_rows)
    
    
csvlbl = Label(ws, text='Upload csv file')
csvlbl.grid(row=0, column=0, padx=10)
csvbtn = Button(ws, text ='Choose File', command = lambda:open_file()) 
csvbtn.grid(row=0, column=1)

toRemove = Label(ws,text='Suffix to remove (can be a regex)')
toRemove.grid(row=1, column=0,padx=10)
toRemovebtn = Entry(ws, textvariable = suffixToRemove,font=('calibre',10,'normal'))
toRemovebtn.grid(row=1, column=1, padx=10)

toadd = Label(ws,text='Suffix to add')
toadd.grid(row=2, column=0,padx=10)
toaddbtn = Entry(ws, textvariable = suffixToAdd,font=('calibre',10,'normal'))
toaddbtn.grid(row=2, column=1, padx=10)

upld = Button(
    ws, 
    text='Upload Files', 
    command=uploadFiles
    )
upld.grid(row=3, columnspan=3, pady=10)


ws.mainloop()