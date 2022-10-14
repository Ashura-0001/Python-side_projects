range_limit_start = int(input("from where do you need the prime nos. ? \n"))
range_limit_end = int(input("till where do you need the prime nos. ? \n"))
prime_nos = []
range_chosen = []
not_prime = []
for i in range (range_limit_start, range_limit_end):
    range_chosen.append(i)
    for j in range (2, i):
        mod = i%j
        if mod == 0:
            not_prime.append(i)
            break
        elif mod != 0:
            continue
prime_nos.extend(list(set(range_chosen)-set(not_prime)))
prime_nos.sort()
print ( "the value of prime_nos is ", prime_nos)