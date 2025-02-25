printed = False

while not printed:
    user_input = input("Write hello world: ")
    if user_input == "hello world":
        print(user_input)
        break
    else:
        while True:
            user_input = input("You must write hello world: ")
            if user_input == "hello world":
                print("Good, now write it like that")
                break
