# set_operations.py
fruits = {"apple", "banana", "mango", "orange"}
print("Initial set of fruits:", fruits)

fruits.add("grape")
print("After adding grape:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)

if "apple" in fruits:
    print("Apple is present in the set.")
else:
    print("Apple is not present in the set.")

print("Total number of fruits in the set:", len(fruits))
