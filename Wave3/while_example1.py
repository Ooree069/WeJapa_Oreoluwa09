#Count By
#Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

#Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? What condition will you use to see when it's time to stop looping?

#After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. It is the case that break_num should be a number that is the first number larger than end_num.




start_num = 120  #provide some start number
end_num = 600  #provide some end number that you stop when you hit
count_by = 12  #provide some number to count by 
break_num = start_num
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
while break_num <= end_num:
    break_num = break_num + count_by
    print (break_num) 

print(break_num)