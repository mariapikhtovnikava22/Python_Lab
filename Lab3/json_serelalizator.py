import types
from re import search, findall

def get_name_of_base_type(obj):
    pass


class JsonSerelizator:
    # serelization in str
    def dumps(self, obj):
        inf = dict()
        obj_type = type(obj)

        def get_name_of_PrimType():
            return search(r"\'([A-Za-z]+)\'", str(obj_type))[1]

        if isinstance(obj, (list, tuple, bytearray, set, bytearray, frozenset)):
            inf["type"] = get_name_of_PrimType()
            inf["value"] = [self.dumps(collection_obj) for collection_obj in obj]

        elif isinstance(obj, dict):
            inf["type"] = get_name_of_PrimType()
            inf["value"] = [[self.dumps(key), self.dumps(value)] for (key, value) in obj.items()]

        elif isinstance(obj, (str, int, bool, float, complex)):
            inf["type"] = get_name_of_PrimType()
            inf["value"] = obj

        elif not obj:
            inf["type"] = "NoneType"
            inf["value"] = None

        return inf

