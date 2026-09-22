# Task 3
original_list = [
    {'make': ' Google ', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sorted_list = sorted(original_list, key=lambda x: x['color'])

print("Original list of dictionaries :", original_list)
print("Sorting the List of dictionaries :", sorted_list)
