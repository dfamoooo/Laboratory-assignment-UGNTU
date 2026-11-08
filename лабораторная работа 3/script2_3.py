import math
while True:
    s = input('N= ')
    try:
        N = int(s)
    except ValueError:
        print('Ошибка: N не число')
        continue
    K = math.log(N, 2)
    k = f'{K:.2f}'
    if k[-3:] != '.00':
        print('Ошибка: K не целое число')
        continue
    break
print('>>', k)


text=input('введите текст:')
res=text.lower()
print(res)
