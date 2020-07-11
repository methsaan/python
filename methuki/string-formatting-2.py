#! /usr/bin/python3

brand = 'Apple'  ## string with % operator %s
exchangeRate = 3.14567899 ## float with % operator %f
count = 1234 ## integer with % operator %d

print ('The %s was too expensive to be bought at %1.4f and the %d was too low a count' %(brand, exchangeRate, count))

#print ('The ' + brand + ' was too expensive to be bought at ' + float(exchangeRate) + ' and the ' + int(count) + ' was too low a count')
