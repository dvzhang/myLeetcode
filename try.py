def rotationChar(c, rotation_places):
    if "a" <= c <= "z":
        c = chr(ord("a") + (ord(c)-ord("a") + rotation_places)%26)
    elif "A" <= c <= "Z":
        c = chr(ord("A") + (ord(c)-ord("A") + rotation_places)%26)
    elif "0" <= c <= "9":
        c = chr(ord("0") + (ord(c)-ord("0") + rotation_places)%10)
    else:
        c = ""
    return c

def rot(msg, rotation_places):
    ans = []
    for i in range(len(msg)):
        ans.append(rotationChar(msg[i], rotation_places))
    return "".join(ans)

print('Your output for msg=hello and rotation places=13 is', rot('xyz', 4))
print('Your output for msg=hello and rotation places=13 is', rot('hello', 13))
print('Your output for msg=hello and rotation places=13 is', rot('wow3', 12))
print('Your output for msg=hello and rotation places=13 is', rot('wow!!!', 12))