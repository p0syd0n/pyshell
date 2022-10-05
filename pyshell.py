import tkinter as tk
import tkinter.messagebox as tkm
import random
import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import keyboard
from selenium.webdriver.common.action_chains import ActionChains

ERROR_TEXT_COLOR='yellow'
ERROR_HIGHLIGHT_COLOR='blue'
SEPARATOR="/"
WARNING_TEXT_COLOR='red'
WARNING_HIGHLIGHT_COLOR='blue'

SHELL_TEXT_COLOR='white'
SHELL_BACKGROUND_COLOR='blue'

window=tk.Tk()
window.geometry("900x500")
window.title("pyshell")
window.config(bg=SHELL_BACKGROUND_COLOR)
line=1
shell=tk.Text(window, bg=SHELL_BACKGROUND_COLOR, fg=SHELL_TEXT_COLOR, width='500', height="900", font='TkFixedFont')
shell.place(x=0, y=0)
shell.insert(tk.END, f"@>>")
shell.focus()
scrollbar=tk.Scrollbar(window, orient='vertical')
scrollbar.pack(side=tk.RIGHT, fill='y')
scrollbar.config(command=shell.yview)
shell.yview_pickplace("end")
shell.pack()
default="https://google.com"
shell.tag_config('warning', background=WARNING_HIGHLIGHT_COLOR, foreground=WARNING_TEXT_COLOR)
shell.tag_config('error', background=ERROR_HIGHLIGHT_COLOR, foreground=ERROR_TEXT_COLOR)
shell.tag_config('none', background=SHELL_BACKGROUND_COLOR, foreground=SHELL_TEXT_COLOR)

def help():
    global line
    print(
        '''
         Syntax
         command/argument1//

         (more arguments to be added shortly)


         Command Directory
         slm/site//.....opens a selenium page where 'site' is the url
         file/file-to-open//........opens a file where 'file-to-open' is the file you want opened
         help/......................opens this directory


         Shortcuts
         c/..................Starts chrome with google
         s/..................starts selenium with google
        '''
    )
    text(
        f'''
            Syntax:
            command{SEPARATOR}argument1{SEPARATOR}{SEPARATOR}

            (more arguments to be added shortly)


            Command Directory:
            slm{SEPARATOR}site{SEPARATOR}{SEPARATOR}.....opens a selenium page where 'site' is the url
            file{SEPARATOR}file-to-open{SEPARATOR}{SEPARATOR}........opens a file where 'file-to-open' is the file you want opened
            help{SEPARATOR}......................opens this directory


            Shortcuts:
            c{SEPARATOR}..................starts chrome with google
            s{SEPARATOR}..................starts selenium with google
        '''
    , 'none')
    line=line+16

def clear():
    shell.delete(1.0, tk.END)


def text(text, type):
    global line
    shell.insert(tk.END, f"$>>{text}", type)
    line=line+1

def selenium(argument1):
    try:
        print("[!] Warning! Shell may become unresponsive after initiating Selenium")
        text("\n$>>[!] Warning! Shell may become unresponsive after initiating Selenium", 'warning')
        driver = webdriver.Chrome()
        driver.get(argument1)
        sleep(4165200)
        

    except Exception as e:

        text(f'[!] Error \n {e} \n \n [!] Error{argument1} is not a url. Searching google\n', 'error')
        try:
            driver.get(f'https://www.google.com/search?q={argument1}&sxsrf=ALiCzsZW5u6tep9E0Vj72ig52vp8M4YiXg%3A1664822481799&source=hp&ei=0Sw7Y7S3Lviu5NoP96OA6AI&iflsig=AJiK0e8AAAAAYzs64cb8L2Xgf8uavqyENhwm-nqg8glI&ved=0ahUKEwj0446F28T6AhV4F1kFHfcRAC0Q4dUDCAk&uact=5&oq=test&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEEMyBQgAEJECMgUIABCRAjIECAAQQzIECAAQQzIECAAQQzIICAAQgAQQsQMyBAgAEEMyBAgAEEMyCwgAEIAEELEDEIsDOgQIIxAnOgsILhCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CAguELEDEIMBOg4ILhCABBCxAxCDARDUAjoKCC4QxwEQ0QMQQzoTCC4QsQMQgwEQxwEQ0QMQ1AIQQ1AAWIEDYOEIaABwAHgAgAGCAYgBxAOSAQMwLjSYAQCgAQG4AQE&sclient=gws-wiz')
            text('\nError resolved', 'none')
            sleep(4165200)
        except:
            text("Error unresolved", 'warning')
            shell.insert(tk.END, f"\n@>>")


def selenium1(default):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_extension('extension_1_7_1_0.crx')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(default)
    # action = ActionChains(driver)
    # action.send_keys(Keys.CONTROL,”t”)


    sleep(4165200)

def selenium2():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(argument1)
    sleep(4165200)

def selenium3():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_extension('extension_1_7_1_0.crx')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(argument1)
    sleep(4165200)

def sort_commands():
    if command == "file":
        print("sorted")
        run_file(argument1)

    elif command == "slm":
        selenium(argument1) 

    if command == "help":
        help()
    
    elif command == "c":
        chrome()

#########
    elif command == "s":
        
        if argument1 == "1":
            selenium1(default)
        else:
            pass


###############
    elif command == "sl":
        try:
            if argument2 == "1":
                selenium1(argument1)

            if argument2 == "2":
                selenium2(argument1)

            if argument2 == "3":
                selenium3(argument1)

            else:
                sleep(1)
                text("argument2 not recognised", "warning")
                selenium(argument1)
        except:
            text("argument2 not found", "error")
        

    

def run_file(argument1):
    os.system(f"start {argument1}")
    text(f"started {argument1}", 'none')


def chrome():
    os.system(f"start chrome.exe")


def extract(window):
    print('start of function')
    global extracted, line, command, argument1, argument2
    
    extracted=shell.get(f'{line}.2', tk.END)

    sub1 = ">"
    sub2 = f"{SEPARATOR}"
    idx1 = extracted.index(sub1)
    idx2 = extracted.index(sub2)
    command = extracted[idx1 + len(sub1) + 0: idx2]
    
    try:
        sub3 = F"{SEPARATOR}{SEPARATOR}"
        idx3 = extracted.index(sub3)
        argument1 = extracted[idx2 + len(sub1) + 0: idx3]

        print(f"{extracted}\n {command}\n {argument1}\n")
    except:
        pass

    try:
        sub4 = F"{SEPARATOR}{SEPARATOR}{SEPARATOR}"
        idx4 = extracted.index(sub3)
        argument2 = extracted[idx3 + len(sub1) + 0: idx4]
    except:
        pass

    # update line
    line=line+1
    sort_commands()
    #inserting next prompt
    shell.insert(tk.END, f"\n@>>")
    

    print('end of function')
    
    



window.bind("<Return>", extract)
window.mainloop()

