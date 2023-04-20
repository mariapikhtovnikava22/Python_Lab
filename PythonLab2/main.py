from parse import parser
from container import User
from for_input import input_, mult_input

parser()

user_name = input_(str, "Enter a user name: ")
user = User(user_name)
list_commands = "Switch command(only number of command):\n" \
                   "1)   Add user\n" \
                   "2)   Add element(s)\n" \
                   "3)   Remove element(s)\n"\
                   "4)   Find element(s)\n" \
                   "5)   Find by regular expression\n" \
                   "6)   Get list elements of current container\n" \
                   "7)   Switch user\n" \
                   "8)   Load from file\n" \
                   "9)   Save to file\n" \
                   "10)  Exit\n"

print(list_commands)

while True:

    n = input_(int, "Switch command: ")
    match n:

        case 1:
            new_user = input_(str, "Enter a new user name: ")
            if not user.add_user(new_user):
                print("Such a user already exists!!!")

        case 2:
            arr = mult_input("Please enter the element(s) you want to add: ")
            if len(arr) == 0:
                print("You didn't enter elements!!!")
            else:
                for i in arr:
                    user.add_keys(i)

        case 3:
            arr = mult_input("Please enter the element(s) you want to delete: ")
            if len(arr) == 0:
                print("You didn't enter element(s)!!!")
            else:
                for i in arr:
                    user.remove_keys(i)
        case 4:
            elem = mult_input("Enter a element(s) which you want to find in the Container: ")
            elements = user.find_key(elem)
            if elements:
                print("There is no such element(s) in the container!!!")
            else:
                print(elements)

        case 5:
            pat = input_(str, "Enter a elem which you want to find in the Container by regular expression: ")

            elements = user.find_grep(pat)
            if not elements:
                print("There is no such element in the container!!!")
            else:
                print(elements)

        case 6:
            print(f"Elements of current collection: {user.get_collection()}")

        case 7:
            while True:
                save = input_(str, "Do you want to save the current Container?? Answer (Yes| No): ").lower().strip()
                if save != "yes":
                    if save != "no":
                        print("Please, enter Yes or No!")
                    else:
                        break
                else:
                    break
            if save == "yes":
                user.save_Container()

            user_name = input_(str, "Enter user name: ")
            user.switch_user(user_name)

        case 8:
            user.load_user()
            user.load_Container()
            print("Container successful load from file!!!")

        case 9:
            user.save_Container()
            user.save_user()
            print("Container successful save to file!!!")

        case 10:
            while True:
                save = input_(str, "Do you want to save the current container?? Answer (Yes| No): ").lower().strip()
                if save != "yes":
                    if save != "no":
                        print("Please, enter Yes or No!")
                    else:
                        break
                else:
                    break
            if save == "yes":
                user.save_user()
                user.save_Container()
            else:
                break
        case _:
            print("Such command is doesn't exist")

