# Dictionaries are mutable data structures that allow you to store key-value pairs.
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}
# get element in dictionary similar to lists but  works with name of the keys instead of  indexes.
# print(programming_dictionary['Bug'])


# Adding element to dictionary
programming_dictionary['Loop'] = 'The action of doing something over and over again.'
print(programming_dictionary)

# Wiping the dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
# programming_dictionary['Loop'] = 'hey'
# print(programming_dictionary)

# Loop through the dictionary
for element in programming_dictionary:
    print(element)
    print(programming_dictionary[element])

# Nesting Dictionary in a Dictionary

travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    "Germany": ['Berlin', 'Hamburg', 'Stuttgart']
}

new_travel_log = {
    "France": {"cities_visited": ['Paris', 'Lille', 'Dijon'], "total_visits": 10},
    "Germany": {"cities_visited": ['Berlin', 'Hamburg', 'Stuttgart'], "total_visits": 4}
}
# Get the first element of the dictionary's dictionary
print(new_travel_log['France']['cities_visited'][0])
print(new_travel_log['Germany']['total_visits'])

# Nesting a dictionary inside a list
list_travel_log = [
    {
        "country": "France",
        "cities_visited": ['Paris', 'Lille', 'Dijon'],
        "total_visits": 10
    },
    {
        "country": "Germany",
        "cities_visited": ['Berlin', 'Hamburg', 'Stuttgart'],
        "total_visits": 10
    }
]
