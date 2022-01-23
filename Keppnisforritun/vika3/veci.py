inntak = input()
orgNumber = int(inntak)
arr = [int(i) for i in inntak]




def intArrayToInt(array):
    strengur = [str(integer) for integer in array]
    semStrengur = "".join(strengur)
    semInt = int(semStrengur)
    return semInt

def check(array):
    # athuga ef ekki hægt
    #athuga 5554
    firstBigger = 1
    for x in array[1:]:
        if x > array[0]:
            firstBigger = 0
            break
    if firstBigger == 1:
        print(0)
        return

    # athuga hvort þurfi að skipta á fyrsta staf
    changeFirst = 1
    curr = array[1]
    for x in array[2:]:
        if x > curr:
            changeFirst = 0
            break
    #print("Changefirst:", changeFirst)

    # case 1: þarf að skipta á fyrsta staf
    if changeFirst == 1:
        utkoma = []
        first = array[0]
        sorted = [i for i in array]
        sorted.sort()
        for x in sorted:
            if x > first:
                utkoma.append(x)
                sorted.remove(x)
                break
        for x in sorted:
            utkoma.append(x)
        print(intArrayToInt(utkoma))
        return
    
    # case 2: ef þarf ekki að skipta á fyrsta staf
    # FÁ 1118 RÉTT!
    if changeFirst == 0:
        #utkoma = []
        #utkoma.append(array[0])
        index = len(array) - 1
        while index > 1:
            if array[index-1] < array[index]:
                temp = array[index]
                array[index] = array[index-1]
                array[index-1] = temp
                break
            index = index - 1
        print(intArrayToInt(array))





        # isDone = 0
        # arrayOrg = [i for i in array]
        # utkoma = [] 
        # utkoma.append(array[0])
        # array.remove(array[0])
        # sorted = [i for i in array]
        
        # for x in range(1, len(arrayOrg)):
        #     if isDone == 0:
        #         for y in sorted:
        #             print("er ad skoda arrayorg[x] og stak í sorted:", arrayOrg[x], y)
        #             if y > arrayOrg[x]:
        #                 print("bæti við y í utkomu:", y)
        #                 utkoma.append(y)
        #                 sorted.remove(y)
        #                 isDone = 1
        #                 break
    
        # for x in sorted:
        #     utkoma.append(x)
        # #print("utkoma:", intArrayToInt(utkoma))
        # print(intArrayToInt(utkoma))
check(arr)



