print('='*100)
import math
u=input('Напряжение (в Вольт): ')
i=input('Сила тока (в Ампер): ')
while not(str(u).isdigit()) or not( str(i).isdigit()):
    print('wrong! try again')
    u=input('Напряжение (в Вольт): ')
    i=input('Сила тока (в Ампер): ')

while not(12<float(u) and float(u)<1000) or not(0.1<float(i) and float(i)<500):
    print('wrong! try again')
    u=input('Напряжение (в Вольт): ')
    i=input('Сила тока (в Ампер): ')
 
U=float(u)
I=float(i)
name='err'
while name=='err':
    N=int(input('Тип нагрузки: '))
    match N:
        case 1:
            name='активная' 
            f=1.0
        case 2:
            name='индуктивная'
            f=0.85
        case 3:
            name='смешанная'
            f=0.75
        case _:
            name='err'
            f=0
    if name=='err':
        print('error: this type doesnt exist')


F=math.radians(f)
P=U*I*math.cos(F)/1000
if U<220:
    state='низкое напряжение'
elif 220<=U<=400:
    state='нормальное напряжение'
else:
    state='высокое напряжение'

print('Тип нагрузки:', name,'|','cosf=', '{0:.2f}'.format(math.cos(F)),'|','мощность: {0:.2f}'.format(P),'|','Класс напряжения:', state)

print('='*100)