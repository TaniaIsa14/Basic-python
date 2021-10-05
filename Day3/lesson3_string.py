'''
string
'''
s = 'Have a nice day'
print('original text:  '+s)
print('Upper case:'+s.upper())
print('lower case : '+s.lower())
print('capitalize case : '+s.capitalize())
print('title case : '+s.title())
print('swap case : '+s.swapcase())
print('count : '+str(s.count('a')))
print('count total number of character : '+str(len(s)))
print('center: '+s.center(50))
print('center: '+s.center(50, '#'))
print('Replace: '+s.replace('nice', 'good'))
print('find :' + str(s.find('nice')))
print('index:' + str(s.index('nice')))
print('find            :    ' + str(s.find('Nice')))
#print('index            :    ' + str(s.index('Nice'))) ValueError: substring not found
print('split           :    ' + str(s.split()))  # return list[]
print(dir(s))
