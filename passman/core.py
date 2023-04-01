import json
import random
import console_colors
import passman_encrypt as pe
from os import system, name


def generate(length,type):
    if type==1:
        password = generate_numeric(length)
    else:
        password = generate_special(length)
    return password


def generate_numeric(length):
    password = [str(int(random.random()*10)) for i in range(length)]
    return ''.join(password)


def generate_special(length):
    password = [chr(int(random.random()*94)+33) for i in range(length)]
    return ''.join(password)


def generate_alphanum(length):
    password = ''
    for i in range(length):
        char_type = random.randint(1,3)
        if char_type == 1:
            password += str(random.randint(0,9))
        elif char_type ==2:
            password += chr(random.randint(0,25)+ord('a'))
        elif char_type ==3:
            password += chr(random.randint(0,25)+ord('A'))
    return password