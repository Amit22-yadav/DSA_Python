def reverse_array(arr):
    return arr[::-1]

array = input("Enter the array to reverse: ")
reversed_array = reverse_array(array)
print("Original Array: ", array)
print("Reversed Array: ", reversed_array)