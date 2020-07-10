# code to figure out the sum of random numbers that appear throughout a file
import re
file = open('regex_sum_709834.txt')
lst = list()
for line in file :
    line = line.rstrip()
    # in 8 it's to find the numbers in each line using regular expressions
    num = re.findall('[0-9]+', line)
    if len(num) < 1 :
        continue
    # I had to find the sum so I had to change the contents of num (which is a list) a from a string to an int, is there a better way to do this than using map?
    num = list(map(int, num))
    # I couldn't think of a way to sum each list (num) from each loop, so I decided to append each num after each line in another list and-
    lst.append(sum(num))
# put the sum function for the new list out of the loop to print
print(sum(lst))
