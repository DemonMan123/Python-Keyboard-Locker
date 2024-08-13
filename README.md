# Python-Keyboard-Locker
A custom Python program I wrote to lock they Keyboard/Mouse inputs. It requires you to type a password and press "Enter".

The program uses bcrypt and a fixed password salt. There's 2 files, "Generate hash" and "LockKeyboard".

Make sure to generate a hash with the "Generate_Hash.py" program first, then change the variable "Real_Pass_hash" value in the "LockKeyboard.py" file.

**WARNING**
--**CHANGE THE PASSWORD TO YOUR GENERATED HASH BEFORE YOU RUN LOCKKEYBOARD**--

**REQUIREMENTS**
bcrypt
pynput
