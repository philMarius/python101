'''Learning python comprehensions'''

# Lists

VEC = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
VEC_2 = [num for elem in VEC for num in elem]

print(VEC)
print(VEC_2)

# Dicts

ANIMALS = {1: 'dog', 2: 'cat', 3: 'hamster'}
print(ANIMALS)
print({value:key for key, value in ANIMALS.items()})

# Primes

NO_PRIMES = [j for i in range(2, 8) for j in range(i*2, 50, i)]
PRIMES = [x for x in range(2, 50) if x not in NO_PRIMES]
print(PRIMES)
