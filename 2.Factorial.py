############ Method 1
factorial=lambda(x: )



############ Method 2
def factorial1(i):
    fact=i
    while i>2:
        fact = fact * (i-1)
        i-=1
    return fact

print (factorial1(6))