is_male = False
is_tall = False
# or, and

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a a male but tall")
else:
    print("you are neither male nor tall")


is_boy = False
if is_boy:
    print("9")
#nothing will be printed here as it is false
else:
    print("6")

#if statements and comparisions: >= <= == !=
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,9,8))

