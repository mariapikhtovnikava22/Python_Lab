import json
from re import fullmatch
from json import load, dump

class Container:

    def __init__(self, *keys):
        self.__elements = set(keys)

    def add(self, key, *keys):
        return self.__elements.update({key, *keys})

    def __iadd__(self, other: 'Container'):
        return self.__elements | other.__elements

    def remove(self, key, *args):
        if len(args):
            print("you are trying to delete more than one key!!!")
            return
        if key not in self.__elements:
            print("You are trying to delete a non-existent key!!!")
            return
        else:
            return self.__elements.remove(key)

    def find(self, key, *keys):
        return list(self.__elements & set([key, *keys]))

    def get_List_elements(self):
        return list(self.__elements)

    def items(self):
        return [*self.__elements]

    def grep(self, pattern: str):
        return [r for r in self.__elements if fullmatch(str, r.__str__())]


class User:

    def __init__(self, user_name):
        self.__user_name = {user_name: Container()}
        self.__current_user = user_name
        self.__current_collection = self.__user_name[user_name]

        with open("for_container.json", "r+") as file_data:
            file_data.truncate()

    def add_user(self, user: str):
        if user in self.__user_name.keys():
            print("Such a user exists")
            return
        else:
            self.__user_name[user] = Container()

    def save_user(self):
        with open("for_container.json", "r+") as file_data:
            json.JSONDecoder.decode(self)

    def load_user(self):
        pass

    def load_Container(self):
        if self.__current_user:
            self.__current_collection += self.__user_name[self.__current_collection]

    def save_Container(self):
        if self.__current_user:
            self.__user_name[self.__current_collection] += self.__current_collection

    def add_keys(self, key, *keys):
        self.__current_collection.add(key, keys)

    def remove_keys(self, keys):
        self.__current_collection.remove(keys)

    def find_key(self, key):
        return self.__current_collection.find(key)

    def find_grep(self, pat):
        return self.__current_collection.grep(pat)
