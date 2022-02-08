# OG
from xmlrpc.client import MAXINT
def subsetSum(X, i, T):
    if T == 0:
        return True
    elif T < 0 or i == 0:
        return False
    else:
        med = subsetSum(X, i-1, T - X[i])
        an = subsetSum(X, i-1, T)
    return med or an

def CountSS(X, i, T, count):
    if T == 0:
        return count + 1
    elif T < 0 or i == 0:
        return count
    else:
        med = CountSS(X, i-1, T - X[i], count)
        an = CountSS(X, i-1, T, count)
    return med + an

listinn = [0,1,2,3,4,5,6,7]
print("fjöldi mismunandi hlutmengja með summu 26:",CountSS(listinn,len(listinn)-1, 26, 0))
print("fjöldi mismunandi hlutmengja með summu 25:",CountSS(listinn,len(listinn)-1, 25, 0))

def ValueSS(X, V, i, T, val):
    if T == 0:
        return val
    elif T < 0 or i == 0:
        return float("-inf")
    else:
        med = ValueSS(X, V, i-1, T - X[i], val + V[i])
        an = ValueSS(X, V, i-1, T, val)
    # med = int(med)
    # an = int(an)
    return max(med, an)

listinn = [0,1,2,3,4,5,6,7]
values = [10,3,7,6,4,9,4,1]
print("max value með summu 27:",ValueSS(listinn, values, len(listinn)-1, 27, 0))
print("max value með summu 26:",ValueSS(listinn, values, len(listinn)-1, 26, 0))
print("max value með summu 29:",ValueSS(listinn, values, len(listinn)-1, 29, 0))
