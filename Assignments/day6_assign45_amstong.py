'''The below function is written to check whether a given three digit number is an Armstrong number.'''
def find_armstrong(number):
    temp=0
    while(number!=0):
        remainder=number%10
        number=number/10
        temp+=(remainder*remainder*remainder)
    if(number==temp):
        return True
    return False

number=371
if(find_armstrong(number)):
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")
