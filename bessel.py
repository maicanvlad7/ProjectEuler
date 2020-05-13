# bessel1 = 0,1717
# bessel2 = 0,2346
# rel path = C:/Users/maica/Desktop/depi lab/besselCoef.txt

import math

Bessel = []

Bessel.append(0.1717)
Bessel.append(0.2346)

print(Bessel)

f = open("C:/Users/maica/Desktop/depi lab/besselCoef.txt", "a")
f.truncate(0)
t = open("C:/Users/maica/Desktop/depi lab/besselFinal.txt", "a")
t.truncate(0)

def computeBessel(n):
    Bessel.append( 2*i/15*Bessel[n]-Bessel[n-1] )
    return Bessel[n]


#pt poz
for i in range(0,10):
    Bessel[i] = computeBessel(i)
    f.write(str(i) + ' ' + str(Bessel[i]) + '\n')

#pt neg
for i in range(-1,-10,-1):
    Bessel[i] = -1**(i)*Bessel[-1*i]
    f.write(str(i) + ' ' + str(Bessel[i]) + '\n')

f.close()

amp = []

for j in range(-7,7):
    Ampl = (1*Bessel[j] + 1.25*Bessel[j+5]*math.cos(3.14/6) + 1.25*Bessel[j-5]*math.cos(3.14/6))*math.cos(3.14/6)
    t.write(str(j) + ' coefBessel = ' + str(Bessel[j]) + '  ampl = ' + str(Ampl) + '\n')
    amp.append(Ampl)

sum = 0

for i in range(0,14):
    sum = sum + (amp[i]*amp[i])/2
    finalSum = 1/2 * sum

finalSum = finalSum / 1000
print(finalSum)



