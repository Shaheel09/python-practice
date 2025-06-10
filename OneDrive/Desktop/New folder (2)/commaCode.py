
def commaCode(sender):
    if len(sender) == 0:
        return 'lol'
    elif len(sender) == 1:
        return sender[0]
    else:
        convertString = ','.join(sender[:-1])
        convertString += ', and ' + sender[-1]
        return convertString

spam = ['apples','bananas','tofu','cats']

print(commaCode(spam))

bacon = ['bat','pet','bag','cpu']

print(commaCode(bacon))

until = ['1','2','3','4','5']

print(commaCode(until))

never = []

print(commaCode(never))

wrong = ['hello']

print(commaCode(wrong))