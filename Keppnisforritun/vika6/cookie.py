from heapq import heappush, heappop, heapify 

median = None
minPQ = []
maxPQ = []

first = 0
while True:
    #print("minna en, median og meira en:", maxPQ, median, minPQ)
    try:
        data = input()
    except EOFError as e:
        break
    if(first == 0):
        median = int(data)
        first += 1
        continue
    if data == "#":
        print(median)
        lengdMin = len(minPQ)
        lengdMax = len(maxPQ)
        if lengdMin == 0 and lengdMax == 0:
            median = None
            continue
        if lengdMin >= lengdMax:
            median = heappop(minPQ)
        else:
            median = -heappop(maxPQ)
    else:
        data = int(data)
        if median == None:
            median = data
            continue
        if data >= median:
            heappush(minPQ, data)
            if len(maxPQ) < len(minPQ):
                heappush(maxPQ, -median)
                median = heappop(minPQ)
        else:
            heappush(maxPQ, -data)
            if len(maxPQ) > len(minPQ) + 1:
                heappush(minPQ, median)
                median = -heappop(maxPQ)

        # if len(minPQ) >= len(maxPQ):
        #     heappush(maxPQ, -data)
        #     heappush(maxPQ, -median)
        #     median = -heappop(maxPQ)
        #     size =+ 1
        # else:
        #     heappush(minPQ, data)
        #     heappush(minPQ, median)
        #     median = heappop(minPQ)
        #     size =+ 1
    



    