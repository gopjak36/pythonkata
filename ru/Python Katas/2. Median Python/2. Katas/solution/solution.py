# zero part:
def creditCardLowPay(OutStandingBalance, yearlyPercentRate):
    '''
    Input: OutStandingbalance, yearlyPercentRate int or float variable.
    Return: Lowest Payment every month for pay the debt.
    '''
    # help variables:
    start_balance = OutStandingBalance
    minPay = 10
    count = 0

    # main part:
    while True:
	# help variables in main part:
        month = 1
        OutStandingBalance = start_balance
        count +=1
	# main algorithm:
        while month < 13:
            balanceAfterMinPay = round(OutStandingBalance - minPay,2)
            percent = round((yearlyPercentRate/12.0)*balanceAfterMinPay,2)
            OutStandingBalance = round(balanceAfterMinPay + percent,2)
            month +=1
        # verify part:
        if OutStandingBalance <=0:
            return 'Минимальный Платеж каждый месяц составляет: ' + str(minPay) + ' | Попыток использовано: ' + str(count)
        else:
            minPay +=10

# test part:
print(creditCardLowPay(5123,0.2)) # --> 470 | 47
print(creditCardLowPay(11,0.18)) # --> 10 | 1
print(creditCardLowPay(858,0.2)) # --> 80 | 8
