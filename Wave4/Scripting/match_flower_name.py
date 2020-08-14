#For the following practice question you will need to write code in Python in the workspace below. This will allow you to practice the concepts discussed in the Scripting lesson, such as reading and writing files. You will see some older concepts too, but again, we have them there to review and reinforce your understanding of those concepts.

#Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

#Sample Output:

#>>> Enter your First [space] Last name only: Bill Newman
#>>> Unique flower name with the first letter: Bellflower

# Write your code here

# HINT: create a dictionary from flowers.txt
flower_dict = {} 
with open("flowers.txt") as flower_names:
    for line in flower_names:
        (key, value) = line.strip().split(":")[:2]
        flower_dict[key.strip()] = value.strip()
    print(flower_dict) 
   
# HINT: create a function
def flower_name(name):
    one = name[0]
    return flower_dict.get(one)

name = input("Enter your First [space] Last name only: ")
print("Unique flower name with the first letter: ",flower_name(name)) 