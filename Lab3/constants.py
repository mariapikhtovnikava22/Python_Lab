PRIMITIVE_TYPE = (str, int, bool, float, complex)
PRIMITIVE_COLLECTIONS = (list, tuple, bytearray, set, bytes, frozenset)
PRIMITIVE_DATA = (PRIMITIVE_COLLECTIONS, PRIMITIVE_TYPE, dict)
CODE_OBJ = ("co_argcount",         # number of arguments (not including keyword only arguments, * or **args)
            "co_posonlyargcount",  #
            "co_kwonlyargcount",   # number of keyword only arguments (not including ** arg)
            "co_nlocals",          # number of local variables
            "co_stacksize",        # virtual machine stack space required
            "co_flags",            # bitmap of CO_* flags, read more here
            "co_code",             # string of raw compiled bytecode
            "co_consts",           # tuple of constants used in the bytecode
            "co_names",            # tuple of names of local variables
            "co_varnames",         # tuple of names of arguments and local variables
            "co_filename",         # name of file in which this code object was created
            "co_name",             # name with which this code object was defined
            "co_firstlineno",      # number of first line in Python source code
            "co_lnotab",           # encoded mapping of line numbers to bytecode indices
            "co_freevars",         # tuple of names of free variables (referenced via a function's closure)
            "co_cellvars")         # tuple of names of cell variables (referenced by containing scopes)