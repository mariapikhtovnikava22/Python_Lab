import inspect
import types
from re import search
from constants import PRIMITIVE_COLLECTIONS, PRIMITIVE_DATA, PRIMITIVE_TYPE,\
    CODE_OBJ, PRIMITIVE_COLLECTIONS_STR, PRIMITIVE_TYPE_STR
from inspect import getmembers, isroutine, ismethod, isfunction, isclass


def get_name_of_PrimType(obj_type):
    return search(r"\'([A-Za-z]+)\'", str(obj_type))[1]


class JsonSerelizator:
    def dumps(self, obj):
        inf = dict()
        if isinstance(obj, PRIMITIVE_DATA):
            return self.serelization_PrimType(obj)
        if isroutine(obj):
            inf['type'] = 'function'
            inf['value'] = self.serelization_Func(obj)
            return inf
        elif isinstance(obj, types.CodeType):
            inf['type'] = 'code'
            args = {k: self.dumps(v) for (k, v) in getmembers(obj) if k in CODE_OBJ}
            inf["value"] = args
            return inf
        elif isinstance(obj, types.ModuleType):
            inf['type'] = 'module'
            inf['value'] = self.dumps(obj.__name__)
            return inf
        elif isinstance(obj, types.CellType):
            inf['type'] = 'cell'
            inf['value'] = self.dumps(obj.cell_contents)
            return inf

        # elif isinstance(obj, types.GeneratorType):
        #     inf['type'] = 'generator'
        #     inf['value'] =

        elif isclass(obj):
            inf['type'] = 'class'
            inf['value'] = self.serealize_Class(obj)
            return inf
        elif not obj:
            inf["type"] = "NoneType"
            inf["value"] = 'Null'
            return inf
        else:
            inf['type'] = 'object'
            inf['value'] = self.serelization_Obj(obj)
            return inf

    def serelization_Obj(self, obj):

        inf = dict()
        inf['__class__'] = self.dumps(obj.__class__)
        members = dict()

        for k, v in getmembers(obj):
            if k.startswith("__") or isfunction(v) or ismethod(v):
                continue

            members[k] = self.dumps(v)

        inf['__members__'] = members

        return inf

    def serealize_Class(self, obj):
        inf = dict()
        inf['__name__'] = self.dumps(obj.__name__)

        for ve in obj.__dict__:
            v = [ve, obj.__dict__[ve]]
            if (v[0] in ("__name__", "__base__",
                              "__basicsize__", "__dictoffset__", "__class__") or
                    type(v[1]) in (
                            types.WrapperDescriptorType,
                            types.MethodDescriptorType,
                            types.BuiltinFunctionType,
                            types.GetSetDescriptorType,
                            types.MappingProxyType
                    )):
                continue

            if isinstance(obj.__dict__[v[0]], staticmethod) and v[1].__func__ is not None:
                inf[v[0]] = {"type": "staticmethod",
                                  "value": {"type": "function",
                                            "value": self.serelization_Func(v[1].__func__, obj)}}
            elif isinstance(obj.__dict__[v[0]], classmethod) and v[1].__func__ is not None:
                inf[v[0]] = {"type": "classmethod",
                                  'value': {"type": "function",
                                            "value": self.serelization_Func(v[1].__func__, obj)}}
            elif ismethod(v[1]):
                inf[v[0]] = self.serelization_Func(v[1].__func__, obj)

            elif isfunction(v[1]):
                inf[v[0]] = {"type": "function", "value": self.serelization_Func(v[1], obj)}
            else:
                inf[v[0]] = self.dumps((v[1]))

        inf["__bases__"] = {'type': 'tuple', 'value': [self.dumps(base) for base in obj.__bases__ if base != object]}

        return inf

    def serelization_PrimType(self, obj):
        inf = dict()
        obj_type = type(obj)

        if isinstance(obj, PRIMITIVE_COLLECTIONS):
            inf["type"] = get_name_of_PrimType(obj_type)
            inf["value"] = [self.dumps(collection_obj) for collection_obj in obj]

        elif isinstance(obj, dict):
            inf["type"] = get_name_of_PrimType(obj_type)
            inf["value"] = [self.dumps([key, value]) for (key, value) in obj.items()]

        elif isinstance(obj, PRIMITIVE_TYPE):
            inf["type"] = get_name_of_PrimType(obj_type)
            inf["value"] = obj

        return inf

    def serelization_Func(self, obj, cls=None):
        if not inspect.isfunction(obj):
            return

        inf = dict()
        inf["__name__"] = obj.__name__
        inf["__globals__"] = self.glob_vars(obj, cls)

        args = dict()

        for k, v in getmembers(obj.__code__):
            if k in CODE_OBJ:
                args[k] = self.dumps(v)

        inf["__code__"] = args

        if obj.__closure__:
            inf["__closure__"] = self.dumps(obj.__closure__)
        else:
            inf["__closure__"] = self.dumps(tuple())

        return inf

    def glob_vars(self, obj, cls=None):

        global_vars = dict()

        for glob in obj.__code__.co_names:
            if glob in obj.__globals__:
                if isinstance(obj.__globals__[glob], types.ModuleType):
                    global_vars["module " + glob] = self.dumps(obj.__globals__[glob].__name__)
                elif isclass(obj.__globals__[glob]):
                    if (cls and obj.__globals__[glob] != cls) or (not cls):
                        global_vars[glob] = self.dumps(obj.__globals__[glob])
                elif glob != obj.__code__.co_name:
                    global_vars[glob] = self.dumps(obj.__globals__[glob])
                else:
                    global_vars[glob] = self.dumps(obj.__name__)

        return global_vars

    def loads(self, obj):
        if obj['type'] in PRIMITIVE_TYPE_STR:
            return self.get_PrimType(obj['value'], obj['type'])
        elif obj['type'] in PRIMITIVE_COLLECTIONS_STR:
            return self.get_collection(obj['type'], obj['value'])
        elif obj['type'] == 'function':
            return self.deser_func(obj['value'])
        elif obj['type'] == 'dict':
            return dict(self.get_collection('list', obj['value']))
        elif obj['type'] == 'module':
            return __import__(obj['value'])
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
        elif obj['type'] == 'cell':
            return types.CellType(self.loads(obj['value']))
        elif obj['type'] == 'class':
            return self.deser_class(obj['value'])

        elif obj["type"] == "staticmethod":
            return staticmethod(self.loads(obj["value"]))

        elif obj["type"] == "classmethod":
            return classmethod(self.loads(obj["value"]))

        elif obj["type"] == "object":
            return self.deser_obj(obj["value"])

    def deser_obj(self, obj):
        clas = self.loads(obj['__class__'])
        members = dict()

        for k, v in obj['__members__'].items():
            members[k] = self.loads(v)

        inf = object.__new__(clas)
        inf.__dict__ = members

        return inf

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
        closuree = obj['__closure__']

        for v in obj["__globals__"]:

            if 'module' in v:
                glob_in_func[globalss[v]['value']] = __import__(globalss[v]['value'])

            elif globalss[v] != obj["__name__"]:
                glob_in_func[v] = self.loads(globalss[v])

        closur = tuple(self.loads(closuree))

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

        Func_Obj = types.FunctionType(code=codeType, globals=glob_in_func, closure=closur)
        Func_Obj.__globals__.update({Func_Obj.__name__: Func_Obj})

        return Func_Obj

    def deser_class(self, obj):
        bases = self.loads(obj["__bases__"])
        members = dict()

        for member, value in obj.items():
            # print(member, value)
            members[member] = self.loads(value)

        clas = type(self.loads(obj["__name__"]), bases, members)

        # чтоб не было бесконечной рекурсии метода и класса
        for k, member in members.items():
            if isinstance(member, types.FunctionType):
                member.__globals__.update({clas.__name__: clas})

            elif isinstance(member, (staticmethod, classmethod)):
                member.__func__.__globals__.update({clas.__name__: clas})

        return clas
        

