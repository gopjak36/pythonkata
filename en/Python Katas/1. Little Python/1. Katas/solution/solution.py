s = "ogbobbobobozobobojbobobsobob" # some bob's-string example --> 7

# help variable:
count = 0
bob = 0

# main part:
for letter in s:

    if count == 0 and letter == 'b':
        count = 1

    elif count == 1 and letter == 'o':
        count = 2

    elif count ==2 and letter == 'b':
        bob +=1
        count = 1

    else:
        if letter == 'b' and count == 1:
            pass
        else:
            count = 0

# final print:
print('Bob occurs times: ', bob)
