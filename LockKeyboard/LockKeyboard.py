# My custom program to lock keyboard and mouse input

from pynput import keyboard, mouse
import bcrypt
import time

# --------------------- Variable Setup Start --------------------- #
Allowed_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
MouseEnabled = True
Password = []
password_salt = b'$2b$12$abcdefghijk1234567890uv'
Real_Pass_hash = "$2b$12$abcdefghijk1234567890uvebfahMd1MXh9fJML1qigno8MiKkT0m"
Alt_pressed_count = 0
# --------------------- Variable Setup End --------------------- #

print(r'''

 ____                 _       _               _    
|  _ \  ___ _ __ ___ (_)_ __ | |    ___   ___| | __
| | | |/ _ \ '_ ` _ \| | '_ \| |   / _ \ / __| |/ /
| |_| |  __/ | | | | | | | | | |__| (_) | (__|   < 
|____/ \___|_| |_| |_|_|_| |_|_____\___/ \___|_|\_\


''')

print("Locking in 5s. \nIf you're using screen: press CTRL + A + D to background screen session.")
time.sleep(5)

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), password_salt)
    return hashed_password

def onPress(key):
    global Password
    try:
        if key.char in Allowed_chars:
            Password.append(key.char)
    except AttributeError:
        pass

def on_release(key):
    global Password
    global MouseEnabled
    global Alt_pressed_count

    '''if key == keyboard.Key.backspace:
        return False'''

    if key == keyboard.Key.enter:
        Formatted_Pass = ''.join(Password)
        pass_hash = hash_password(Formatted_Pass)
        #print(Formatted_Pass)
        if pass_hash.decode('utf-8') == Real_Pass_hash:
            return False
        else:
            Password.clear()
            pass
    elif key == keyboard.Key.alt:
        if MouseEnabled == True:
            print("Disabled mouse")
            global Mouse_Listener
            Mouse_Listener = mouse.Listener(suppress=True)
            Mouse_Listener.start()
            MouseEnabled = False

        Alt_pressed_count += 1
        if not Alt_pressed_count == 6:
            return
            
        elif MouseEnabled == False:
            print("Enabled Mouse")
            Mouse_Listener.stop()
            MouseEnabled = True
            Alt_pressed_count = 0

with keyboard.Listener(on_press = onPress, on_release = on_release,suppress=True) as listener:
    listener.join()