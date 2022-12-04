######## Method 1
def primenumber(number):
    prime_no=True
    div=number-1
    while div>1:
        rem = (number%div)
        if rem==0:
            prime_no = False
            break
        else:
            div-=1 #reduced the number by 1 to check if remainder is zero (for non-prime or not (prime)
    return prime_no

print(primenumber(17))
print(primenumber(18))


