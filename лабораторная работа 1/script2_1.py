# №2
import math
print('='*100)
a=float(input('a= '))
b=float(input('b= '))
y=float(input('угол: '))
if a>0 and b>0 and y>0:
    Y=math.radians(y)
    S=math.ceil((a*b*math.sin(Y))/2)
    c=math.sqrt( b**2+a**2-2*b*a*(float(math.cos(Y))) )

    ha=2*S/a
    hb=2*S/b
    hc=2*S/c
    if a+b>c and c+b>a and c+a>b:
        print('Высоты: ', '{0:.2f}'.format(ha), '{0:.2f}'.format(hb), '{0:.2f}'.format(hc), )
    else:
        print('такого треугольника не существует')
print('='*100)