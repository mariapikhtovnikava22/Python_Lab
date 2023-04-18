from re import findall, fullmatch
class Container:

    def __init__(self, *keys):
        self.__elements = set(keys)

    def add(self, key, *keys):
        return self.__elements.update({key, *keys})

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

    def grep(self, regex):
        return [r for r in self.__elements if fullmatch(regex, str(r))]


class User:
    pass

