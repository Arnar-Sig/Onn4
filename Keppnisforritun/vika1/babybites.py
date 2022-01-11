number = int(input())
data = input()
listi = data.split()
isOk = 1
for x in range(number):
    #print("listi[x]: ", listi[x])
    #print("x: ", x+1)
    if listi[x] != "mumble":
        if int(listi[x]) != x+1:
            isOk = 0
        

if isOk == 1:
    print("makes sense")
else:
    print("something is fishy")