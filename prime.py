def prime(num):
    for i in range (2,num):
        if (num%i==0):
            return ("Non Prime number")
        else:
            return (" Prime number")
print(prime(7))