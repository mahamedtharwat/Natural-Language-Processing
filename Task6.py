import re

# Regular expression pattern
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

# Test variable names
variable_names = ["valid_name", "_valid_name", "invalid-name", "123invalid", "invalid!name"]

# Check if each variable name is valid
for name in variable_names:
    if re.match(pattern, name):
        print(name, "is a valid variable name.")
    else:
        print(name, "is an invalid variable name.")
