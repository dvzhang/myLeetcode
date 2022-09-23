# Read from the file file.txt and output all valid phone numbers to stdout.
# grep -P '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt


def isNum(num):
    return ord(num) >= ord("0") and ord(num) <= ord("9")

def valid(line):
    if line[0] == "(":
        for i in [1,2,3,6,7,8,10,11,12,13]:
            if not isNum(line[i]):
                return False
        if line[4:6] != ") " or line[9] != "-":
            return False
        return True
    else:
        for i in [0,1,2,4,5,6,8,9,10,11]:
            if not isNum(line[i]):
                return False
        if line[3] != "-" or line[7] != "-":
            return False
        return True


with open("file.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    if valid(line):
        print(line)




