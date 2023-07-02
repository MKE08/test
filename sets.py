# sets: unordered, mutable, no duplcates

my_set = {"apple", "banana", "cherry"}
print(my_set)
print(type(my_set)) #type set

# set does not allow duplicate 
my_set = {"apple", "banana", "cherry", "cherry"}
print(my_set)
print(type(my_set)) #type set

# or use the set function and create from an iterable, e.g. list, tuple, string
my_set_2 = set(["one", "two", "three"])
my_set_2 = set(("one", "two", "three"))
print(my_set_2)

# to know how many differents characters are in the word
my_set_3 = set("aaabbbcccdddeeeeeffff")
print(my_set_3)

# careful: an empty set cannot be created with {}, as this is interpreted as dict
# use set() instead
a = {}
print(type(a))
a = set()
print(type(a))

 # Add elements
my_set = set()

# use the add() method to add elements
my_set.add(42)
my_set.add(True)
my_set.add("Hello")

# note: the order does not matter, and might differ when printed
print(my_set)

# nothing happens when the element is already present:
my_set.add(42)
print(my_set)

# Remove elements
# remove(x): removes x, raises a KeyError if element is not present
my_set = {"apple", "banana", "cherry"}
my_set.remove("apple")
print(my_set)

# KeyError:
# my_set.remove("orange")

# discard(x): removes x, does nothing if element is not present
my_set.discard("cherry")
my_set.discard("blueberry")
print(my_set)

# clear() : remove all elements
my_set.clear()
print(my_set)

# pop() : return and remove a random element
a = {True, 2, False, "hi", "hello"}
print(a.pop())
print(a)