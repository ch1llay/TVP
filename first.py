import re

pattern = "0*(10)*"

if re.fullmatch(pattern, input()) != None:
    print("Ok")
else:
    print("Not match")