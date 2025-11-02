from pquery import *
from test import *

obj1 = Object()
obj2 = Object()

test("itself is equal to itself", expected_to(eq, obj1, obj1))
test("different objects are not equal", expected_to(not_eq, obj1, obj2))

queue = Queue([1, 2, 3])
queue = Queue([])

test("queue pop returns first element", expected_to(eq, queue["dequeue"](), 1))
test("queue pop returns first element", expected_to(eq, queue["dequeue"](), 2))
test("queue pop returns first element", expected_to(eq, queue["dequeue"](), 3))

report()
