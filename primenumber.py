def is_prime(n):
    if n<2:
        return False
    else:
        flag=False
        for i in range (2,n):
            if(n%i==0):
                flag=True
                break
        if flag==True:
            return False
        else:
            return True
# the function defined bellow is known as modular exponentiation used by Diffie Hellman problem
# base is public, modulus is public, exponent is private

def mod_exp(base, exponent, modulus):
    result=1
# we are running a loop since if we don't that then it will be a large scale calculation and which will hence decrease the time efficiency
    for i in range (exponent):
        result=(result*base)%modulus
    return result