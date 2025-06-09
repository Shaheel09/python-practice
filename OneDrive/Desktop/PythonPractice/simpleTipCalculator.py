print('This program is use to for Simple Tip Calculator')



def calculateTip():
    billAmount = float(input('How much is the bill ?  '))
    tipPercentage = float(input('And how much is the TIP Percentage ? '))
    tipsAmount = billAmount * tipPercentage / 100
    totalAmount = billAmount + tipsAmount

    print(f'Your bill amount is ${billAmount: .2f}')
    print(f'Your tip amount is ${tipsAmount: .2f}')
    print(f'Your total amount to pay is ${totalAmount: .2f}')

calculateTip()