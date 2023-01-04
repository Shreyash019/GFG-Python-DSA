def palindrome(number):
    rev = 0
    temp = number
    while(temp>0):
        rd = temp%10
        rev = rev*10+rd
        temp = temp//10
    return rev


number = int(input('Enter the number to check palindrome:: '))
print(number==palindrome(number))