# help variable:
num = int(input('Your number: '))
number = num
binary_num = ''

# main part:
''' Ckeck num negative or not '''
if num < 0:
    isNeg = True
else:
    isNeg = False

''' Conver num to binary '''

if num == 0:
    binary_num = '0'

while num > 0:
    binary_num = str(num % 2) + binary_num
    num = num // 2

if isNeg:
    binary_num = '-' + binary_num

# final print:
print('"Двоичное число от %s это %s' % (number, binary_num))
