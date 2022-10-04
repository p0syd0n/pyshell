import tkinter as tk
import tkinter.messagebox as tkm
import random
import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import keyboard
window=tk.Tk()
window.geometry("900x500")
window.title("pyshell")
window.config(bg="black")
line=1
shell=tk.Text(window, bg="blue", fg="white", width='500', height="900", font='TkFixedFont')
shell.place(x=0, y=0)
shell.insert(tk.END, f"@>>")
shell.focus()
scrollbar=tk.Scrollbar(window, orient='vertical')
scrollbar.pack(side=tk.RIGHT, fill='y')
scrollbar.config(command=shell.yview)
shell.yview_pickplace("end")
shell.pack()
default="https://google.com"



def clear():
    shell.delete(1.0, tk.END)


def text(text):
    
    shell.insert(tk.END, f"$>>{text}")


def selenium(argument1):
    try:
        driver = webdriver.Chrome()
        driver.get(argument1)
        print("[!] Warning! Shell may become unresponsive after initiating Selenium")
        text("[!] Warning! Shell may become unresponsive after initiating Selenium")
        
        sleep(4165200)
        

    except Exception as e:

        text(f'[!] Error \n {e} \n {argument1} is not a url. Searching google')
        try:
            driver.get(f'https://www.google.com/search?q={argument1}&sxsrf=ALiCzsZW5u6tep9E0Vj72ig52vp8M4YiXg%3A1664822481799&source=hp&ei=0Sw7Y7S3Lviu5NoP96OA6AI&iflsig=AJiK0e8AAAAAYzs64cb8L2Xgf8uavqyENhwm-nqg8glI&ved=0ahUKEwj0446F28T6AhV4F1kFHfcRAC0Q4dUDCAk&uact=5&oq=test&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEEMyBQgAEJECMgUIABCRAjIECAAQQzIECAAQQzIECAAQQzIICAAQgAQQsQMyBAgAEEMyBAgAEEMyCwgAEIAEELEDEIsDOgQIIxAnOgsILhCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CAguELEDEIMBOg4ILhCABBCxAxCDARDUAjoKCC4QxwEQ0QMQQzoTCC4QsQMQgwEQxwEQ0QMQ1AIQQ1AAWIEDYOEIaABwAHgAgAGCAYgBxAOSAQMwLjSYAQCgAQG4AQE&sclient=gws-wiz')
            text('\n Error resolved')
        except:
            text("Error unresolved")
            shell.insert(tk.END, f"\n@>>")


def selenium1():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_extension('extension_1_7_1_0.crx')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(default)
    sleep(4165200)


def sort_commands():
    if command == "start":
        print("sorted")
        run_file(argument1)

    elif command == "selenium":
        selenium(argument1) 
    



    elif command == "c":
        chrome()

    elif command == "s":
        if argument1 == "1":
            selenium1()
        else:
            sleep(1)
            selenium(default)
    
        
        



        
 

def run_file(argument1):
    os.system(f"start {argument1}")
    text(f"started {argument1}")

def chrome():
    os.system(f"start chrome.exe")

def extract(window):
    print('start of function')
    global extracted, line, command, argument1
    
    extracted=shell.get(f'{line}.2', tk.END)

    sub1 = ">"
    sub2 = "/"
    idx1 = extracted.index(sub1)
    idx2 = extracted.index(sub2)
    command = extracted[idx1 + len(sub1) + 0: idx2]
    
    try:
        sub3 = "//"
        idx3 = extracted.index(sub3)
        argument1 = extracted[idx2 + len(sub1) + 0: idx3]

        print(f"{extracted}\n {command}\n {argument1}\n")
    except:
        pass

    # update line
    line=line+1
    sort_commands()
    #inserting next prompt
    shell.insert(tk.END, f"\n@>>")
    line=line+1

    print('end of function')
    
    



window.bind("<Return>", extract)
window.mainloop()

