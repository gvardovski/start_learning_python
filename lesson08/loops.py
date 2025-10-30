#value = 1
#while value <= 10:
#    value += 1
#    if value == 5:
#        continue
#    print(value)
#else:
#   print("Value is now = " + str(value))

# names = ["dave", "Sara", "john"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# for x in range(4):
#     print(x)
# for x in range(2,4):
#     print(x)
for x in range(0,101,5):
    print(x)
else:
    print("Glad thst\'s over")

names = ["dave", "Sara", "john"]
actions = ['Eat', 'sleep', 'codes']
# for name in names:
#     for act in actions:
#         print(name + ' ' + act)
for act in actions:
    for name in names:
        print(name + ' ' + act)