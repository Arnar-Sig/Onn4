inntak = input()
listi = inntak.split("-")
uttak = ""
for x in listi:
    uttak = uttak + x[0]
print(uttak)
