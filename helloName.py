from os import system
from time import sleep
clicked=False
system('cls')
iscorrect = False
while not iscorrect:
    name = f'Hello, {input("Enter your name: ")}! '    
    if name.isalpha:
        iscorrect = True
    
name = ' '.join(list(name))
while True:
    system('cls')
    print(name)
    name = f'{name[-1]}{name[:-1]}'
    sleep(0.5)
    
