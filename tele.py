val = input("Enter your number: ")

OperatorA = {
    '1':0.9,
    '268':5.1,
    '46':0.17,
    '4620':0.0,
    '468':0.15,
    '4631':0.15,
    '4673':0.9,
    '46732':1.1
}

OperatorB = {
    '1':0.92,
    '44':0.5,
    '46':0.2,
    '467':1.0,
    '48':1.2,
}



def compare (num):

    if num in OperatorA and num in OperatorB:
        if OperatorA[num] > OperatorB[num]:
            return OperatorB[num]
        else:
            return OperatorA[num]
    elif num in OperatorA:
        return OperatorA[num]
    elif num in OperatorB:
        return OperatorB[num]
    else:
        return 'false'


ans='Prefix not found'
for i in range (1,6):
    if compare(val[0:i]) == 'false':
        i += 1
    else:
        ans = 'The cheapest price is ' + str(compare(val[0:i])) + ' per minute'

print(ans)

