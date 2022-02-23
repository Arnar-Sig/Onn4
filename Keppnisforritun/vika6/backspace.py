data = input()
nytt = []

i = 0
j = 0
lengd = len(data)
while j < len(data):
    if data[j] == "<":
        while j < lengd and data[j] == "<" :
            nytt.pop()
            j += 1
        continue   
        
    else:
        nytt.append(data[j])
    j += 1

print(''.join(nytt))

# for x in data:
#     if ord(x) == 60:
#         strengur = strengur[:-1]
#     else:



