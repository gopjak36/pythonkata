# zero part:
def creditCardOutStanding(outStandingBalance, yearlyPercentRate, monthlyPercentRate):
    '''
    Input: outStandingBalance, yearlyPercentRate, monthlyPercentRate int or float variable
    Return: Remaining OutStandingBalance after 12 month mimimum paument every month.
    '''
    # help variable:
    month = 1
    # main part:
    while month < 13:
        minPay = round(outStandingBalance * monthlyPercentRate,2)
        balanceAfterMinPay = round(outStandingBalance - minPay,2)
        percent = round((yearlyPercentRate/12.0)*balanceAfterMinPay,2)
        outStandingBalance = round(balanceAfterMinPay + percent,2)
        print('Месяц '+str(month)+' Непогашенный Остаток: '+str(outStandingBalance) + ' | Минимальный Платеж в этом месяце: ' + str(minPay))
        month +=1
    # final part:
    return "Непогашенный Остаток составляет: " + str(outStandingBalance)

# test part:
print(creditCardOutStanding(3329,0.2,0.03)) # --> 2816.55
print(creditCardOutStanding(341,0.12,0.05)) # --> 207.63
print(creditCardOutStanding(168,0.15,0.06)) # --> 92.81
