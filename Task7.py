import re

def find_sequences(text):
    pattern = r"[A-Z][a-z]+"
    sequences = re.findall(pattern, text)
    return sequences

# Test string
test_string = "This is a TestString with SeveralUpperCaseSequences AndALongerOneHere."

# Find sequences of one uppercase letter followed by lowercase letters
result = find_sequences(test_string)
print("Sequences of one uppercase letter followed by lowercase letters:")
print(result)
