#Coding Quiz: Check for Prime Numbers
#Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

#For instance, 6 has four factors: 1, 2, 3, 6.
#1 X 6 = 6
#2 X 3 = 6
#So we know 6 is not a prime number.

#In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.


## Your code should check if each number in the list is a prime number

# the numbers are prime, the code should print "[number] is a prime number."
#If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".
#Example output:

#7 IS a prime number
#26 is NOT a prime number, because 2 is a factor of 26

check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

#def prime(check_prime):
#    for num in check_prime:
  #      if num % 2 == 1 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
   #         print("{} is a prime number.".format(num))
   #     else:
 #           print("{} is not a prime number.".format(num))
for num in check_prime:
    if num > 1:
        for i in range (2,num):
            if (num % i) == 0:
                print("{} is not a prime number.".format(num))
                break
        else:
            print("{} is a prime number.".format(num))
        
    else:
            print("{} is a not a prime number.".format(num))
#print(prime(check_prime))     
    
# all non_prime numbers must be divisible by either one of 2,3,5 or 7
