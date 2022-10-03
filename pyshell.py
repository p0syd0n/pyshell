import tkinter as tk
import tkinter.messagebox as tkm
import random
import os

window=tk.Tk()
window.geometry("900x500")
window.title("pyshell")
window.config(bg="black")
line=1
shell=tk.Text(window, bg="blue", fg="white", width='500', height="900", font='TkFixedFont')
shell.place(x=0, y=0)
shell.insert(tk.END, f"{line}>>", "prompt")
shell.focus()



def text(text):
    
    shell.insert(tk.END, f"$>>{text}")
    


def sort_commands():
    if command=="start":
        print("sorted")
        run_file(argument1)
        
 

def run_file(argument1):
    os.system(f"start {argument1}")
    text(f"started {argument1}")
    

def extract(window):
    print('start of function')
    global extracted, line, command, argument1
    
    extracted=shell.get(f'{line}.2', tk.END)

    sub1 = ">"
    sub2 = "/"
    idx1 = extracted.index(sub1)
    idx2 = extracted.index(sub2)
    command = extracted[idx1 + len(sub1) + 0: idx2]
    
    
    sub3 = "//"
    idx3 = extracted.index(sub3)
    argument1 = extracted[idx2 + len(sub1) + 0: idx3]

    print(f"{extracted}\n {command}\n {argument1}\n")

    # update line
    line=line+1
    sort_commands()
    #inserting next prompt
    shell.insert(tk.END, f"\n{line}>>")
    line=line+1

    print('end of function')
    
    



window.bind("<Return>", extract)
window.mainloop()

