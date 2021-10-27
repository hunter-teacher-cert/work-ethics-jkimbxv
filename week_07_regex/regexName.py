import re


def find_date(line):
    pattern = r"[A-Z]?[a-z]{1,20},? ?[A-Z]?[a-z]{1,20}"
    result = re.findall(pattern,line)
    return result


#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)

f = open("namefile.dat")
for line in f.readlines():
    #print(line)
    result = find_date(line)
    if (len(result)>0):
        print(result)
