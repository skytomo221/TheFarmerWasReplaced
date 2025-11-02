from pquery import *
from test import *

obj1 = Object()
obj2 = Object()

test("itself is equal to itself", expected_to(eq, obj1, obj1))
test("different objects are not equal", expected_to(not_eq, obj1, obj2))
test("object hash is consistent", expected_to(eq, obj1["hash"](), obj1["hash"]()))
test("different objects have different hashes", expected_to(not_eq, obj1["hash"](), obj2["hash"]()))
test("object class is Object", expected_to(eq, str(obj1["class"]()), "Object"))
test("objects have the same class", expected_to(eq, obj1["class"](), obj2["class"]()))

queue = Queue([1, 2, 3])
queue2 = Queue([])

test("queue pop returns first element", expected_to(eq, queue["dequeue"](), 1))
test("queue pop returns first element", expected_to(eq, queue["dequeue"](), 2))
test("queue pop returns first element", expected_to(eq, queue["dequeue"](), 3))

def TestClass():
  def method_no_args(self):
    return 0
  def method_one_arg(self, arg):
    return arg
  def method_two_args(self, arg1, arg2):
    return arg1 + arg2
  def method_three_args(self, arg1, arg2, arg3):
    return arg1 + arg2 + arg3
  def method_four_args(self, arg1, arg2, arg3, arg4):
    return arg1 + arg2 + arg3 + arg4
  def method_five_args(self, arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5
  def method_six_args(self, arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6
  def method_seven_args(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7
  def method_eight_args(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8
  def method_nine_args(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8 + arg9
  def method_ten_args(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8 + arg9 + arg10
  def method_eleven_args(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8 + arg9 + arg10 + arg11
  def method_twelve_args(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8 + arg9 + arg10 + arg11 + arg12
  def method_thirteen_args(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8 + arg9 + arg10 + arg11 + arg12 + arg13
  def method_fourteen_args(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8 + arg9 + arg10 + arg11 + arg12 + arg13 + arg14
  def method_fifteen_args(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8 + arg9 + arg10 + arg11 + arg12 + arg13 + arg14 + arg15
  def method_sixteen_args(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8 + arg9 + arg10 + arg11 + arg12 + arg13 + arg14 + arg15 + arg16
  def __init__(self, num):
    self["super"]["__init__"]()
    self["num"] = num
  def is_even(self):
    return self["num"] % 2 == 0
  return {
    "members": { "num": None },
    "methods": [
      (method_no_args, 0),
      (method_one_arg, 1),
      (method_two_args, 2),
      (method_three_args, 3),
      (method_four_args, 4),
      (method_five_args, 5),
      (method_six_args, 6),
      (method_seven_args, 7),
      (method_eight_args, 8),
      (method_nine_args, 9),
      (method_ten_args, 10),
      (method_eleven_args, 11),
      (method_twelve_args, 12),
      (method_thirteen_args, 13),
      (method_fourteen_args, 14),
      (method_fifteen_args, 15),
      (method_sixteen_args, 16),
      (__init__, 1),
      (is_even, 0, "even?")
    ]
  }
TestClass = Class(TestClass)

test_class = TestClass(42)
test("method with no args returns 0", expected_to(eq, test_class["method_no_args"](), 0))
test("method with one arg returns the arg", expected_to(eq, test_class["method_one_arg"](1), 1))
test("method with two args returns their sum", expected_to(eq, test_class["method_two_args"](1, 2), 3))
test("method with three args returns their sum", expected_to(eq, test_class["method_three_args"](1, 2, 3), 6))
test("method with four args returns their sum", expected_to(eq, test_class["method_four_args"](1, 2, 3, 4), 10))
test("method with five args returns their sum", expected_to(eq, test_class["method_five_args"](1, 2, 3, 4, 5), 15))
test("method with six args returns their sum", expected_to(eq, test_class["method_six_args"](1, 2, 3, 4, 5, 6), 21))
test("method with seven args returns their sum", expected_to(eq, test_class["method_seven_args"](1, 2, 3, 4, 5, 6, 7), 28))
test("method with eight args returns their sum", expected_to(eq, test_class["method_eight_args"](1, 2, 3, 4, 5, 6, 7, 8), 36))
test("method with nine args returns their sum", expected_to(eq, test_class["method_nine_args"](1, 2, 3, 4, 5, 6, 7, 8, 9), 45))
test("method with ten args returns their sum", expected_to(eq, test_class["method_ten_args"](1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 55))
test("method with eleven args returns their sum", expected_to(eq, test_class["method_eleven_args"](1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), 66))
test("method with twelve args returns their sum", expected_to(eq, test_class["method_twelve_args"](1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), 78))
test("method with thirteen args returns their sum", expected_to(eq, test_class["method_thirteen_args"](1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), 91))
test("method with fourteen args returns their sum", expected_to(eq, test_class["method_fourteen_args"](1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), 105))
test("method with fifteen args returns their sum", expected_to(eq, test_class["method_fifteen_args"](1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), 120))
test("method with sixteen args returns their sum", expected_to(eq, test_class["method_sixteen_args"](1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), 136))
test("is_even returns true for even numbers", expected_to(eq, test_class["even?"](), True))

def TestClass2():
  def __init__(self):
    self["super"]["__init__"]()
  def test2_method(self):
    return "TestClass2 method called"
  return {
    "members": { },
    "methods": [
      (__init__, 0),
      (test2_method, 0)
    ]
  }
TestClass2 = Class(TestClass2)

def TestClass3():
  def __init__(self):
    self["super"]["__init__"]()
  def test3_method(self):
    return "TestClass3 method called"
  return {
    "extends": "TestClass2",
    "members": { },
    "methods": [
      (__init__, 0),
      (test3_method, 0)
    ]
  }
TestClass3 = Class(TestClass3)

t2 = TestClass2()
t3 = TestClass3()

test("TestClass3 inherits from TestClass2", expected_to(eq, t3["test2_method"](), "TestClass2 method called"))
test("TestClass3 method works", expected_to(eq, t3["test3_method"](), "TestClass3 method called"))
test("TestClass3 is instance of TestClass3", expected_to(eq, t3["is_a?"](t3["class"]()), True))
test("TestClass3 is instance of TestClass2", expected_to(eq, t3["is_a?"](t2["class"]()), True))

report()
