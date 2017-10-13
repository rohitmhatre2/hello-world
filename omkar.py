a=input("Enter sentence here")
c=0
d=0
for i in a:
    if(i=='a'or i=='e' or i=='i' or i=='0' or i=='u'):
     c=c+1
print('number of vowels are:')
print(c)
a=len(a)
print('number of consonants is:',a-c)
d=d+1
if(i==' '):
   print('number of d sentences:',d)    
