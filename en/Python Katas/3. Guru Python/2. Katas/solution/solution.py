# zero part
def creditCardMinPay_BS(outStandingBalance, yearlyPersentRate):
    '''
    Input: outStandingBalance, yearlyPersentRate int or float variable
    Return: Lowest Payment after 12 month
    '''
    # hepl variables:
    start_balance = outStandingBalance
    monthlyPercentRate = yearlyPersentRate/12
    lowerPay = start_balance/12
    upperPay = (start_balance * (1 + monthlyPercentRate)**12)/12.0
    epsilon = 0.03
    count = 0

    # main part:
    while abs(outStandingBalance) > epsilon:
        # help variables of main part:
        minPay = (upperPay + lowerPay)/2
        outStandingBalance = start_balance
        count +=1
        # main algorithm:
        for i in range(12):
            outStandingBalance = outStandingBalance - minPay + ((outStandingBalance - minPay) * monthlyPercentRate)
        # verify part:
        if outStandingBalance > epsilon:
            lowerPay = minPay
        elif outStandingBalance < -epsilon:
            upperPay = minPay
        else:
            break
    # final part:
    minPay = round(minPay, 2)
    return 'Minimum Payment every month:' + str(minPay) + ' | Count used: ' + str(count) 


# test part:
print(creditCardMinPay_BS(320000,0.2)) # --> 29157.09; 17
print(creditCardMinPay_BS(999999,0.18)) # --> 90325.02; 22
print(creditCardMinPay_BS(999999,0.18)) # --> 32809.62; 20
