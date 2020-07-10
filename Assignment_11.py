import re
file = open('regex_sum_709834.txt')
lst = list()
for line in file :
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) < 1 :
        continue
    num = list(map(int, num))
    lst.append(sum(num))
print(sum(lst))
