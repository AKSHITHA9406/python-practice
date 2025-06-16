# dictionary_operations.py

students = {
    "Alice": 20,
    "Bob": 21,
    "Charlie": 22
}

print("Initial dictionary:", students)

# Adding a new student
students["David"] = 23
print("After adding David:", students)

# Updating age for one student
students["Bob"] = 25
print("After updating Bob's age:", students)

# Deleting one student
del students["Alice"]
print("After deleting Alice:", students)

# Printing all student names and ages
print("All students and their ages:")
for name, age in students.items():
    print(name, ":", age)
