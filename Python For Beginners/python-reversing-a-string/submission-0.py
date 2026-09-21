def reverse_string(input_string: str) -> str:
    length1 = len(input_string)
    length = length1 + 3
    return(input_string[length::-1])

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
