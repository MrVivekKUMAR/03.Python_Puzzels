######## Method 1 - Using Lambda Function

oddEven=(lambda x:x%2==0)
print (f'output from Method 1 : {oddEven(3)}')  # Print False if number is Odd, Print Even if number is Even

##### Method 2 Equivalant code

def oddEven1(x):
    return True if x%2==0 else False

print (f'output from Method 2 : {oddEven1(10)}')