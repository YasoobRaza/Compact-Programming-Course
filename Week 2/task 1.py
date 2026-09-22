# Task 1
def sort_tuple_list(tup_list):
    return sorted(tup_list, key=lambda x: x[-1])

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Original List:", sample_list)
print("Expected Result:", sort_tuple_list(sample_list))
