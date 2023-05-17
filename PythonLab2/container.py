from re import fullmatch
from json import load, dump, JSONEncoder
import copy
from for_input import yes_no_input, input_, mult_input

class Container:

    def __init__(self, *keys):
        self.__elements = set(keys)

    def add(self, key, *keys):
        if keys:
            self.__elements.update([key, *keys])
        else:
            self.__elements.update([key])

    def __iadd__(self, other: 'Container'):

        if other.__elements:
            self.__elements = self.__elements | other.__elements

        return self

    def remove(self, key):
        if key in self.__elements:
            return self.__elements.remove(key)
        else:
            print("There is no such element in the container!!!")

    def find(self, key, *keys):
        return list(self.__elements & set([key, *keys]))

    def get_List_elements(self):
        return [*self.__elements]

    def grep(self, pattern: str):
        return [r for r in self.__elements if fullmatch(pattern, r.__str__())]

    # def __str__(self):
    #     return str(self.__elements - {()})
    #
    # def __copy__(self):
    #     return Container(*self.__elements)

    def items(self):
        return [e for e in self.__elements if e]


class User:

    def __init__(self, user_name: str, *args):
        self.__user_name = {user_name: Container(args)}
        self.__current_user = user_name
        self.__current_collection = self.__user_name[user_name]

        # with open("for_container.json", "r+") as file_data:
        #     file_data.truncate()

    def add_user(self, user: str):
        if user not in self.__user_name.keys():
            self.__user_name[user] = Container()
            a = True
        else:
            a = False
        return a

    def switch_user(self, user_name: str):
        if user_name in self.__user_name:
            self.__current_user = user_name
            print("Do you want to load a container for this user or you"
                  " want to work with new empty container? Answer (Yes|No): ")
            save = yes_no_input()

            if save == "yes":
                self.__current_collection = self.__user_name[self.__current_user]
            else:
                self.__current_collection = Container()
        else:
            print("There is no such user!!!")

    def save_user(self):
        with open("for_container.json", "w") as file_data:
            dump(self, file_data, cls=UserCollectionEncoder, indent=4)

    def load_user(self):
        with open("for_container.json", "r") as file_data:
            data = load(file_data)
            user_name = self.__current_user
            if user_name not in data:
                print("User {} not found or you have not saved any user!!!".format(user_name))

    def load_Container(self):
        if self.__current_user:
            self.__current_collection += self.__user_name[self.__current_user]

    def save_Container(self):
        if self.__current_user:
            self.__user_name[self.__current_user] += self.__current_collection

    def add_keys(self, key):
        self.__current_collection.add(key)

    def remove_keys(self, keys):
        self.__current_collection.remove(keys)

    def find_key(self, key):
        return self.__current_collection.find(key)

    def find_grep(self, pat):
        return self.__current_collection.grep(pat)

    def get_collection(self):
        return self.__current_collection.items()

    # def __str__(self):
    #     return str({item[0]: str(item[1]) for item in self.__user_name.items()})

    def get_users(self):
        return copy.copy(self.__user_name)


class UserCollectionEncoder(JSONEncoder):
    def default(self, obj):
        return {item[0]: item[1].items() for item in obj.get_users().items()}


# def from_json(uc_dict):
#     new_dict = {item[0]: Container(*item[1]) for item in uc_dict.items()}
#     return new_dict
def containerr():
    user_name = input_(str, "Enter a user name: ")
    user = User(user_name)
    list_commands = "Switch command(only number of command):\n" \
                    "1)   Add user\n" \
                    "2)   Add element(s)\n" \
                    "3)   Remove element(s)\n" \
                    "4)   Find element(s)\n" \
                    "5)   Find by regular expression\n" \
                    "6)   Get list elements of current container\n" \
                    "7)   Switch user\n" \
                    "8)   Load from file\n" \
                    "9)   Save to file\n" \
                    "10)  Exit\n" \
                    "11)  Show list of commands\n"

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

            case 11:
                print(list_commands)
            case _:
                print("Such command is doesn't exist")


# if __name__ == "__main__":
#     container()
