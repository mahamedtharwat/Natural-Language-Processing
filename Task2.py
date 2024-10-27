def are_all_integers(lst):
    for item in lst:
        if not isinstance(item, int):
            return False
    return True

# Given list
list1 = [100, 200, 300, 'A', 400, 500]

# Check if all items are integers
if are_all_integers(list1):
    print("All items in the list are integers.")
else:
    print("Not all items in the list are integers.")
