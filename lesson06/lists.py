users = ['DAVE', 'John', 'Sara']
data = ['Dave', 42, True]
empty = []
print("DAVE" in users)
print("DAVE" in empty)
print(users[0])
print(users[-1])
print(users.index('Sara'))
print(users[0:2])
print(users[-3:-1])
print(len(data))
users.append('Elsa')
print(users)
users += ['Json']
print(users)
users.extend(['Robert'])
print(users)
#users.extend(data)
#print(users)
users.insert(0, 'Bob')
print(users)
users[2:2] = ['Edi', 'Alex']
print(users)
users[1:3] = ['JPJ', 'Elis']
print(users)

users.remove('Bob')
print(users)
print(users.pop())
print(users)

del users[0]
print(users)

#del data[]
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)
users.sort(key = str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse=False))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(numscopy)
mynums.sort()
print(mynums)
print(mycopy)

print(type(nums))

mylist = list([1, 'Nail', True])
print(mylist)

#Tuples

mytuples = tuple(('Dave', 42, True))
tuples1 = (1, 2, 3, 4)

print(mytuples)
print(type(mytuples))

newlist = list(mytuples)
newlist.append('Neil')
newteuple = tuple(newlist)
print(newteuple)

print(tuples1.count(3))