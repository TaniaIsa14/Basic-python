'''
Tuple
------
tuplename=(value1,value2,value3...........)

'''
magician=('sajib','shujon','sabyassci','saida')
print(magician)
for x  in magician:
    print(x)

digits=(12,36,56,7,89,9,78,34,23)
print(digits)
print(max(digits))
print(min(digits))
print(sum(digits))

players=('Armn','shuvo','gulshan','Rina','Maruf')
print(players[0:2])
actors=players[:]
print(actors)
print(dir(actors))
print(actors.index('gulshan'))
print(actors.count('gulshan'))
