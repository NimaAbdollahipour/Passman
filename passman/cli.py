def main_loop():
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
            if input("YOUR CHOICE: ")=="1":
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
        elif choice=="2":
            show_passwords()
        elif choice=="3":
            search(input('WHAT YOU WANT TO SEARCH:'))
        else:
            print(console_colors.Red)
            print("WRONG CHOICE")
        input("PRESS ENTER TO CONTINUE>>")