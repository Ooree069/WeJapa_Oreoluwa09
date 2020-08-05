#Nearest Square
#Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

#For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40

# write your while loop here
# while limit == 40:
# import math

square_list = [] 
for num in range(40):
    if (num ** (.5) == int(num ** (.5))):
        square_list.append(int(num))
while max(square_list) < limit :
    limit = max(square_list) 
    nearest_square = limit

print(nearest_square)