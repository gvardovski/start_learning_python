def hello_world():
    print("Hello world!")

hello_world()

def sum(num1 = 1, num2 = 2):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

print(sum(""))

def multi_items(*args):
    print(args)
    print(type(args))

multi_items("Dave", "", 0, None)

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "dvasdf", last = None)