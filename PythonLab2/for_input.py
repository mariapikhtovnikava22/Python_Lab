from enum import Enum
def get_user_inp():
    test_str = ''

    print("Please enter a text(enter 'стоп' to complete): ")

    while True:
        line = input()
        if not line:  # Проверяем, что строка пустая
            print("You have not entered the text please try again.")
            continue
        if line.lower().strip() == "стоп":
            break
        test_str += line + "\n"

    return test_str


def input_(type_of_inp: int | str, mess=''):
    if type_of_inp == int:
        while True:
            # input_str = input()
            try:
                inp = int(input(mess).strip())
                if inp < 0:
                    print("Please enter a positive number!!!")
                else:
                    break
            except ValueError:
                print("Error! You didn't enter a number. Try again!!!")
    else:
        while True:
            inp = input(mess)
            if len(inp) == 0:
                print("You haven't entered anything! Try again!!!")
            else:
                break

    return inp

def yes_no_input():
    while True:
        save = input().lower().strip()
        if save != "yes":
            if save != "no":
                print("Please enter Yes or no")
            else:
                break
        else:
            break
    return save

def mult_input(mess):
    arr = []
    for i in input(mess).split():
        arr.append(i)
    return arr


class Switch(Enum):
    sw1 = "ADD USER"
    sw2 = "ADD ELEMENTS"
    sw3 = "REMOVE ELEMENTS"
    sw4 = "FIND ELEMENTS"
    sw5 = "FIND BY REGEX"
    sw6 = "GET LIST"
    sw7 = "SWITCH"
    sw8 = "LOAD"
    sw9 = "SAVE"
    sw10 = "EXIT"

    @staticmethod
    def get_switch_inp(s: str):
        s = s.strip().lower()

        match s:

            case "add":
                return Switch.sw1
            case "add elements":
                return Switch.sw2
            case "remove elements":
                return Switch.sw3
            case "find elements":
                return Switch.sw4


