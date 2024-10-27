def reverse_string(string):
    reversed_str = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_str += string[i]
    return reversed_str

# Example usage:
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)
