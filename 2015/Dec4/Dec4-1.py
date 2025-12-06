import hashlib
input, found, num = open("Dec4.txt", "r"), False, 0

for i in input: 
    while found == False: 
        if hashlib.md5((i + str(num)).encode()).hexdigest().startswith("00000"): 
            print(num)
            found = True
        
        num += 1