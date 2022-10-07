import tkinter as tk
import tkinter.messagebox as tkm
import random
import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import keyboard
from selenium.webdriver.common.action_chains import ActionChains
import threading
from datetime import datetime, date
ERROR_TEXT_COLOR='red'
ERROR_HIGHLIGHT_COLOR='black'
SEPARATOR="."
WARNING_TEXT_COLOR='yellow'
WARNING_HIGHLIGHT_COLOR='black'

SHELL_TEXT_COLOR='white'
SHELL_BACKGROUND_COLOR='black'

CURSOR_COLOR='white'

window=tk.Tk()
window.geometry("900x500")
window.title("pyshell")
window.config(bg=SHELL_BACKGROUND_COLOR)
line=1
shell=tk.Text(window, bg=SHELL_BACKGROUND_COLOR, fg=SHELL_TEXT_COLOR, width='500', height="900", font='TkFixedFont', blockcursor=True)
shell.place(x=0, y=0)
shell.insert(tk.END, f"@>>")
shell.config(insertbackground=CURSOR_COLOR)
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
            command{SEPARATOR}argument1{SEPARATOR}{SEPARATOR}argument2{SEPARATOR}{SEPARATOR}{SEPARATOR}

            (not all commands need 2 arguments)


            Command Directory:
            slm{SEPARATOR}site{SEPARATOR}{SEPARATOR}.................opens a selenium page where 'site' is the url
            file{SEPARATOR}file-to-open{SEPARATOR}{SEPARATOR}........opens a file where 'file-to-open' is the file you want opened
            help{SEPARATOR}..........................................opens this directory


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
        print("initiating Selenium")

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(default)
        
        

    except Exception as e:

        text(f'[!] Error \n {e} \n \n [!] Error{argument1} is not a url. Searching google\n', 'error')
        try:
            driver.get(f'https://www.google.com/search?q={argument1}&sxsrf=ALiCzsZW5u6tep9E0Vj72ig52vp8M4YiXg%3A1664822481799&source=hp&ei=0Sw7Y7S3Lviu5NoP96OA6AI&iflsig=AJiK0e8AAAAAYzs64cb8L2Xgf8uavqyENhwm-nqg8glI&ved=0ahUKEwj0446F28T6AhV4F1kFHfcRAC0Q4dUDCAk&uact=5&oq=test&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEEMyBQgAEJECMgUIABCRAjIECAAQQzIECAAQQzIECAAQQzIICAAQgAQQsQMyBAgAEEMyBAgAEEMyCwgAEIAEELEDEIsDOgQIIxAnOgsILhCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CAguELEDEIMBOg4ILhCABBCxAxCDARDUAjoKCC4QxwEQ0QMQQzoTCC4QsQMQgwEQxwEQ0QMQ1AIQQ1AAWIEDYOEIaABwAHgAgAGCAYgBxAOSAQMwLjSYAQCgAQG4AQE&sclient=gws-wiz')
            text('\nError resolved', 'none')
            sleep(4165200)
        except:
            text("Error unresolved", 'warning')
            shell.insert(tk.END, f"\n@>>")

def start_selenium(argument1):
    print('reached new thread')
    try:
        text("Threading started", 'none')
        text("\n[!] Warning! Shell may become unresponsive for a few seconds after initiating Selenium", 'warning')
        threading.Thread(target=selenium(argument1)).start()
    except Exception as e:
        text("[!] Error! Error during threading", 'error')


def start_selenium_1(argument2):
    print('reached new thread')
    try:
        text("Threading started", 'none')
        text("\n[!] Warning! Shell may become unresponsive for a few seconds after initiating Selenium", 'warning')
        threading.Thread(target=seleium_1(argument2)).start()
    except Exception as e:
        shell.insert(tk.END, "\n$>>[!] Error: Error during threading, written to error log", 'error')
        today = date.today()
        now = datetime.now()
        timm = now.strftime("%H:%M:%S")
        datt = today.strftime("%b-%d-%Y")
        f = open("error_log.txt", "a")
        f.write(f'\n\n-------------------{datt} {timm}-------------------------\n {e}')
        f.close()

def start_selenium_2(argument2):
    print('reached new thread')
    try:
        text("Threading started", 'none')
        text("\n[!] Warning! Shell may become unresponsive for a few seconds after initiating Selenium", 'warning')
        threading.Thread(target=selenium_2(argument2)).start()
    except Exception as e:
        text("\n[!] Error! Error during threading, written to error log", 'error')
        today = date.today()
        now = datetime.now()
        timm = now.strftime("%H:%M:%S")
        datt = today.strftime("%b-%d-%Y")
        f = open("error_log.txt", "a")
        f.write(f'\n\n-------------------{datt} {timm}-------------------------\n {e}')
        f.close()


