# defined_classes は、定義されたクラス名（文字列）をキーとして、クラス定義関数を格納するグローバル変数です。
defined_classes = {}
# defined_constructors は、定義されたクラスのコンストラクタをキーとして、クラス定義関数を格納するグローバル変数です。
defined_constructors = {}

def Class(class_definition_function):
    # もしコンストラクタが渡されたら、クラス定義関数を返す
    if class_definition_function in defined_constructors:
        return defined_constructors[class_definition_function]
    class_definition = class_definition_function()
    def generate_method(instance, function, args_count):
        # C# には「可変長ジェネリック型引数」（variadic generics）は存在せず、
        # Action<T1,...> や Func<T1,...> などは 最大16引数まで の型がフレームワーク側であらかじめ定義されています。
        # そのため、ここでも同様に最大16引数までのメソッドを個別に定義し、引数の数に応じて適切なメソッドを返すようにしています。
        # もし、それ以上の引数が必要な場合は、引数を配列や辞書などにまとめて1つの引数として渡すようにしてください。
        def method_no_args():
            def method():
                return function(instance)
            return method
        def method_one_arg():
            def method(arg):
                return function(instance, arg)
            return method
        def method_two_args():
            def method(arg1, arg2):
                return function(instance, arg1, arg2)
            return method
        def method_three_args():
            def method(arg1, arg2, arg3):
                return function(instance, arg1, arg2, arg3)
            return method
        def method_four_args():
            def method(arg1, arg2, arg3, arg4):
                return function(instance, arg1, arg2, arg3, arg4)
            return method
        def method_five_args():
            def method(arg1, arg2, arg3, arg4, arg5):
                return function(instance, arg1, arg2, arg3, arg4, arg5)
            return method
        def method_six_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6)
            return method
        def method_seven_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6, arg7)
            return method
        def method_eight_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
            return method
        def method_nine_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
            return method
        def method_ten_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)
            return method
        def method_eleven_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)
            return method
        def method_twelve_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12)
            return method
        def method_thirteen_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13)
            return method
        def method_fourteen_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14)
            return method
        def method_fifteen_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15)
            return method
        def method_sixteen_args():
            def method(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16):
                return function(instance, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16)
            return method
        method_mapping = {
            0: method_no_args(),
            1: method_one_arg(),
            2: method_two_args(),
            3: method_three_args(),
            4: method_four_args(),
            5: method_five_args(),
            6: method_six_args(),
            7: method_seven_args(),
            8: method_eight_args(),
            9: method_nine_args(),
            10: method_ten_args(),
            11: method_eleven_args(),
            12: method_twelve_args(),
            13: method_thirteen_args(),
            14: method_fourteen_args(),
            15: method_fifteen_args(),
            16: method_sixteen_args(),
        }
        return method_mapping[args_count]
    def register_special_methods(instance):
        def get_class():
            def method():
                return class_definition_function
            return method
        instance["class"] = get_class()
        def superclass():
            def method():
                if class_definition_function == defined_classes["Object"]:
                    return None
                super_class_definition_function = defined_classes["Object"]
                if "extends" in class_definition:
                    super_class_definition_function = defined_classes[class_definition["extends"]]
                return super_class_definition_function
            return method
        instance["superclass"] = superclass()
        def is_instance_of():
            def method(class_def_function):
                current_class_function = class_definition_function
                while True:
                    if current_class_function == class_def_function:
                        return True
                    if current_class_function == defined_classes["Object"]:
                        break
                    super_class_definition_function = defined_classes["Object"]
                    current_class_definition = current_class_function()
                    if "extends" in current_class_definition:
                        super_class_definition_function = defined_classes[current_class_definition["extends"]]
                    current_class_function = super_class_definition_function
                return False
            return method
        instance["is_a?"] = is_instance_of()
    def register_super_class_members(instance, super_class_definition_function):
        super_class_definition = super_class_definition_function()
        for member in super_class_definition["members"]:
            instance[member] = super_class_definition["members"][member]
    def register_super_class_methods(instance, super_class_definition_function):
        instance["super"] = {}
        super_class_definition = super_class_definition_function()
        for function_definition in super_class_definition["methods"]:
            function = function_definition[0]
            args_count = function_definition[1]
            function_name = str(function)
            if len(function_definition) != 2:
                function_name = function_definition[2]
            instance[function_name] = generate_method(instance, function, args_count)
            instance["super"][function_name] = instance[function_name]
    def setup_superclass_relations(instance, class_definition_function):
        if class_definition_function == defined_classes["Object"]:
            return
        super_class_definition_function = defined_classes["Object"]
        if "extends" in class_definition_function():
            super_class_definition_function = defined_classes[class_definition["extends"]]
        register_super_class_members(instance, super_class_definition_function)
        register_super_class_methods(instance, super_class_definition_function)
        setup_superclass_relations(instance, super_class_definition_function)
    def register_members(instance, class_definition):
        for member in class_definition["members"]:
            instance[member] = class_definition["members"][member]
    def register_methods(instance, class_definition):
        for function_definition in class_definition["methods"]:
            function = function_definition[0]
            args_count = function_definition[1]
            function_name = str(function)
            if len(function_definition) != 2:
                function_name = function_definition[2]
            instance[function_name] = generate_method(instance, function, args_count)
    def setup_instance(instance, class_definition):
        register_special_methods(instance)
        setup_superclass_relations(instance, class_definition_function)
        register_members(instance, class_definition)
        register_methods(instance, class_definition)
    def generate_class(args_count):
        def constructor_no_args():
            def constructor():
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"]()
                return instance
            return constructor
        def constructor_one_arg():
            def constructor(arg):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg)
                return instance
            return constructor
        def constructor_two_args():
            def constructor(arg1, arg2):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2)
                return instance
            return constructor
        def constructor_three_args():
            def constructor(arg1, arg2, arg3):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3)
                return instance
            return constructor
        def constructor_four_args():
            def constructor(arg1, arg2, arg3, arg4):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4)
                return instance
            return constructor
        def constructor_five_args():
            def constructor(arg1, arg2, arg3, arg4, arg5):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5)
                return instance
            return constructor
        def constructor_six_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6)
                return instance
            return constructor
        def constructor_seven_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7)
                return instance
            return constructor
        def constructor_eight_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
                return instance
            return constructor
        def constructor_nine_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
                return instance
            return constructor
        def constructor_ten_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)
                return instance
            return constructor
        def constructor_eleven_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)
                return instance
            return constructor
        def constructor_twelve_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12)
                return instance
            return constructor
        def constructor_thirteen_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13)
                return instance
            return constructor
        def constructor_fourteen_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14)
                return instance
            return constructor
        def constructor_fifteen_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15)
                return instance
            return constructor
        def constructor_sixteen_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16):
                instance = {}
                setup_instance(instance, class_definition)
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16)
                return instance
            return constructor
        constructor_mapping = {
            0: constructor_no_args(),
            1: constructor_one_arg(),
            2: constructor_two_args(),
            3: constructor_three_args(),
            4: constructor_four_args(),
            5: constructor_five_args(),
            6: constructor_six_args(),
            7: constructor_seven_args(),
            8: constructor_eight_args(),
            9: constructor_nine_args(),
            10: constructor_ten_args(),
            11: constructor_eleven_args(),
            12: constructor_twelve_args(),
            13: constructor_thirteen_args(),
            14: constructor_fourteen_args(),
            15: constructor_fifteen_args(),
            16: constructor_sixteen_args(),
        }
        return constructor_mapping[args_count]
    args_count = None
    for function_definition in class_definition["methods"]:
        function, function_args_count = function_definition
        if str(function) == "__init__":
            args_count = function_args_count
            break
    global defined_classes
    defined_classes[str(class_definition_function)] = class_definition_function
    constructor = generate_class(args_count)
    defined_constructors[constructor] = class_definition_function
    return constructor

def Object():
    def __init__(self):
        self["_hash"] = random() * (2 ** 53) // 1
        return self
    def hash(self):
        return self["_hash"]
    def itself(self):
        return self
    return {
        "members": { "_hash": None },
        "methods": { (__init__, 0), (hash, 0), (itself, 0) }
    }
Object = Class(Object)

def Queue():
    def __init__(self, list):
        self["super"]["__init__"]()
        self["queue"] = list or []
        return self
    def enqueue(self, args):
        item = args
        self["queue"].append(item)
        return enqueue
    def dequeue(self):
        return self["queue"].pop(0)
    return {
        "members": { "queue": [] },
        "methods": { (__init__, 1), (enqueue, 1), (dequeue, 0), }
    }
Queue = Class(Queue)
