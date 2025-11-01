

def Class(class_definition_function):
    class_definition = class_definition_function()
    instance = {}
    def generate_method(function, args_count):
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
    def generate_class(instance, args_count):
        def constructor_no_args():
            def constructor():
                instance["__init__"](instance)
                return instance
            return constructor
        def constructor_one_arg():
            def constructor(arg):
                instance["__init__"](arg)
                return instance
            return constructor
        def constructor_two_args():
            def constructor(arg1, arg2):
                instance["__init__"](arg1, arg2)
                return instance
            return constructor
        def constructor_three_args():
            def constructor(arg1, arg2, arg3):
                instance["__init__"](arg1, arg2, arg3)
                return instance
            return constructor
        def constructor_four_args():
            def constructor(arg1, arg2, arg3, arg4):
                instance["__init__"](arg1, arg2, arg3, arg4)
                return instance
            return constructor
        def constructor_five_args():
            def constructor(arg1, arg2, arg3, arg4, arg5):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5)
                return instance
            return constructor
        def constructor_six_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6)
                return instance
            return constructor
        def constructor_seven_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7)
                return instance
            return constructor
        def constructor_eight_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
                return instance
            return constructor
        def constructor_nine_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
                return instance
            return constructor
        def constructor_ten_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)
                return instance
            return constructor
        def constructor_eleven_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)
                return instance
            return constructor
        def constructor_twelve_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12)
                return instance
            return constructor
        def constructor_thirteen_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13)
                return instance
            return constructor
        def constructor_fourteen_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14)
                return instance
            return constructor
        def constructor_fifteen_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15):
                instance["__init__"](arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15)
                return instance
            return constructor
        def constructor_sixteen_args():
            def constructor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16):
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

    constructor_definition = None
    for member in class_definition["members"]:
        instance[member] = class_definition["members"][member]
    for function_definition in class_definition["methods"]:
        function, args_count = function_definition
        instance[str(function)] = generate_method(function, args_count)
        if str(function) == "__init__":
            constructor_definition = function_definition
    _, args_count = constructor_definition
    return generate_class(instance, args_count)

def Queue():
    def __init__(self, list = []):
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
begin = get_tick_count()
q = Queue([])
end = get_tick_count()
print(end - begin)
q["enqueue"](1)
q["enqueue"](2)
print(q["queue"])
