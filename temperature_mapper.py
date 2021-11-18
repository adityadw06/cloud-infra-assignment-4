#code snippets borrowed from lecture and then modified
import sys

for line in sys.stdin:
    line = line.strip()
    temperature = int(line[87:92])
    yearMonthDay = line[15:23]
    quality = int(line[92])
    #accepted quality flags
    include = [0,1,4,5,9]
    if ((temperature != 9999)):
        #excluding readings which do not have quality flag as 0,1,4,5 or 9
        if quality in include:
            print('%s\t%d' % (yearMonthDay, temperature))