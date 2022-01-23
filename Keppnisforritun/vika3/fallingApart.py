n = int(input())
data = [int(x) for x in input().split()]    
a = 0
b = 0
data.sort(reverse=True)
index = 0
    length = len(data)

while index < length:
    if index%2==0:
        a = a + data[index]
    else:
        b = b + data[index]
    index = index + 1
print(a, b)