#COUNT UNIQUE WORDS

#Your task for this quiz is to find the number of unique words in the text. In the code editor below, complete these three steps to get your answer.
#1. Split verse into a list of words. Hint: You can use a string method you learned in the previous lesson.
#2. Convert the list into a data structure that would keep only the unique elements from the list.
#3. Print the length of the container.

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements

verse_set = set(verse_list) 
print(verse_set, '\n') 

# print the number of unique words
num_unique = sum(verse_set.values())
print(num_unique, '\n')
