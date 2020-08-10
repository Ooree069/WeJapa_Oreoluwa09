#filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True. The code below uses filter() to get the names in cities that are fewer than 10 characters long to create the list short_cities. Give it a test run to see what happens.

#Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter().


cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

#def is_short(name):
 #   return len(name) < 10

short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)