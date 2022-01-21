from doctest import DocFileSuite


inntak = input().split()
uttak = ""
wentInLoop = 0

for x in inntak:
    if "flatbaka" in x:
        uttak = uttak + "petsa" + x[8:] + " "
        continue
    elif "bauk" in x:
        #uttak = uttak + "dos" + x[4:] + " "
        uttak = uttak + "dos "
        continue
    elif x.istitle():
        uttak = uttak + x + " "
        continue
    # elif x == "Flatbakan":
    #     uttak = uttak + "Flatbakan "
    #     continue
    # elif x == "Bauk":
    #     uttak = uttak + "Bauk "       
    #     continue 
    else:
        for y in x:
            if y == "k":
                uttak = uttak + "g"
            elif y == "y":
                uttak = uttak + "u"
            else:
                uttak = uttak + y
        uttak = uttak + " "
    wentInLoop = 1

if wentInLoop:
    uttak = uttak[:-1]   
print(uttak)



# wentInLoop = 0
# for x in inntak:
#     if x == "Flatbakan":
#         uttak = uttak + "Flatbakan "
#         continue
#     if x == "Bauk":
#         uttak = uttak + "Bauk "
#         continue
#     if x == "bauk":
#         uttak = uttak + "dos "
#         continue
#     if x == "flatbaka":
#         uttak = uttak + "petsa "
#         continue
#     for y in x:
#         if y == "k":
#             uttak = uttak + "g"
#         elif y == "y":
#             uttak = uttak + "u"
#         else:
#             uttak = uttak + y
#     uttak = uttak + " "
#     wentInLoop = 1
# if wentInLoop:
#     uttak = uttak[:-1]
# print(uttak)



