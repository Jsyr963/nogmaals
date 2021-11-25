# name of student: John Youssef
# number of student: 99067606
# purpose of program: 
# function of program:
# structure of program: 



toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay
tweeeuro=0
eeneuro=0
vijftigcent=0
twintigcent=0
tiencent=0
vijfcent=0
tweecent=0
eencent=0


if change > 0: #
  coinValue = 200 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 200:
      tweeeuro=nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      eeneuro=nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      vijftigcent=nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      twintigcent=nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      tiencent=nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      vijfcent=nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      tweecent=nrCoinsReturned
      coinValue = 1
    elif coinValue == 1:
      eencent=nrCoinsReturned
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
print(tweeeuro, "x 2 =",tweeeuro * 2)
print(eeneuro, "x 1 =",eeneuro * 1 )
print(vijftigcent, "x 0.5 =",vijftigcent * 0.5 )
print(twintigcent, "x 0.2 =",twintigcent * 0.2 )
print(tiencent, "x 0.1 =",tiencent * 0.1 )
print(vijfcent, "x 0.05 =",vijfcent * 0.05 )
print(tweecent, "x 0.02 =",tweecent * 0.02 )
print(eencent, "x 0.01 = ", eencent * 0.01 )