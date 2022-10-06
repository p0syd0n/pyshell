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
ERROR_TEXT_COLOR='red'
ERROR_HIGHLIGHT_COLOR='blue'
SEPARATOR="/"
WARNING_TEXT_COLOR='orange'
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
        print("initiating Selenium")
        print("[!] Warning! Shell may become unresponsive after initiating Selenium")
        text("\n$>>[!] Warning! Shell may become unresponsive after initiating Selenium", 'warning')
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
    threading.Thread(target=selenium(argument1)).start()

def start_selenium_1():
    threading.Thread(target=selenium_1).start()

def start_selenium_2():
     threading.Thread(target=selenium_2).start()

def start_selenium_3():
     threading.Thread(target=selenium_3).start()

def selenium_1(argument1):

 
    
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_extension('extension_1_7_1_0.crx')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(content)
    sleep(4165200)

def warn_selenium():
    text("[!] Warning! Shell may become unresponsive after initiating Selenium", 'warning')
    
    

def selenium_2(argument2):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(argument2)
        sleep(4165200)
    except:
        driver.get(f'https://www.google.com/search?q={argument2}&source=hp&ei=l_U9Y-2hD-6e5NoP-vGluA0&iflsig=AJiK0e8AAAAAYz4DpxNZoLvh3UggMip95rBGus7DjB7q&ved=0ahUKEwityazlgsr6AhVuD1kFHfp4CdcQ4dUDCAk&uact=5&oq=test&gs_lp=Egdnd3Mtd2l6uAED-AEBGgIYAzILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgUQABiABDILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMhcQLhiABBixAxiDARjUAhiLAxioAxiYAzIOEAAYgAQYsQMYgwEYiwPCAgsQLhiABBixAxiDAcICERAuGIAEGLEDGIMBGMcBGNEDwgIIEC4YsQMYgwHCAg4QLhiABBixAxjHARjRA8ICERAuGIAEGLEDGMcBGNEDGNQCwgIOEC4YgAQYsQMYgwEYiwPCAhQQLhixAxiDARjUAhiLAxijAxioA8ICDhAuGLEDGIMBGNQCGIsDwgIXEC4YsQMYgwEYiwMYmgMYqAMYmwMYmAPCAggQLhiABBixA0i_ClAAWIQGcAB4AMgBAJABAJgBR6ABggKqAQE0&sclient=gws-wiz')
        sleep(4165200)

def selenium_3():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_extension('extension_1_7_1_0.crx')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(argument2)
    sleep(4165200)

def sort_commands():
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
            selenium_1(default)
        else:
            pass


###############
    elif command == "sl":
        warn_selenium()
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
                text("[!] Error: argument1 not recognised", "error")


        except Exception as e:
            shell.insert(tk.END, '\n')
            text(f'{e}', 'error')
    else:
        text('[!] Error: Command not recognized')
    


        

    

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

