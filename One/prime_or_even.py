def primeOrEven(num):
    if num % 2 == 0: # % sign is called a modulus and it just another name for remainder
        return f"{num} is an even number"
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return f"{num} is not a prime number" # f-string f"{varible} constant"
        
    return f"{num} is a prime number"

number = primeOrEven(121)
print(number)