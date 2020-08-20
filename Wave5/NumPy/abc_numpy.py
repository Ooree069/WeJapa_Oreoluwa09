#Create a numpy array of strings containing letters 'a' through 'j' (inclusive) of the alphabet. Then, use numpy array attributes to print the following information about this array:

#dtype of array

#shape of array
#size of array

#The code you submit in the code editor below will not be graded. Use the results from your code below, along with what you remember from the previous video, to complete the quiz below the code editor.



import numpy as np

# create numpy array of letters a-j
letter_array = np.array(['a','b','c','d','e','f','g','h','i','j'])
print("Letter Array: ", letter_array)

# get dtype of array
print('dtype:', letter_array.dtype)

# get shape of array
print('shape:', letter_array.shape)

# get size of array
print('size:', letter_array.size)