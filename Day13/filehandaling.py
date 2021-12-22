'''
File Handaling
--------------
Two open a file object in python is 
file_object=open('filename','more')
the modes are:
'r'  --> read mode
'w'  --> write mode
'a'  --> append mode
'''
f=open('tania.txt','w')
f.write('This is our new text file\n')
f.write('This is our another line\n')
f.write('Today make my day \n')
f.close()

#open a file for read mode
file=open('tania.txt','r')
#print(file.read())
#print(file.read(7))
print(file.readlines())

file.close()


#add some more data

f=open('tania.txt','a')
f.write('The Erie County Fair is a fair held in Hamburg in Erie County, \n')
f.write('This is our another line\n')
f.write('Today lucky day')
f.close()
file=open('tania.txt','r')
print(file.read())