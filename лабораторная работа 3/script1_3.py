a=''
s=0
while not(int(a.isdigit())):
    a=input('a= ')
b=''
while not( int(b.isdigit())):
    b=input('b= ')  
while a>=b:
    b=input('b= ')
for i in range(int(a),int(b)+1):
    s+=i
print('сумма: ', s)


