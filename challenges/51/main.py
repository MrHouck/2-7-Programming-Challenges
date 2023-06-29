import sys
from mpmath import *
import timeit


def summation(k):
    num = mp.fac(6*k) * (545140134*k + 13591409)
    den = mp.fac(3*k) * (mp.fac(k))**3 * mp.power(mpf(-262537412640768000),k)
    res = num/den

    if k > 0:
        return res + summation(k - 1)
    else:
        return res
    



def chudnovsky(k):
    mp.prec = k+1
    numerator = mp.sqrt(mpf(10005))*426880
    denominator = nsum(lambda n: (mp.fac(6*n) * (545140134*n + 13591409))
     /
     (mp.fac(3*n) * (mp.fac(n))**3 * mp.power(mpf(-262537412640768000),n))
     , [0, inf])
    return numerator/denominator

k = int(input("How many digits do you want to calculate: "))
# To get the real number of iterations we have to do to get K digits, we have to do some math stuff
# https://mathoverflow.net/questions/261162/chudnovsky-algorithm-and-pi-precision
k *= log10(151931373056000)


start = timeit.default_timer()
pi_estimate = chudnovsky(k)
stop = timeit.default_timer()
print(pi_estimate)
print(f"Calculated in {stop-start} seconds")
#TODO: Idk why but when I put K as 1000, it only spits out ~300 digits instead of the expected 1000
#idk if this is some complicated math thing completely beyond me but it works so who cares