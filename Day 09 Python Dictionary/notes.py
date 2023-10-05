# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# # # retrieving items from dictionary
# # print(programming_dictionary["Bug"])
#
# # adding new item to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
#
# # loop
# for key in programming_dictionary:
#     print(key)  # print the key only
#     print(programming_dictionary[key])  # print the value only
#
# # print(programming_dictionary)


# student_scores = {
#     "Harry": 81,
#     "Samuel": 95,
#     "James": 87,
#     "Jacob": 79,
# }
#
# for key in student_scores:
#     print(student_scores[key])


# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Nice"]
}

# Nesting a dictionary in a dictionary
travel_log_visited = {
    "France": {"City visited": ["Paris", "Lille", "Nice"], "total_visits": 12},
    "Germany": {"City visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}


def add_new_country(name, time_visited, cities_visited):
    new_country = ()
    new_country["country"] = name
    new_country["visited"] = time_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


print(travel_log)
print(travel_log_visited["Germany"])

add_new_country("US", '3', "Dallas")

