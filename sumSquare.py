sumOfSquares = 0
squareOfSum = 0

for x in range(1,101):
    sumOfSquares = sumOfSquares + x*x
    squareOfSum = squareOfSum + x

print(squareOfSum*squareOfSum - sumOfSquares)