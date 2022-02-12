
def knap(capacity, length, weights, values):
    # setja upp tvívítt fylki með indexi og þyngdum
    for index in range(length+1):
        for thyngd in range(capacity+1):
            #print("index og thyngd:", index, thyngd)
            #print("current geymsla:", geymsla)
            if index == 0 or thyngd == 0:
                geymsla[index][thyngd] = 0
            elif weights[index-1] <= thyngd:
                #print("er inni elif")
                #print("max:", max(values[index-1] + geymsla[index-1][thyngd - weights[index-1]],
                #geymsla[index-1][thyngd]))

                geymsla[index][thyngd] = max(values[index-1] + geymsla[index-1][thyngd - weights[index-1]],
                geymsla[index-1][thyngd])
            else:
                #print("er inni else")
                geymsla[index][thyngd] = geymsla[index-1][thyngd]
    
    #print("geymsla:",geymsla)
    # fara í gegnum fylkið afturábak og finna indexa sem passa best
    thyngd = capacity
    curr = geymsla[length][capacity]
    count = 0
    indices = []
    #print("curr:", geymsla[n][capacity])
    for i in range(length, 0, -1):
        #print(geymsla[i][thyngd])
        #print(geymsla)
        # if curr <= 0:
        #     break
            #print("er i curr <= 0 og i:", i)
        #print("i-1 og thyngd:", (i-1), thyngd)
        if curr == geymsla[i-1][thyngd]:
            #print("er i geymsla[i-1][thyngd] == curr")
            continue
        else:
            #print(weights[i-1])
            thyngd = thyngd - weights[i-1]
            curr = curr - values[i-1]
            count += 1
            indices.append((i-1))
    print(count)
    strengur = ""
    for x in range(len(indices)):
        print(indices[x], end=" ")
  
    
            
while True:
    data = []
    data = input().split()
    capacity = int(data[0])
    n = int(data[1])
    weights = []
    values = []
    geymsla = []
    indices = []
    count = 0
    for x in range(n):
        data = input().split()
        values.append(int(data[0]))
        weights.append(int(data[1]))
    #geymsla = [[0]*(capacity+1)]*(n+1)
    geymsla = [[0 for x in range((capacity + 1))] for y in range((n + 1))]
    #print(n)
    #print(geymsla)
    #print(weights)
    #print(values)
   
    knap(capacity, n, weights, values)

    #print(geymsla)


# # Brute !
# def knapBrute(capacity, i, weights, values):
#     if capacity == 0 or i == 0:
#         return 0
#     if capacity < weights[i-1]:
#         return knapBrute(capacity, i-1, weights, values)
#     else:
#         return max(knapBrute(capacity, i-1, weights, values),
#                 knapBrute(capacity - weights[i], i-1, weights, values) + values[i])
# for test in range(30):
#     data = input().split()
#     capacity = int(data[0])
#     n = int(data[1])
#     weights = []
#     values = [] = []
#     for x in range(n):
#         data = input().split()
#         values.append(int(data[0]))
#         weights.append(int(data[1]))
#     print(knapBrute(capacity, n-1, weights, values))


    
