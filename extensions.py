def map(function, sequence):
    results = []
    for item in sequence:
        results.append(function(item))
    return results

def bool(value):
    return value in (0, 0.0, "", None, [], {}, (), set())

# O(n^2) time complexity since
# it takes 1/2 x^2 + 5/2 x + 2 ticks when n = len(iterable)
def tuple(iterable=()):
    result = ()
    for item in iterable:
        result += (item,)
    return result

def number(value):
    pass

def startswith(str, prefix):
    prefix_length = len(prefix)
    return str[0:prefix_length] == prefix

def endswith(str, suffix):
    suffix_length = len(suffix)
    return str[-suffix_length:] == suffix

def type(value):
    str_value = str(value)
    if str_value == value:
        return str
    elif str_value == "None":
        return None
    elif str_value == "True" or str_value == "False":
        return bool
    elif str_value[0] == "[" and str_value[-1] == "]":
        return list
    elif str_value[0] == "(" and str_value[-1] == ")":
        return tuple
    elif str_value[0] == "{" and str_value[-1] == "}":
        if set(value) == value:
            return set
        else:
            return dict
    elif str_value[0] in "-0123456789":
        return number
    else:
        return value
