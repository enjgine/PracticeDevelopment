import time
starttimer = time.time_ns()/1000000

dicttest = {}

for i in range(1,1000000):
    for x in range(1,10):
        dicttest[i] = x

endtimer = (time.time_ns()/1000000)-starttimer
print(endtimer)

starttimer = time.time_ns()/1000000

mathtest = 0

for i in range(1,1000000):
    for x in range(1,10):
        mathtest += x

endtimer = (time.time_ns()/1000000)-starttimer
print(endtimer)