import re

#assumes name is first letter capitalized of first name and last name
def find_date(line):
    pattern = r"[A-Z][a-z]{1,10} [A-Z][a-z]{1,10}"
    result = re.findall(pattern,line)
    newPattern = r"[A-Z][a-z]{1,10},? ?[A-Z][a-z]{1,10}"
    result = result + re.findall(newPattern,line)
    return result


f = open("namefile.dat")
for line in f.readlines():
    #print(line)
    result = find_date(line)
    if (len(result)>0):
        print(result)
