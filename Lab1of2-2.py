#Quiz: Assign and Modify Variables
#Now it's your turn to work with variables. The comments in this quiz (the lines that begin with #) have instructions for creating and modifying variables. After each comment write a line of code that implements the instruction.

#Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

# Write your function here. Make sure to use "population_density" as the name of the fucntion. so, the test below works.
def population_density (number_of_people, land_area) :
    return number_of_people / land_area
	

# test cases for your function Dont change anything below this comment.

test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))