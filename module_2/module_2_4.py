numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    is_prime = True
    if numbers[i] != 1:
       for j in range(2, numbers[i]):
           if numbers[i] % j == 0:
               is_prime = False
               break
    else:
        continue
    if is_prime == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print("Primes: ", primes)
print("Not primes: ", not_primes)