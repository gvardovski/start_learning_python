band = {
    "vokals": "Plant",
    "guitar": "Page",
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(len(band))
print(type(band))

#acces items
print(band["vokals"])
print(band.get("guitar"))

#list keys
print(band.keys())

#list all values
print(band.values())

#list of keys or values pairs as tuples
print(band.items())

#verify if the key exist in the dictionary
print("guitar" in band)
print("dsg" in band)

#change value
band["vokals"] = "Coverdale"
band.update({"base": "JPJ"})
print(band)

#Remove items
print(band.pop("base"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

#delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)
del band2

#copy dictionaries
# band2 = band #reference

# band2["drums"] = "Bonham"
# print(band)

band2 = band.copy()
band2["drums"] = "Bonham"
print(band2)

band3 = dict(band)
print(band3)

# NEsted dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

#sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#No duplicates allowed
nums = {1, 2, 2, 3}
print(nums)

#True is a dupe of 1, False is a dup of 0
nums = {1, True, 2, 0, 3, 4, False}
print(nums)

#check is a value is in a set
print(2 in nums)

#but you can not refer to an ellement in a set with an insex or a key

#add a new ellement to a set 
nums.add(8)
print(nums)

#add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

#update with lists, tuples, and dictionaries, too

#merge two sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}
newset = one.union(two)
print(newset)

#keep only duples from two sets
one = {1, 2, 3}
two = {4, 23, 2}

one.intersection_update(two)
print(one)

#keep everything exept the duplicates
one = {1, 2, 3}
two = {4, 23, 2}

one.symmetric_difference_update(two)
print(one)