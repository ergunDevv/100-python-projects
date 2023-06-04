# Iterative way
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
# new_list.append(add_1)
# print(new_list)


# List comprehension
# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)


# list comprehension string
# name = "Rein"
# letters_list = [letter for letter in name]
# print(letters_list)

# list comprehension range
# number_list = [n*2 for n in range(1, 5)]
# print(number_list)

# list comprhension with if
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)
