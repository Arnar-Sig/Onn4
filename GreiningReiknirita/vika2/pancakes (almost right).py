# O(1) skv. fyrirmælum
def flip(listi, k):
    left = k
    right = len(listi) - 1
    while left < right:
        temp = listi[left]
        listi[left] = listi[right]
        listi[right] = temp
        right = right - 1
        left = left + 1

#stærsta pönnukaka = 0, minnsta pönnukaka = lengd á lista - 1
def pancakeFlip(listi):
    org = listi.copy()
    finished = 0
    count = 0
    while  finished < len(listi):
        curr = finished

        # leit að stærstu pönnuköku er hugsað sem O(1) skv. fyrirmælum
        while curr < len(listi):
            if listi[curr] == finished:
                if curr != finished:
                    flip(listi, curr)
                    if curr != finished:
                        flip(listi, finished)
                        count = count + 2
                    else: count = count + 1
                finished = finished + 1
                break
            curr = curr + 1

    print("upphaflegi staflinn: ", org, "| raðaðar pönnukökur: ", listi, " og fjöldi snúninga sem þurfti:", count)

# pancakeFlip([0, 1, 2, 3])
pancakeFlip([1, 2, 0])
# pancakeFlip([3, 2, 1, 0])
# pancakeFlip([4, 2, 1, 3, 0])
# pancakeFlip([1, 2, 3, 5, 0, 4])
# pancakeFlip([1, 2, 3, 8, 4, 6, 7, 0, 5, 9])