def start_selenium_3(argument2):
    print('reached new thread')
    try:
        text("Threading started", 'none')
        text("\n[!] Warning! Shell may become unresponsive for a few seconds after initiating Selenium", 'warning')
        threading.Thread(target=selenium_3(argument2)).start()
    except Exception as e:
        text("\n[!] Error! Error during threading, written to error log", 'error')
        today = date.today()
        now = datetime.now()
        timm = now.strftime("%H:%M:%S")
        datt = today.strftime("%b-%d-%Y")
        f = open("error_log.txt", "a")
        f.write(f'\n\n-------------------{datt} {timm}-------------------------\n {e}')
        f.close()


def selenium_1(argument2):

 
    try:
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_extension('extension_1_7_1_0.crx')
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(argument2)
    except:
        driver.get(f'https://www.google.com/search?q={argument2}&source=hp&ei=zjg_Y9pBpqvk2g-FhorgDg&iflsig=AJiK0e8AAAAAYz9G3qutdeqr7By_peYazdQtVoi2XQIP&ved=0ahUKEwja4JWEt8z6AhWmFVkFHQWDAuwQ4dUDCAk&uact=5&oq=test&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIFCAAQgAQyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwguEIAEELEDENQCOgsILhCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6BQguEIAEOggILhCxAxCDAToOCC4QgAQQsQMQxwEQ0QM6EQguEIAEELEDEMcBENEDENQCOgsILhCxAxCDARDUAjoICC4QgAQQsQNQAFjQAmC6CGgAcAB4AIABUogBngKSAQE0mAEAoAEB&sclient=gws-wiz')    

def warn_selenium():
    text("[!] Warning! Shell may become unresponsive after initiating Selenium", 'warning')
    
    

def selenium_2(argument2):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        chrome_options.add_experimental_option("detach", True)
        driver.get(argument2)
        
        
        
    except:
        driver.get(f'https://www.google.com/search?q={argument2}&source=hp&ei=zjg_Y9pBpqvk2g-FhorgDg&iflsig=AJiK0e8AAAAAYz9G3qutdeqr7By_peYazdQtVoi2XQIP&ved=0ahUKEwja4JWEt8z6AhWmFVkFHQWDAuwQ4dUDCAk&uact=5&oq=test&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIFCAAQgAQyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwguEIAEELEDENQCOgsILhCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6BQguEIAEOggILhCxAxCDAToOCC4QgAQQsQMQxwEQ0QM6EQguEIAEELEDEMcBENEDENQCOgsILhCxAxCDARDUAjoICC4QgAQQsQNQAFjQAmC6CGgAcAB4AIABUogBngKSAQE0mAEAoAEB&sclient=gws-wiz')
        

def selenium_3(argument2):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_extension('extension_1_7_1_0.crx')
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(argument2)
    

def sort_commands():
    tkm.showwarning('WARNING', 'I am IN THE PROCESS of building this part of pyshell-program may crash unexpectedly')
    global line
    if command == "file":
        print("sorted")
        run_file(argument1)

    elif command == "slm":
        start_selenium(argument1) 

    elif command == "help":
        help()
    
    elif command == "c":
        chrome()

#########
    elif command == "s":
        
        if argument1 == "1":
            start_selenium_1(default)
        else:
            text('[!] Error- Argument not recognized', 'error')


###############
    elif command == "sl":
        
        try:
            if argument1 == "1":
                print(f'argument2: {argument2}')
                print("selenium1")
                start_selenium_1(argument2)

            if argument1 == "2":
                print(f'argument2: {argument2}')
                print("selenium2")
                start_selenium_2(argument2)

            if argument1 == "3":
                print(f'argument2: {argument2}')
                print("selenium3")
                start_selenium_3(argument2)

            else:
                sleep(1)
                shell.insert(tk.END, "\n[!] Error: argument1 not recognised", "error")
                line+=1


        except Exception as e:
            shell.insert(tk.END, '\n')
            text(f'{e}', 'error')
    else:
        text('[!] Error: Command not recognized', 'error')
    


        

    

def run_file(argument1):
    os.system(f"start {argument1}")
    text(f"started {argument1}", 'none')


def chrome():
    text('chrome opened', 'none')
    os.system(f"start chrome.exe")


def extract(window):
    print('start of function')
    global extracted, line, command, argument1, argument2
    
    extracted=shell.get(f'{line}.2', tk.END)
    try:
        sub1 = ">"
        sub2 = f"{SEPARATOR}"
        idx1 = extracted.index(sub1)
        idx2 = extracted.index(sub2)
        command = extracted[idx1 + len(sub1) + 0: idx2]
    except:
        text('[!] Error: Command not recognized', 'error')
        shell.insert(tk.END, f"\n@>>")
        line=line+1
        
    
    try:
        sub3 = f"{SEPARATOR}{SEPARATOR}"
        idx3 = extracted.index(sub3)
        argument1 = extracted[idx2 + len(sub1) + 0: idx3]

        print(f"{extracted}\n {command}\n {argument1}\n")
    except:
        pass

    try:
        sub4 = f"{SEPARATOR}{SEPARATOR}{SEPARATOR}"
        idx4 = extracted.index(sub4)
        argument2 = extracted[idx3 + len(sub1) + 1: idx4]
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

