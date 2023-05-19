import types
from re import search
from constants import PRIMITIVE_COLLECTIONS, PRIMITIVE_DATA, PRIMITIVE_TYPE, CODE_OBJ
from inspect import getmembers, iscode


def get_name_of_PrimType(obj_type):
    return search(r"\'([A-Za-z]+)\'", str(obj_type))[1]


class JsonSerelizator:
    def dumps(self, obj):
        inf = dict()
        if isinstance(obj, PRIMITIVE_DATA):
            return self.serelization_PrimType(obj)
        if isinstance(obj, types.FunctionType):
            inf['type'] = 'function'
            inf['value'] = self.serelization_Func(obj)
            return inf
        if iscode(obj):
            inf['type'] = 'code'
            args = {k: self.dumps(v) for (k, v) in getmembers(obj.__code__) if k in CODE_OBJ}
            inf["value"] = args
        elif not obj:
            inf["type"] = "NoneType"
            inf["value"] = None
            return inf
        else:
            inf["type"] = "NoneType"
            inf["value"] = None
            return inf

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

        else:
            inf["type"] = "NoneType"
            inf["value"] = None

        return inf

    def serelization_Func(self, obj):

        inf = dict()
        inf["__name__"] = obj.__name__
        inf["__globals__"] = self.glob_vars(obj)
        args = {k: self.dumps(v) for (k, v) in getmembers(obj.__code__) if k in CODE_OBJ}
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

    def loads(self, obj):
        if obj['type'] in str(PRIMITIVE_TYPE):
            return self.get_PrimType(obj['value'], obj['type'])
        elif obj['type'] in str(PRIMITIVE_COLLECTIONS):
            return self.get_collection(obj['type'], obj['value'])
        elif obj['type'] == 'function':
            return self.deser_func(obj['value'])
        elif obj['type'] == 'code':
            code = obj['value']
            return types.CodeType(self.loads(code["co_argcount"]),
                                  self.loads(code["co_posonlyargcount"]),
                                  self.loads(code["co_kwonlyargcount"]),
                                  self.loads(code["co_nlocals"]),
                                  self.loads(code["co_stacksize"]),
                                  self.loads(code["co_flags"]),
                                  self.loads(code["co_code"]),
                                  self.loads(code["co_consts"]),
                                  self.loads(code["co_names"]),
                                  self.loads(code["co_varnames"]),
                                  self.loads(code["co_filename"]),
                                  self.loads(code["co_name"]),
                                  self.loads(code["co_firstlineno"]),
                                  self.loads(code["co_lnotab"]),
                                  self.loads(code["co_freevars"]),
                                  self.loads(code["co_cellvars"]))

    def get_PrimType(self, obj, typee):
        if typee == 'int':
            return int(obj)
        elif typee == 'float':
            return float(obj)
        elif typee == 'str':
            return str(obj)
        elif typee == 'complex':
            return complex(obj)
        elif typee == 'bool':
            return bool(obj)

    def get_collection(self, typee, obj):
        if typee == 'list':
            return list(self.loads(col_obj) for col_obj in obj)
        elif typee == 'tuple':
            return tuple(self.loads(col_obj) for col_obj in obj)
        elif typee == 'set':
            return set(self.loads(col_obj) for col_obj in obj)
        elif typee == 'frozenset':
            return frozenset(self.loads(col_obj) for col_obj in obj)
        elif typee == 'bytearray':
            return bytearray(self.loads(col_obj) for col_obj in obj)
        elif typee == 'bytes':
            return bytes(self.loads(col_obj) for col_obj in obj)

    def deser_func(self, obj):

        code = obj['__code__']
        globalss = obj['__globals__']
        glob_in_func = dict()

        for v in globalss:

            if 'module' in v:
                glob_in_func[globalss[v]['value']] = __import__(globalss[v]['value'])

            elif globalss[v] != obj["__name__"]:
                glob_in_func[v] = self.loads(globalss[v])

        codeType = types.CodeType(self.loads(code["co_argcount"]),
                                  self.loads(code["co_posonlyargcount"]),
                                  self.loads(code["co_kwonlyargcount"]),
                                  self.loads(code["co_nlocals"]),
                                  self.loads(code["co_stacksize"]),
                                  self.loads(code["co_flags"]),
                                  self.loads(code["co_code"]),
                                  self.loads(code["co_consts"]),
                                  self.loads(code["co_names"]),
                                  self.loads(code["co_varnames"]),
                                  self.loads(code["co_filename"]),
                                  self.loads(code["co_name"]),
                                  self.loads(code["co_firstlineno"]),
                                  self.loads(code["co_lnotab"]),
                                  self.loads(code["co_freevars"]),
                                  self.loads(code["co_cellvars"]))

        Func_Obj = types.FunctionType(code=codeType, globals=glob_in_func)
        Func_Obj.__globals__.update({Func_Obj.__name__: Func_Obj})

        return Func_Obj

