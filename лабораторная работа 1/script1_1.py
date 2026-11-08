import math
print('='*100)
al=float(input('A= '))
bt=float(input('B= '))

a=math.exp(al+bt)+(1/(al+bt))
x=math.sqrt(a**2+bt**2)
y=math.log10(a+x)/(al*math.sin(a+x))
print('при float:  {0:.2f}'.format(a), '{0:.2f}'.format(x), '{0:.2f}'.format(y),'    ',al,bt)
#####

al1=int(al)
bt1=int(bt)

a1=math.exp(al1+bt1)+(1/(al1+bt1))
x1=math.sqrt(a1**2+bt1**2)
y1=math.log10(a1+x1)/(al1*math.sin(a1+x1))
print('при int:     {0:.2f}'.format(a1), '{0:.2f}'.format(x1), '{0:.2f}'.format(y1),'    ',al1,bt1)

print('='*100)