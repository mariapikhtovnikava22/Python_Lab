import types
from re import search
from constants import PRIMITIVE_COLLECTIONS, PRIMITIVE_DATA, PRIMITIVE_TYPE, CODE_OBJ
from inspect import getmembers


def get_name_of_PrimType(obj_type):
    return search(r"\'([A-Za-z]+)\'", str(obj_type))[1]


class JsonSerelizator:
    def dumps(self, obj):
        if isinstance(obj, PRIMITIVE_DATA):
            return self.serelization_PrimType(obj)
        if isinstance(obj, types.FunctionType):
            return self.serelization_Func(obj)

    def serelization_PrimType(self, obj):
        inf = dict()
        obj_type = type(obj)

        if isinstance(obj, PRIMITIVE_COLLECTIONS):
            inf["type"] = get_name_of_PrimType(obj_type)
            inf["value"] = [self.dumps(collection_obj) for collection_obj in obj]

        elif isinstance(obj, dict):
            inf["type"] = get_name_of_PrimType(obj_type)
            inf["value"] = [[self.dumps(key), self.dumps(value)] for (key, value) in obj.items()]

        elif isinstance(obj, PRIMITIVE_TYPE):
            inf["type"] = get_name_of_PrimType(obj_type)
            inf["value"] = obj

        elif not obj:
            inf["type"] = "NoneType"
            inf["value"] = None

        return inf

    def serelization_Func(self, obj):
        inf = dict()
        inf["__name__"] = obj.__name__
        inf["__globals__"] = self.glob_vars(obj)
        args = {k: v for k, v in getmembers(obj.__code__) if k in CODE_OBJ}
        inf["__code__"] = args

        if obj.__closure__:
            inf["__closure__"] = self.dumps(obj.__closure__)
        else:
            inf["__closure__"] = self.dumps(tuple())

        return inf

    def glob_vars(self, obj):

        global_vars = dict()

        for glob in obj.__code__.co_names:
            if glob in obj.__globals__:
                if isinstance(obj.__globals__[glob], types.ModuleType):
                    global_vars["module " + glob] = self.dumps(obj.__globals__[glob].__name__)
                elif glob != obj.__code__.co_name:
                    global_vars[glob] = self.dumps(obj.__globals__[glob])
                else:
                    global_vars[glob] = self.dumps(obj.__name__)

            return global_vars



