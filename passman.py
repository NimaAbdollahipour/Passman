import json
import random
import console_colors
import passman_encrypt as pe
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


def generate(pass_len, t):
    if t == 1:
        password = generate_numeric(pass_len)
    elif t == 2:
        password = generate_special(pass_len)
    else:
        password = generate_alphanum(pass_len)
    return password


def generate_alphanum(pass_len):
    no_of_special = random.randint(pass_len)
    password = [chr(int(random.random() * 94) + 33) for i in range(length - no_of_special)]
    special_chars = [random.choice(['@', '#', "&", "*", "$", "?", "!"]) for i in range(no_of_special)]
    password += special_chars
    random.shuffle(password)
    return ''.join(password)


def generate_numeric(pass_len):
    password = [str(int(random.random() * 10)) for i in range(pass_len)]
    return ''.join(password)


def generate_special(pass_len):
    password = [chr(int(random.random() * 94) + 33) for i in range(pass_len)]
    return ''.join(password)


def save(password, username, host):
    data = dict()
    try:
        file = open("passwords.json", "+r")
        string = file.read()
        file.close()
        data = json.loads(string)
    except OSError:
        print("Error Reading the file")
    except TypeError:
        print("Empty")

    try:
        file_2 = open("passwords.json", "+w")
        data[pe.encrypt(host, PASSWORD)] = {"username": pe.encrypt(username, PASSWORD),
                                            "password": pe.encrypt(password, PASSWORD)}
        file_2.write(json.dumps(data))
        file_2.close()
    except OSError:
        print("Error writing the file")


def list_passwords():
    data = dict()
    data_dec = dict()
    try:
        file = open("passwords.json", "+r")
        string = file.read()
        file.close()
        data = json.loads(string)
    except OSError:
        print(console_colors.Red, "Error Reading the file")
    except TypeError:
        print(console_colors.Red, "Empty")

    for key, value in data.items():
        data_dec[pe.encrypt(key, PASSWORD)] = {"username": pe.encrypt(value['username'], PASSWORD),
                                               "password": pe.encrypt(value['password'], PASSWORD)}
    return data_dec


def show_passwords():
    data_dec = list_passwords()
    for k, v in data_dec.items():
        print(console_colors.Green)
        print("H: ", k)
        print("U: ", v['username'])
        print("P: ", v['password'])


def search(s):
    data = list_passwords()
    for k, v in data.items():
        if not k.find(s) == -1:
            print(console_colors.Green)
            print("H: ", k)
            print("U: ", v['username'])
            print("P: ", v['password'])
            return True
    print(console_colors.Yellow)
    print("Not Found!")
    return False


clear()
print(console_colors.Blue)
PASSWORD = pe.format_pass(input('ENTER YOUR PASSWORD:'))
while True:
    clear()
    print(console_colors.Blue)
    print("1.GENERATE PASSWORD:")
    print("2.SHOW ALL PASSWORDS:")
    print("3.SEARCH FOR A PASSWORD:")
    choice = input("SELECT: ")
    if choice == "1":
        print("1.Numeric:")
        print("2.Including Special Characters:")
        if input("YOUR CHOICE: ") == "1":
            length = int(input("LENGTH OF YOUR PASSWORD: "))
            p = generate(length, 1)
            h = input("NAME OF THE APP OR WEBSITE: ")
            u = input("USERNAME: ")
            save(p, u, h)
        else:
            length = int(input("LENGTH OF YOUR PASSWORD: "))
            p = generate(length, 2)
            h = input("NAME OF THE APP OR WEBSITE: ")
            u = input("USERNAME: ")
            save(p, u, h)
    elif choice == "2":
        show_passwords()
    elif choice == "3":
        search(input('WHAT YOU WANT TO SEARCH:'))
    else:
        print(console_colors.Red)
        print("WRONG CHOICE")
    input("PRESS ENTER TO CONTINUE>>")
