import math; import operator
input = open("Dec22_Input.txt", "r")

first = []
iterations = 2000
secrets = []
sum = 0

for i in input: 
    first.append(int(i.split("\n")[0]))

def next_secret_number(current): 
    sixtyfour = current * 64
    next = mix(current, sixtyfour)
    thirtytwo = math.floor(next / 32)
    next = mix(next, thirtytwo)
    twentyfortyeight = next * 2048
    next = mix(next, twentyfortyeight)
    return next

def mix(a, b): 
    return operator.xor(a, b) % 16777216

for num in first: 
    for it in range(iterations): 
        num = next_secret_number(num)
    secrets.append(num)

for secret in secrets: 
    sum += secret

print(sum)