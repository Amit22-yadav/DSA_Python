# Reverse string using for loop
def reverse_string(input):
    result = " "
    for char in input:
      result = char + result
    return result 
user_input = input("Enter the String You want to reverse :- ")
output = reverse_string(user_input)
print(output)

# Reverse string using String Slicing
string_input = input("Enter the String:- ")
output = string_input[::-1]
print(output)