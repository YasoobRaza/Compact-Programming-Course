# Task 4
def strings_to_list_of_lists(str_list):
    return list(map(list, str_list))

sample_strings = ["Python", "Task", "Four"]
print("Original list of strings:", sample_strings)
print("List of lists:", strings_to_list_of_lists(sample_strings))
