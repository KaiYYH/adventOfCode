import re


s = "1-3 a: abcde"

result = re.split(r"[-: ]", s)

print(result)