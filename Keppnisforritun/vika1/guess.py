
def binarySearch():
    low = 1
    high = 1000
    while low<= high:
        mid = low + ((high - low)//2)
        print(mid, flush=True)
        target = input()
        if target == "correct":
            break
        elif target == "higher":
            low = mid + 1
        else:
            high = mid -1


binarySearch()


# import sys
# currentNumber = 500
# jumps = [250, 125, 75, 37, 19, 9, 5, 2, 1]
# round = 0
# while 1:
#     print(currentNumber)
#     sys.stdout.flush()
#     inntak = input()
#     if inntak == "correct":
#         break
#     elif inntak == "higher":
#         currentNumber = currentNumber + jumps[round]
#         round = round + 1
#     else:
#         currentNumber = currentNumber - jumps[round]
#         round = round + 1

