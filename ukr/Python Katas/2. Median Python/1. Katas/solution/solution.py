# random part:
import random   # import random module
random_number = random.randint(0,101) # random one number from 0 to 100
print("Random number is: ",random_number)

# help variables:
low_number = 0
hight_number = 100
count = 0

# main part:
while True:

  answer_number = (hight_number+low_number)//2
  count += 1

  if answer_number == random_number:
    print('Рандомне число це: ', answer_number, 'Використано входів: ', count)
    break
  else:
    if answer_number > random_number:
      hight_number = answer_number
    elif answer_number < random_number:
      low_number = answer_number
